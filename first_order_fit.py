import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use("./style/simple_bold.mplstyle") #select stylesheet
from scipy.optimize import curve_fit #import linear regression from scipy

def first_order_fit_ethylphenol_concentration_profiles_and_write_to_DataFrame(filename: str = r"./vinylphenol transfer hydrogenation(data).parquet", dpi: int = 300) -> pd.DataFrame: #return 
    df = pd.read_parquet(filename) #import raw data
    df = df.query("temperature_C == 75") #filter the data for temperature
    FitData = pd.DataFrame(columns=["rxn_label", "catalyst", "formate_mM", "IPA_molefrac", "slope", "slope_stderr", "intercept", "intercept_stderr", "mass_activity", "mass_activity_stderr", "COD"]) #initialize fit results dataframe

    for catalyst in df.catalyst.unique():
        for formate_mM in sorted(df["formate_mM"].unique()):
            if df.query("catalyst == @catalyst & formate_mM == @formate_mM").empty:
                print(f"no data found for catalyst {catalyst} and formate concentration {formate_mM}. skipping...")
                continue #skip conditions for which there is no data
            
            color_list = ['darkblue', '#58a8f9', 'darkgreen'] #colors for plots
            fig, ax = plt.subplots(1,1)

            for IPA_molefrac, color in zip(sorted(df["IPA_molefrac"].unique()), color_list):
                ax.scatter(df.query("catalyst == @catalyst & formate_mM == @formate_mM & IPA_molefrac == @IPA_molefrac").time_min, 
                            df.query("catalyst == @catalyst & formate_mM == @formate_mM & IPA_molefrac == @IPA_molefrac").ethylphenol_mM, c=color, edgecolor='k')              
                DF = df.query("catalyst == @catalyst & formate_mM == @formate_mM & IPA_molefrac == @IPA_molefrac") #fit only the linear portion of the data
                
                for rxn in DF.rxn_label.unique(): #loop over unique reaction labels
                    xdata, ydata = DF[DF["rxn_label"] == rxn]["time_min"], DF[DF["rxn_label"] == rxn]["ethylphenol_mM"]
                    def first_order (t, C_0, k):
                        C = C_0*(1-np.exp(-k*t))
                        return C

                    fit_result, covariance = curve_fit(first_order, xdata, ydata, bounds=(-100, 100), p0=[18, 0.02])
                    SE = np.sqrt(np.diag(covariance))
                    C_0_SE, k_SE = SE[0], SE[1]
                    print(f"Coefficient ± SE C_0: {fit_result[0]:0.2f} ± {C_0_SE:0.2f}, k: {fit_result[1]:0.2f} ± {k_SE:0.2f}")
                    #plot data and fit
                    x_fit = np.linspace(DF["time_min"].min(), DF["time_min"].max(), 100) #generate x values for fit curve
                    y_fit = first_order(x_fit, fit_result[0], fit_result[1]) #generate y values using the fit parameters
                    plt.plot(x_fit, y_fit, color=color) #plot the fit curve
                    
                    ## WRITE TO NEW DATAFRAME
                    new_row = pd.DataFrame({
                    "rxn_label": [rxn],
                    "catalyst": [catalyst],
                    "formate_mM": [formate_mM],
                    "IPA_molefrac": [IPA_molefrac],
                    "rate_constant": [fit_result[1]],
                    "slope_stderr": [SE[1]],
                    "initial_concentration_mM": [fit_result[0]],
                    "initial_concentration_SE": [SE[0]],
                    "mass_normalized_rate_constant":[fit_result[1]/DF.query("rxn_label == @rxn").catalyst_mass.unique()], 
                    "mass_normalized_rate_constant_SE":[SE[1]/DF.query("rxn_label == @rxn").catalyst_mass.unique()]
                    })

                    FitData = pd.concat([FitData, new_row], ignore_index=True)

                    # print(f'catalyst = {catalyst}, formate concentration = {formate_mM}, IPA mole fraction = {IPA_molefrac}, rxn: {rxn} : mass activity = {fit_result.slope/DF.query("rxn_label == @rxn").catalyst_mass.unique():.2f} ± {fit_result.stderr/DF.query("rxn_label == @rxn").catalyst_mass.unique():.2f}, COD = {fit_result.rvalue:.2f}')
                    ##%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

            plt.xlabel("Time (min)") #add x-axis label
            plt.ylabel("Ethylphenol Concentration (mM)") #add y-axis label
            plt.title(f"catalyst = {catalyst}, [formate] = {formate_mM: .0f} mM") #add title
            fig.savefig(f"./fitted-concentration-profiles/first-order/fitted_ethylphenol_generation_vs_time_{catalyst}_{formate_mM}mM_formate_{dpi}dpi.png", dpi=dpi, bbox_inches='tight') #export the figure as a 900 dpi .png
            print(f'figure saved to "fitted_ethylphenol_generation_vs_time_{catalyst}_{formate_mM}mM_formate_{dpi}dpi.png"')
            fig.clf()
        FitData.to_parquet(f"./{catalyst}_first_order_fit_results.parquet")
        print(f'fit results saved to "{catalyst}_fitting_results.parquet"')
    return FitData

if __name__ == "__main__":
   first_order_fit_ethylphenol_concentration_profiles_and_write_to_DataFrame()