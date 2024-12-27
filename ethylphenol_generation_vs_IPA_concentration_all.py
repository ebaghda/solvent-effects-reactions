import pandas as pd
import matplotlib.pyplot as plt
plt.style.use("./style/simple_bold.mplstyle") #set plot style

fig, ax = plt.subplots(2,4,figsize=(38, 38/2)) #create a figure and axis

DF = pd.read_parquet(r"vinylphenol transfer hydrogenation(data).parquet") #import the data

df= DF.query("catalyst == 'Pd' & temperature_C == 75 & formate_mM == 10 & stock_batch_number >= 0") #filter the data

ax[0, 0].errorbar(df.IPA_molefrac, df.EP_generation_rate, yerr=df.EP_generation_rate_std_err, c="k", capsize=4, linewidth=1, zorder=0) #plot the standard error

df[df["IPA_molefrac"] == 0.0].plot.scatter("IPA_molefrac", "EP_generation_rate", ax=ax[0, 0], label="0% IPA",s=60, c="b", edgecolor="k") #plot the 0% IPA data
df[df["IPA_molefrac"] == 0.1].plot.scatter("IPA_molefrac", "EP_generation_rate", ax=ax[0, 0], label="10% IPA",s=60, c="#58a8f9", edgecolor="k") #plot the 10% IPA data
df[df["IPA_molefrac"] == 0.2].plot.scatter("IPA_molefrac", "EP_generation_rate", ax=ax[0, 0], label="20% IPA",s=60, c="g",edgecolor="k") #plot the 20% IPA data

df= DF.query("catalyst == 'Pd' & temperature_C == 75 & formate_mM == 100 & stock_batch_number >= 0") #filter the data
ax[0, 1].errorbar(df.IPA_molefrac, df.EP_generation_rate, yerr=df.EP_generation_rate_std_err, c="k", capsize=4, linewidth=1, zorder=0) #plot the standard error

df[df["IPA_molefrac"] == 0.0].plot.scatter("IPA_molefrac", "EP_generation_rate", ax=ax[0, 1], label="0% IPA",s=60, c="b", edgecolor="k") #plot the 0% IPA data
df[df["IPA_molefrac"] == 0.1].plot.scatter("IPA_molefrac", "EP_generation_rate", ax=ax[0, 1], label="10% IPA",s=60, c="#58a8f9", edgecolor="k") #plot the 10% IPA data
df[df["IPA_molefrac"] == 0.2].plot.scatter("IPA_molefrac", "EP_generation_rate", ax=ax[0, 1], label="20% IPA",s=60, c="g",edgecolor="k") #plot the 20% IPA data

df= DF.query("catalyst == 'Pd' & temperature_C == 75 & formate_mM == 1000 & stock_batch_number >= 0") #filter the data
ax[0, 2].errorbar(df.IPA_molefrac, df.EP_generation_rate, yerr=df.EP_generation_rate_std_err, c="k", capsize=4, linewidth=1, zorder=0) #plot the standard error

df[df["IPA_molefrac"] == 0.0].plot.scatter("IPA_molefrac", "EP_generation_rate", ax=ax[0, 2], label="0% IPA",s=60, c="b", edgecolor="k") #plot the 0% IPA data
df[df["IPA_molefrac"] == 0.1].plot.scatter("IPA_molefrac", "EP_generation_rate", ax=ax[0, 2], label="10% IPA",s=60, c="#58a8f9", edgecolor="k") #plot the 10% IPA data
df[df["IPA_molefrac"] == 0.2].plot.scatter("IPA_molefrac", "EP_generation_rate", ax=ax[0, 2], label="20% IPA",s=60, c="g",edgecolor="k") #plot the 20% IPA data

df= DF.query("catalyst == 'Pt' & temperature_C == 75 & formate_mM == 10 & stock_batch_number >= 0") #filter the data
ax[1, 0].errorbar(df.IPA_molefrac, df.EP_generation_rate, yerr=df.EP_generation_rate_std_err, c="k", capsize=4, linewidth=1, zorder=0) #plot the standard error

