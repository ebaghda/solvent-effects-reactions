import numpy as np
import pandas as pd
from scipy.optimize import curve_fit

def linear_fit_all_and_rewrite_in_dataframe(filename: str = "vinylphenol transfer hydrogenation(data).parquet"):
    try:
        df = pd.read_parquet("vinylphenol transfer hydrogenation(data)_fitted.parquet")
    except: 
        df = pd.read_parquet(filename)
        
    new_columns = {"slope": np.nan, "slope_SE": np.nan, "intercept": np.nan, "intercept_SE": np.nan, "mass_activity": np.nan, "mass_activity_SE": np.nan}
    df = df.assign(**new_columns)
    print(df.head())

    # Define first order fitting function
    def first_order(x, m, b):
        y = m*x+b
        return y

    for rxn_label in df.rxn_label.unique():
        
        xdata = df[df["rxn_label"] == rxn_label].time_min[0:4] if df[df["rxn_label"] == rxn_label].formate_mM.unique() >= 250 else df[df["rxn_label"] == rxn_label].time_min
        ydata = df[df["rxn_label"] == rxn_label].ethylphenol_mM[0:4] if df[df["rxn_label"] == rxn_label].formate_mM.unique() >= 250 else df[df["rxn_label"] == rxn_label].ethylphenol_mM
        fit_result, covariance = curve_fit(first_order, xdata, ydata, bounds=(-1000, 1000), p0=[20, 0.5])
        if rxn_label == 115:
            print(xdata, ydata, df.formate_mM)
            # raise("stop")
        slope, intercept = fit_result[0], fit_result[1]
        SE = np.sqrt(np.diag(covariance))
        slope_SE, intercept_SE = SE[0], SE[1]
        print(f"Coefficient ± SE slope: {fit_result[0]:0.2f} ± {slope_SE:0.2f}intercept: {fit_result[1]:0.2f} ± {intercept_SE:0.2f}")
        df.loc[df["rxn_label"] == rxn_label, "slope"] = slope
        df.loc[df["rxn_label"] == rxn_label, "slope_SE"] = slope_SE
        df.loc[df["rxn_label"] == rxn_label, "intercept"] = intercept
        df.loc[df["rxn_label"] == rxn_label, "intercept_SE"] = intercept_SE
        df.loc[df["rxn_label"] == rxn_label, "mass_activity"] = slope/df[df["rxn_label"] == rxn_label].catalyst_mass.unique()[0]
        df.loc[df["rxn_label"] == rxn_label, "mass_activity_SE"] = slope_SE/df[df["rxn_label"] == rxn_label].catalyst_mass.unique()[0]
        

    print(df.head())
    df.to_parquet(filename.replace(".parquet", "_fitted.parquet"))
    print(f"Fitted data saved to {filename.replace('.parquet', '_fitted.parquet')}")
    return df

if __name__ == "__main__":
    df = linear_fit_all_and_rewrite_in_dataframe()
    df = df.query("catalyst == 'Pd' and temperature_C == 75")

    print(df.head())
    import matplotlib.pyplot as plt
    plt.style.use("./style/simple_bold.mplstyle") #select stylesheet

    catalyst = "Pd"
    dpi = 300
    fig, ax = plt.subplots(figsize=(5,5)) #initialize figure
    plt.errorbar(df.query("IPA_molefrac == 0")["formate_mM"], df.query("IPA_molefrac == 0")["mass_activity"], yerr=df.query("IPA_molefrac == 0")["mass_activity_SE"], fmt="", c='black', capsize=4, linewidth=1, zorder=0, marker="o", ls='none', markerfacecolor = 'b') #plot the standard error of each fit
    plt.errorbar(df.query("IPA_molefrac == 0.1")["formate_mM"], df.query("IPA_molefrac == 0.1")["mass_activity"], yerr=df.query("IPA_molefrac == 0.1")["mass_activity_SE"], fmt="", c='black', capsize=4, linewidth=1, zorder=0, marker="^", ls='none', markerfacecolor = '#58a8f9') #plot the standard error of each fit
    plt.errorbar(df.query("IPA_molefrac == 0.2")["formate_mM"], df.query("IPA_molefrac == 0.2")["mass_activity"], yerr=df.query("IPA_molefrac == 0.2")["mass_activity_SE"], fmt="", c='black', capsize=4, linewidth=1, zorder=0, marker="s", ls='none', markerfacecolor = 'g') #plot the standard error of each fit
    ax.legend(["0 mol% IPA", "10 mol% IPA", "20 mol% IPA"])
    plt.ylabel("Ethylphenol Generation Rate (mM/g min)") #set the ylabel
    plt.xlabel("Formate Concentration (mM)") #set the xlabel
    ax.set_xscale('log') # select the x scaling 
    ax.set_yscale('linear') #set the y scaling 
    fig.savefig(f"TESTethylphenol_generation_vs_formate_concentration_{catalyst}_{dpi}dpi.png", dpi=dpi, bbox_inches='tight') #export the figure as a 900 dpi .png
    print(f"saved figure as \"ethylphenol_generation_vs_formate_concentration_{catalyst}_{dpi}dpi.png\"") #print success message
    fig.clf()