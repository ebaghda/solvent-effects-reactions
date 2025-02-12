import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use("./style/simple_bold.mplstyle") #select stylesheet
from scipy.stats import linregress #import linear regression from scipy

def linear_fit_ethylphenol_concentration_profiles_and_write_to_DataFrame(filename: str = r"./vinylphenol transfer hydrogenation(data).parquet", dpi: int = 900) -> pd.DataFrame: #return 
    df = pd.read_parquet(filename) #import raw data
    df = df.query("temperature_C == 75") #filter the data for temperature
    FitData = pd.DataFrame(columns=["rxn_label", "catalyst", "formate_mM", "IPA_molefrac", "slope", "slope_stderr", "intercept", "intercept_stderr", "mass_activity", "mass_activity_stderr", "COD"]) #initialize fit results dataframe

    for catalyst in df.catalyst.unique():
        for formate_mM in sorted(df["formate_mM"].unique()):
            if df.query("catalyst == @catalyst & formate_mM == @formate_mM").empty:
                print(f"no data found for catalyst {catalyst} and formate concentration {formate_mM}. skipping...")
                continue #skip conditions for which there is no data
            
            color_list = ['darkblue', '#58a8f9', 'darkgreen'] #colors for plots
            shape_list = ['o', '^', 's']
            fig, ax = plt.subplots(1,1)

            for IPA_molefrac, color, shape in zip(sorted(df["IPA_molefrac"].unique()), color_list, shape_list):
                ax.scatter(df.query("catalyst == @catalyst & formate_mM == @formate_mM & IPA_molefrac == @IPA_molefrac").time_min, 
                            df.query("catalyst == @catalyst & formate_mM == @formate_mM & IPA_molefrac == @IPA_molefrac").ethylphenol_mM, c=color, marker=shape, edgecolor='k')              
                DF = df.query("catalyst == @catalyst & formate_mM == @formate_mM & IPA_molefrac == @IPA_molefrac & time_min <= 15") if formate_mM >= 250 else df.query("catalyst == @catalyst & formate_mM == @formate_mM & IPA_molefrac == @IPA_molefrac") #fit only the linear portion of the data
                
                for rxn in DF.rxn_label.unique(): #loop over unique reaction labels
                    fit_result = linregress(DF[DF["rxn_label"] == rxn]["time_min"], DF[DF["rxn_label"] == rxn]["ethylphenol_mM"]) #fit the data
                    x_fit = np.linspace(DF["time_min"].min(), DF["time_min"].max(), 2) #generate x values for fit curve
                    y_fit = fit_result.slope * x_fit + fit_result.intercept #generate y values using the fit parameters
                    plt.plot(x_fit, y_fit, color=color) #plot the fit curve
                    ax.annotate(f"{catalyst}\n{formate_mM} mM potassium formate", (0.02, 0.87), xycoords="axes fraction", fontweight="bold") #add the catalyst label to the plot

                    
                    ## WRITE TO NEW DATAFRAME
                    new_row = pd.DataFrame({
                    "rxn_label": [rxn],
                    "catalyst": [catalyst],
                    "formate_mM": [formate_mM],
                    "IPA_molefrac": [IPA_molefrac],
                    "slope": [fit_result.slope],
                    "slope_stderr": [fit_result.stderr],
                    "intercept": [fit_result.intercept],
                    "intercept_stderr": [fit_result.intercept_stderr],
                    "mass_activity":[fit_result.slope/DF.query("rxn_label == @rxn").catalyst_mass.unique()], 
                    "mass_activity_stderr":[fit_result.stderr/DF.query("rxn_label == @rxn").catalyst_mass.unique()], 
                    "COD": fit_result.rvalue
                    })

                    FitData = pd.concat([FitData, new_row], ignore_index=True)

                    ##%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

            plt.xlabel("Time (min)") #add x-axis label
            plt.ylabel("Ethylphenol Concentration (mM)") #add y-axis label
            #plt.title(f"catalyst = {catalyst}, [formate] = {formate_mM: .0f} mM") #add title
            fig.savefig(f"./fitted-concentration-profiles/linear/fitted_ethylphenol_generation_vs_time_{catalyst}_{formate_mM}mM_formate_{dpi}dpi.png", dpi=dpi, bbox_inches='tight') #export the figure as a 900 dpi .png
            print(f'figure saved to "fitted_ethylphenol_generation_vs_time_{catalyst}_{formate_mM}mM_formate_{dpi}dpi.png"')
            fig.clf()
        FitData.to_parquet(f"./{catalyst}_fitting_results.parquet")
        print(f'fit results saved to "{catalyst}_fitting_results.parquet"')
    return FitData

if __name__ == "__main__":
   linear_fit_ethylphenol_concentration_profiles_and_write_to_DataFrame()