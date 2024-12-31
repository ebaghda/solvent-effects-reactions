import pandas as pd
import matplotlib.pyplot as plt
plt.style.use("./style/simple_bold.mplstyle") #select stylesheet

catalyst = "Pd" #select the catalyst
formate_concentration = 500 #mM 

df = pd.read_parquet("vinylphenol transfer hydrogenation(data).parquet") #import the data


df = df.query("temperature_C == 75 & time_min <= 30")

fig, ax = plt.subplots() #initialize figure
'''
TODO:
    - Filter the data by catalyst, formate concentration, and isopropanol mole fraction.
    - Fit the data to a linear model.
    - Plot the data and the fit curve for each reaction.
    - Print the slope, intercept, and coefficient of determination (COD) for each reaction.
'''
plt.errorbar(df["formate_mM"], df["EP_generation_rate"], yerr=df["EP_generation_rate_std_err"], fmt="", c='black', capsize=4, linewidth=1, zorder=0, marker="", ls='none') #plot the standard error of each fit
plt.scatter(df_0pctIPA["formate_mM"], df_0pctIPA["EP_generation_rate"], marker='o', c='b', s=30) #plot the 0% IPA ethylphenol generation rates against formate concentration
plt.scatter(df_10pctIPA["formate_mM"], df_10pctIPA["EP_generation_rate"], marker='^', c="#58a8f9", s=30) #plot the 10% IPA ethylphenol generation rates against formate concentration
plt.scatter(df_20pctIPA["formate_mM"], df_20pctIPA["EP_generation_rate"], marker='s',  c='g', s=30) #plot the 20% IPA ethylphenol generation rates against formate concentration

plt.ylabel("Ethylphenol Generation Rate (mM/g min)") #set the ylabel
plt.xlabel("Formate Concentration (mM)") #set the xlabel
ax.set_xscale('log') # select the x scaling 
ax.set_yscale('linear') #set the y scaling 
fig.savefig("ethylphenol_generation_vs_formate_concentration_Pt_900dipi.png", dpi=900, bbox_inches='tight') #export the figure as a 900 dpi .png
print("saved figure as \"ethylphenol_generation_vs_formate_concentration_Pt_900dpi.png\"") #print success message