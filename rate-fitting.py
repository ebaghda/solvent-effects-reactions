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

DF = pd.read_parquet("vinylphenol transfer hydrogenation(data).parquet") #import the data
DF = DF.query("temperature_C == 75 & time_min <= 30") #filter the data

catalyst = "Pd" #select the catalyst %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
formate_mM = 2000 #mM %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
IPA_molefrac = 0.1 #mole fraction %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

DF = DF.query("catalyst == @catalyst & formate_mM == @formate_mM & IPA_molefrac == @IPA_molefrac") #filter the data
if formate_mM > 500:
    DF = DF.query("time_min == 0 | time_min == 5 | time_min == 10 | time_min == 15") #filter the data
DF.plot.scatter(x="time_min", y="ethylphenol_mM", s=8, c='k') #plot the data

for rxn in DF.rxn_label.unique(): #loop over unique reaction labels
    fit_result = linregress(DF[DF["rxn_label"] == rxn]["time_min"], DF[DF["rxn_label"] == rxn]["ethylphenol_mM"]) #fit the data
    a, b = fit_result[0:2] #extract the fit parameters
    x_fit = np.linspace(DF["time_min"].min(), DF["time_min"].max(), 100) #generate x values for fit curve
    y_fit = a * x_fit + b #generate y values using the fit parameters
    plt.plot(x_fit, y_fit, color='gray', label=f'slope = {a:.2f}, intercept = {b:.2f}, COD = {fit_result.rvalue:.2f}') #plot the fit curve

plt.legend() #add a legend
plt.xlabel("Time (min)") #add x-axis label
plt.ylabel("Ethylphenol Concentration (mM)") #add y-axis label
plt.title(f"catalyst = {catalyst}, [formate] = {formate_mM: .0f} mM, [IPA] = {IPA_molefrac: .0%}") #add title
plt.show() #show the plot

print(fit_result) #print the fit results