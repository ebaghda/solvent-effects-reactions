import numpy as np
import pandas as pd
from scipy.optimize import curve_fit

def fit_all_and_rewrite_in_dataframe(filename: str = "vinylphenol transfer hydrogenation(data).parquet") -> pd.DataFrame:
    try:
        df = pd.read_parquet("vinylphenol transfer hydrogenation(data)_fitted.parquet")
    except: 
        df = pd.read_parquet(filename)    

    new_columns = {"rate_constant": np.nan, "rate_constant_SE": np.nan, "initial_VP_concentration_mM": np.nan, "initial_VP_concentration_SE_mM": np.nan, "mass_normalized_rate_constant": np.nan, "mass_normalized_rate_constant_SE": np.nan}
    df = df.assign(**new_columns)
    print(df.head())

    # Define first order fitting function
    def first_order(t, C_0, k):
        C = C_0 * (1 - np.exp(-k * t))
        return C

    for rxn_label in df.rxn_label.unique():
        xdata = df[df["rxn_label"] == rxn_label].time_min
        ydata = df[df["rxn_label"] == rxn_label].ethylphenol_mM

        fit_result, covariance = curve_fit(first_order, xdata, ydata, bounds=(-1000, 1000), p0=[20, 0.5])
        C_0, k = fit_result[0], fit_result[1]
        SE = np.sqrt(np.diag(covariance))
        C_0_SE, k_SE = SE[0], SE[1]
        print(f"Coefficient ± SE C_0 (mM): {fit_result[0]:0.2f} ± {C_0_SE:0.2f}, k (/min): {fit_result[1]:0.2f} ± {k_SE:0.2f}")
        df.loc[df["rxn_label"] == rxn_label, "rate_constant"] = k
        df.loc[df["rxn_label"] == rxn_label, "rate_constant_SE"] = k_SE
        df.loc[df["rxn_label"] == rxn_label, "initial_VP_concentration_mM"] = C_0
        df.loc[df["rxn_label"] == rxn_label, "initial_VP_concentration_SE_mM"] = C_0_SE
        df.loc[df["rxn_label"] == rxn_label, "mass_normalized_rate_constant"] = k/df[df["rxn_label"] == rxn_label].catalyst_mass.unique()[0]
        df.loc[df["rxn_label"] == rxn_label, "mass_normalized_rate_constant_SE"] = k_SE/df[df["rxn_label"] == rxn_label].catalyst_mass.unique()[0]
        

    print(df.head())
    df.to_parquet(filename.replace(".parquet", "_fitted.parquet"))
    print(f"Fitted data saved to {filename.replace('.parquet', '_fitted.parquet')}")
    return df

if __name__ == "__main__":
    fit_all_and_rewrite_in_dataframe()