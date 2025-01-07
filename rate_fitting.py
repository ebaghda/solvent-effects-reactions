"""
Usage:
    1. Ensure the raw data file "vinylphenol transfer hydrogenation(data).parquet" is in the same directory as this script.
    2. Adjust the catalyst, formate concentration, and isopropanol mole fraction as needed.
    3. Run the script to generate the scatter plot and fit curves.
    4. The script will display the plot and print the fit results for each reaction.
Dependencies:
    - pandas
    - numpy
    - matplotlib
    - scipy
This script fits the data from the vinylphenol transfer hydrogenation reaction to a linear model. The data is filtered by catalyst, formate concentration, and isopropanol mole fraction. The script plots the data and the fit curve for each reaction. The mass activity, mass activity error, and coefficient of determination (COD) are printed for each concentration profile.
"""
import pandas as pd #import pandas
import numpy as np #import numpy
import matplotlib.pyplot as plt #import matplotlib.pyplot
plt.style.use("./style/simple_bold.mplstyle") #set plot stylesheet
from scipy.stats import linregress #import linear regression from scipy

def plot_fitting_results(filepath: str = r"vinylphenol transfer hydrogenation(data).parquet", dpi: int = 300, vertical_layout: bool = True, catalyst: str = "Pd"):

    from fit_ethylphenol_concentration_profiles import fit_ethylphenol_concentration_profiles_and_write_to_DataFrame
    DF = fit_ethylphenol_concentration_profiles_and_write_to_DataFrame(r"vinylphenol transfer hydrogenation(data).parquet", dpi = dpi)

    df=pd.read_parquet(f"{catalyst}_fitting_results.parquet")
    if vertical_layout:
        fig, ax = plt.subplots(len(df.formate_mM.unique()), 1, figsize = (5, 5*len(df.formate_mM.unique())))
    else:
        fig, ax = plt.subplots(1, len(df.formate_mM.unique()), figsize = (5*len(df.formate_mM.unique()), 5))

    formate_concentrations = list(reversed(sorted(df.formate_mM.unique()))) if vertical_layout else sorted(df.formate_mM.unique())
    print(formate_concentrations)

    for i in range(len(formate_concentrations)): #for each formate concentration
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
        ax[i].set_ylim(-0.3, 30) if catalyst == "Pd" else None #set the y axis limits
        
    plt.tight_layout() #correct the layout
    fig.savefig(f"ethylphenol_generation_vs_IPA_concentrationFIT_RESULT_panel_{catalyst}_{dpi}dpi.png", bbox_inches="tight", dpi=dpi) #save the figure as a 900 dpi .png
    print(f'figure saved to "ethylphenol_generation_vs_IPA_concentration_panel_{catalyst}_{dpi}dpi.png"') #print success message
        

if __name__ == "__main__":
    plot_fitting_results(r"vinylphenol transfer hydrogenation(data).parquet", dpi = 200, vertical_layout=False, catalyst = "Pt")
