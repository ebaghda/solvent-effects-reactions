"""
Usage:
    1. Ensure the data file "vinylphenol transfer hydrogenation(data).parquet" is in the same directory as this script.
    2. Adjust the catalyst, formate concentration, and isopropanol mole fraction as needed.
    3. Run the script to generate the scatter plot and fit curves.
    4. The script will display the plot and print the fit results for each reaction.
Dependencies:
    - pandas
    - numpy
    - matplotlib
    - scipy
This script fits the data from the vinylphenol transfer hydrogenation reaction to a linear model. The data is filtered by catalyst, formate concentration, and isopropanol mole fraction. The script plots the data and the fit curve for each reaction. The slope, intercept, and coefficient of determination (COD) are printed for each concentration profile.
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.style.use("./style/simple_bold.mplstyle") #set plot style
from scipy.stats import linregress

def load_and_filter_data(filepath: str, ) -> pd.DataFrame:
    df = pd.read_parquet(filepath)
    df = df.query("temperature_C == 75 & time_min <=30 & catalyst == 'Pd'")
    return df


def rate_fitting(filepath: str, dpi: int) -> pd.DataFrame: #retun 
    df = load_and_filter_data(filepath)
    FitData = pd.DataFrame(columns=["rxn_label", "catalyst", "formate_mM", "IPA_molefrac", 
                                    "slope", "slope_stderr", 
                                    "intercept", "intercept_stderr", 
                                    "mass_activity", "mass_activity_stderr"])

    for catalyst in df["catalyst"].unique():
        for formate_mM in sorted(df["formate_mM"].unique()):
            
            color_list = ['darkblue', '#58a8f9', 'darkgreen'] #colors for plots
            for IPA_molefrac, color in zip(sorted(df["IPA_molefrac"].unique()), color_list):
                df1 = df.query("catalyst == @catalyst & formate_mM == @formate_mM & IPA_molefrac == @IPA_molefrac") #filter the data
                plt.scatter(df1.time_min, df1.ethylphenol_mM, c=color, edgecolor='k')
                DF = df1.query("time_min <= 15") if formate_mM >= 250 else df1 #fit only the linear portion of the data
                for rxn in DF.rxn_label.unique(): #loop over unique reaction labels
                    fit_result = linregress(DF[DF["rxn_label"] == rxn]["time_min"], DF[DF["rxn_label"] == rxn]["ethylphenol_mM"]) #fit the data
                    x_fit = np.linspace(DF["time_min"].min(), DF["time_min"].max(), 2) #generate x values for fit curve
                    y_fit = fit_result.slope * x_fit + fit_result.intercept #generate y values using the fit parameters
                    plt.plot(x_fit, y_fit, color=color) #plot the fit curve
                    
                    
                    ## WRITE TO NEW DATAFRAME = -- throws error %%%%%%%%%%%%%%%%
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
                    "mass_activity_stderr":[fit_result.stderr/DF.query("rxn_label == @rxn").catalyst_mass.unique()]
                    })

                    FitData = pd.concat([FitData, new_row], ignore_index=True)

                    print(f'catayst = {catalyst}, formate concentration = {formate_mM}, IPA mole fraction = {IPA_molefrac}, rxn: {rxn} : slope = {fit_result.slope:.2f} ± {fit_result.stderr:.2f}, intercept = {fit_result.intercept:.2f} ± {fit_result.intercept_stderr:.2f}, COD = {fit_result.rvalue:.2f}')
                    ##%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

            plt.xlabel("Time (min)") #add x-axis label
            plt.ylabel("Ethylphenol Concentration (mM)") #add y-axis label
            plt.title(f"catalyst = {catalyst}, [formate] = {formate_mM: .0f} mM") #add title
            plt.savefig(f"./fitted-concentration-profiles/fitted_ethylphenol_generation_vs_time_{catalyst}_{formate_mM}mM_formate_{dpi}dpi.png", dpi=dpi, bbox_inches='tight') #export the figure as a 900 dpi .png
            print(f'figure saved to "fitted_ethylphenol_generation_vs_time_{catalyst}_{formate_mM}mM_formate_{dpi}dpi.png"')
            plt.clf()
    FitData.to_parquet(r"./fitting_results.parquet")
    print('fit results saved to "fitting_results.parquet"')
    return FitData


def plot_fitting_results(filepath, dpi):
    DF = rate_fitting(r"vinylphenol transfer hydrogenation(data).parquet", dpi = dpi)
    df=DF
    fig, ax = plt.subplots(1, len(df.formate_mM.unique()), figsize = (5*len(df.formate_mM.unique()), 5))

    formate_concentrations = df.formate_mM.unique()
    for i in range(len(formate_concentrations)): #for each formate concentration
        catalyst = "Pd"
        formate_concentration = formate_concentrations[i] #get the current formate concentration
        df = DF.query("formate_mM == @formate_concentration") #filter the data for the current formate concentration

        legend = ax[1].legend(["0% IPA", "10% IPA", "20% IPA"], loc="upper left") #add the legend
        legend.set_visible(False) #hide the legend

        ax[i].errorbar(df.query("IPA_molefrac == 0")["IPA_molefrac"], df.query("IPA_molefrac == 0")["mass_activity"], yerr=df.query("IPA_molefrac == 0")["mass_activity_stderr"], fmt="", c='black', capsize=4, linewidth=1, zorder=0, marker="o", ls='none', markerfacecolor = 'b') #plot the 00% IPA data
        ax[i].errorbar(df.query("IPA_molefrac == 0.1")["IPA_molefrac"], df.query("IPA_molefrac == 0.1")["mass_activity"], yerr=df.query("IPA_molefrac == 0.1")["mass_activity_stderr"], fmt="", c='black', capsize=4, linewidth=1, zorder=0, marker="^", ls='none', markerfacecolor = '#58a8f9') #plot 10% IPA data
        ax[i].errorbar(df.query("IPA_molefrac == 0.2")["IPA_molefrac"], df.query("IPA_molefrac == 0.2")["mass_activity"], yerr=df.query("IPA_molefrac == 0.2")["mass_activity_stderr"], fmt="", c='black', capsize=4, linewidth=1, zorder=0, marker="s", ls='none', markerfacecolor = 'g') #plot 20% IPA data
        
        ax[i].annotate(f"{catalyst}\n{formate_concentration} mM potassium formate", (0.02, 0.89), xycoords="axes fraction", fontweight="bold") #add the catalyst label
        
        ax[i].set_xlabel("IPA Concentration (mole/mole)", labelpad=5) #add x axis label
        ax[i].set_ylabel("Ethylphenol Generation Rate (mM/g min)", labelpad=5) #add y axis label
        ax[i].set_xticks([0, 0.1, 0.2]) #set x axis tick marks
        ax[i].set_xticklabels(["0", "0.1", "0.2"]) #set x axis tick labels
        ax[i].set_xlim(-0.05, 0.25) #set the x axis limits
        ax[i].set_ylim(-0.3, 30) #set the y axis limits
        
    plt.tight_layout() #correct the layout
    fig.savefig(f"ethylphenol_generation_vs_IPA_concentrationFIT_RESULT_panel_{catalyst}_{dpi}dpi.png", bbox_inches="tight", dpi=dpi) #save the figure as a 900 dpi .png
    print(f'figure saved to "ethylphenol_generation_vs_IPA_concentration_panel_{catalyst}_{dpi}dpi.png"') #print success message
        

if __name__ == "__main__":
    #FitData = rate_fitting(r"vinylphenol transfer hydrogenation(data).parquet", dpi = 250)
    # print("completed rate_fitting.py")
    # print(FitData.head(100).to_string())
    plot_fitting_results(r"vinylphenol transfer hydrogenation(data).parquet", dpi = 250)
