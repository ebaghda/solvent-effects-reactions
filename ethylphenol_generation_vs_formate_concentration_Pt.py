import pandas as pd
import matplotlib.pyplot as plt
plt.style.use("./style/simple_bold.mplstyle") #select stylesheet

DF = pd.read_parquet("vinylphenol transfer hydrogenation(data).parquet") #read .parquet data file 
df = DF.query("time_min == 0 & formate_mM >= 0 & catalyst == 'Pd'") #filter the data

print(df.head()) # check the first 5 rows are correct
print(df.tail()) #check the last 5 rows are correct

df_0pctIPA = df.query("IPA_molefrac == 0.0") #select 0% IPA
df_10pctIPA = df.query("IPA_molefrac == 0.1") #select 10% IPA
df_20pctIPA = df.query("IPA_molefrac == 0.2") #select 10% IPA

fig, ax = plt.subplots() #initialize figure
plt.errorbar(df["formate_mM"], df["EP_generation_rate"], yerr=df["EP_generation_rate_std_err"], fmt="", c='black', capsize=4, linewidth=1, zorder=0, marker="", ls='none') #plot the standard error of each fit
plt.scatter(df_0pctIPA["formate_mM"], df_0pctIPA["EP_generation_rate"], marker='o', c='b', s=30) #plot the 0% IPA ethylphenol generation rates against formate concentration
plt.scatter(df_10pctIPA["formate_mM"], df_10pctIPA["EP_generation_rate"], marker='^', c="#58a8f9", s=30) #plot the 10% IPA ethylphenol generation rates against formate concentration
plt.scatter(df_20pctIPA["formate_mM"], df_20pctIPA["EP_generation_rate"], marker='s',  c='g', s=30) #plot the 20% IPA ethylphenol generation rates against formate concentration

plt.ylabel("Ethylphenol Generation Rate (mM/g s)") #set the ylabel
plt.xlabel("Formate Concentration (mM)") #set the xlabel
ax.set_xscale('log') # select the x scaling 
ax.set_yscale('linear') #set the y scaling 
fig.savefig("ethylphenol_generation_vs_formate_concentration_Pd_900dipi.png", dpi=900, bbox_inches='tight') #export the figure as a 900 dpi .png
print("saved figure as \"ethylphenol_generation_vs_formate_concentration_Pd_900dpi.png\"") #print success message
