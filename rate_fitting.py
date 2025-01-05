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
    df = df.query("temperature_C == 75 & time_min <=30 & formate_mM > 10 & catalyst == 'Pd'")
    return df

def rate_fitting(filepath: str, dpi: int) -> None:
    color_list = ['darkblue', '#58a8f9', 'darkgreen']
    df = load_and_filter_data(filepath)
    for catalyst in df["catalyst"].unique():
        for formate_mM in sorted(df["formate_mM"].unique()):
            df0 = df.query("catalyst == @catalyst & formate_mM == @formate_mM")
                        
            for IPA_molefrac, color in zip(sorted(df0["IPA_molefrac"].unique()), color_list):
                df1 = df0.query("IPA_molefrac == @IPA_molefrac") #filter the data
                plt.scatter(df1.time_min, df1.ethylphenol_mM, c=color, edgecolor='k')
                DF = df1.query("time_min <= 15") if formate_mM >= 500 else df1 #filter the data
                for rxn in DF.rxn_label.unique(): #loop over unique reaction labels
                    fit_result = linregress(DF[DF["rxn_label"] == rxn]["time_min"], DF[DF["rxn_label"] == rxn]["ethylphenol_mM"]) #fit the data
                    x_fit = np.linspace(DF["time_min"].min(), DF["time_min"].max(), 2) #generate x values for fit curve
                    y_fit = fit_result.slope * x_fit + fit_result.intercept #generate y values using the fit parameters
                    plt.plot(x_fit, y_fit, color=color,zorder=0) #plot the fit curve

                    print(f'catayst = {catalyst}, formate concentration = {formate_mM}, IPA mole fraction = {IPA_molefrac}, rxn: {rxn} : slope = {fit_result.slope:.2f} ± {fit_result.stderr:.2f}, intercept = {fit_result.intercept:.2f} ± {fit_result.intercept_stderr:.2f}, COD = {fit_result.rvalue:.2f}')
            plt.legend(["0% IPA", "10% IPA", "20% IPA"]) #add a legend
            plt.xlabel("Time (min)") #add x-axis label
            plt.ylabel("Ethylphenol Concentration (mM)") #add y-axis label
            plt.title(f"catalyst = {catalyst}, [formate] = {formate_mM: .0f} mM") #add title
            plt.savefig(f"./fitted-concentration-profiles/fitted_ethylphenol_generation_vs_time_{formate_mM}mM_formate_{catalyst}_{dpi}dpi.png", dpi=dpi, bbox_inches='tight') #export the figure as a 900 dpi .png


if __name__ == "__main__":
    rate_fitting(r"vinylphenol transfer hydrogenation(data).parquet", dpi = 200)
    print("completed rate_fitting.py")