df[df["IPA_molefrac"] == 0.0].plot.scatter("IPA_molefrac", "EP_generation_rate", ax=ax[1, 0], label="0% IPA",s=60, c="b", edgecolor="k") #plot the 0% IPA data
df[df["IPA_molefrac"] == 0.1].plot.scatter("IPA_molefrac", "EP_generation_rate", ax=ax[1, 0], label="10% IPA",s=60, c="#58a8f9", edgecolor="k") #plot the 10% IPA data
df[df["IPA_molefrac"] == 0.2].plot.scatter("IPA_molefrac", "EP_generation_rate", ax=ax[1, 0], label="20% IPA",s=60, c="g",edgecolor="k") #plot the 20% IPA data

df= DF.query("catalyst == 'Pt' & temperature_C == 75 & formate_mM == 100 & stock_batch_number >= 0") #filter the data
ax[1, 1].errorbar(df.IPA_molefrac, df.EP_generation_rate, yerr=df.EP_generation_rate_std_err, c="k", capsize=4, linewidth=1, zorder=0) #plot the standard error

df[df["IPA_molefrac"] == 0.0].plot.scatter("IPA_molefrac", "EP_generation_rate", ax=ax[1, 1], label="0% IPA",s=60, c="b", edgecolor="k") #plot the 0% IPA data
df[df["IPA_molefrac"] == 0.1].plot.scatter("IPA_molefrac", "EP_generation_rate", ax=ax[1, 1], label="10% IPA",s=60, c="#58a8f9", edgecolor="k") #plot the 10% IPA data
df[df["IPA_molefrac"] == 0.2].plot.scatter("IPA_molefrac", "EP_generation_rate", ax=ax[1, 1], label="20% IPA",s=60, c="g",edgecolor="k") #plot the 20% IPA data


df= DF.query("catalyst == 'Pt' & temperature_C == 75 & formate_mM == 1000 & stock_batch_number >= 0") #filter the data
ax[1, 3].errorbar(df.IPA_molefrac, df.EP_generation_rate, yerr=df.EP_generation_rate_std_err, c="k", capsize=4, linewidth=1, zorder=0) #plot the standard error

df[df["IPA_molefrac"] == 0.0].plot.scatter("IPA_molefrac", "EP_generation_rate", ax=ax[1, 3], label="0% IPA",s=60, c="b", edgecolor="k") #plot the 0% IPA data
df[df["IPA_molefrac"] == 0.1].plot.scatter("IPA_molefrac", "EP_generation_rate", ax=ax[1, 3], label="10% IPA",s=60, c="#58a8f9", edgecolor="k") #plot the 10% IPA data
df[df["IPA_molefrac"] == 0.2].plot.scatter("IPA_molefrac", "EP_generation_rate", ax=ax[1, 3], label="20% IPA",s=60, c="g",edgecolor="k") #plot the 20% IPA data

for row in ax:
    for axi in row:
        axi.set_xlabel("IPA Concentration (mole/mole)", labelpad=15, fontsize=24) #add x axis label
        axi.set_ylabel("Ethylphenol Generation Rate (mM/g s)", labelpad=15, fontsize=24) #add y axis label
        axi.set_xticks([0, 0.1, 0.2]) #set x axis tick marks
        axi.set_xticklabels(["0", "0.1", "0.2"], fontsize=20) #set x axis tick labels
        axi.set_xlim(-0.05, 0.25) #set the x axis limits
        axi.set_ylim(-0.05, None) #set the y axis limits
        axi.legend().set_visible(False) #hide the legend
plt.annotate("catalyst\nNNN mM potassium formate", (0.02, 0.85), xycoords="axes fraction", fontsize=24, fontweight="bold") #add the catalyst label
plt.savefig("ethylphenol_generation_vs_IPA_concentration_all_900dpi.png", bbox_inches="tight", dpi=400) #save the figure as a 900 dpi .png
print('figure saved to "ethylphenol_generation_vs_IPA_concentration_all_900dpi.png"') #print success message