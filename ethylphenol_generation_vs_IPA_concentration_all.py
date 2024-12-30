import pandas as pd
import matplotlib.pyplot as plt
plt.style.use("./style/simple_bold1.mplstyle") #set plot style

fig, ax = plt.subplots(2,5,figsize=(50, 20)) #create a figure and axis

DF = pd.read_parquet(r"vinylphenol transfer hydrogenation(data).parquet") #import the data

df= DF.query("catalyst == 'Pd' & temperature_C == 75 & formate_mM == 10 & stock_batch_number >= 0") #filter the data

ax[0, 0].errorbar(df.IPA_molefrac, df.EP_generation_rate, yerr=df.EP_generation_rate_std_err, c="k", capsize=6, elinewidth=1.5, markeredgewidth=1.5, zorder=0) #plot the standard error

df[df["IPA_molefrac"] == 0.0].plot.scatter("IPA_molefrac", "EP_generation_rate", ax=ax[0, 0], label="0% IPA",s=250, c="b", edgecolor="k") #plot the 0% IPA data
df[df["IPA_molefrac"] == 0.1].plot.scatter("IPA_molefrac", "EP_generation_rate", ax=ax[0, 0], label="10% IPA",s=250, c="#58a8f9", edgecolor="k") #plot the 10% IPA data
df[df["IPA_molefrac"] == 0.2].plot.scatter("IPA_molefrac", "EP_generation_rate", ax=ax[0, 0], label="20% IPA",s=250, c="g",edgecolor="k") #plot the 20% IPA data
ax[0,0].annotate("Pd\n10 mM potassium formate", (0.02, 0.89), xycoords="axes fraction", fontsize=24, fontweight="bold") #add the catalyst label


df= DF.query("catalyst == 'Pd' & temperature_C == 75 & formate_mM == 100 & stock_batch_number >= 0") #filter the data
ax[0, 1].errorbar(df.IPA_molefrac, df.EP_generation_rate, yerr=df.EP_generation_rate_std_err, c="k", capsize=6, elinewidth=1.5, markeredgewidth=1.5, zorder=0) #plot the standard error

df[df["IPA_molefrac"] == 0.0].plot.scatter("IPA_molefrac", "EP_generation_rate", ax=ax[0, 1], label="0% IPA",s=250, c="b", edgecolor="k") #plot the 0% IPA data
df[df["IPA_molefrac"] == 0.1].plot.scatter("IPA_molefrac", "EP_generation_rate", ax=ax[0, 1], label="10% IPA",s=250, c="#58a8f9", edgecolor="k") #plot the 10% IPA data
df[df["IPA_molefrac"] == 0.2].plot.scatter("IPA_molefrac", "EP_generation_rate", ax=ax[0, 1], label="20% IPA",s=250, c="g",edgecolor="k") #plot the 20% IPA data
ax[0, 1].annotate("Pd\n100 mM potassium formate", (0.02, 0.89), xycoords="axes fraction", fontsize=24, fontweight="bold") #add the catalyst label

df= DF.query("catalyst == 'Pd' & temperature_C == 75 & formate_mM == 500 & stock_batch_number >= 0") #filter the data
ax[0, 2].errorbar(df.IPA_molefrac, df.EP_generation_rate, yerr=df.EP_generation_rate_std_err, c="k", capsize=6, elinewidth=1.5, markeredgewidth=1.5, zorder=0) #plot the standard error

df[df["IPA_molefrac"] == 0.0].plot.scatter("IPA_molefrac", "EP_generation_rate", ax=ax[0, 2], label="0% IPA",s=250, c="b", edgecolor="k") #plot the 0% IPA data
df[df["IPA_molefrac"] == 0.1].plot.scatter("IPA_molefrac", "EP_generation_rate", ax=ax[0, 2], label="10% IPA",s=250, c="#58a8f9", edgecolor="k") #plot the 10% IPA data
df[df["IPA_molefrac"] == 0.2].plot.scatter("IPA_molefrac", "EP_generation_rate", ax=ax[0, 2], label="20% IPA",s=250, c="g",edgecolor="k") #plot the 20% IPA data
ax[0, 2].annotate("Pd\n500 mM potassium formate", (0.02, 0.89), xycoords="axes fraction", fontsize=24, fontweight="bold") #add the catalyst label

df= DF.query("catalyst == 'Pd' & temperature_C == 75 & formate_mM == 1000 & stock_batch_number >= 0") #filter the data
ax[0, 3].errorbar(df.IPA_molefrac, df.EP_generation_rate, yerr=df.EP_generation_rate_std_err, c="k", capsize=6, elinewidth=1.5, markeredgewidth=1.5, zorder=0) #plot the standard error

df[df["IPA_molefrac"] == 0.0].plot.scatter("IPA_molefrac", "EP_generation_rate", ax=ax[0, 3], label="0% IPA",s=250, c="b", edgecolor="k") #plot the 0% IPA data
df[df["IPA_molefrac"] == 0.1].plot.scatter("IPA_molefrac", "EP_generation_rate", ax=ax[0, 3], label="10% IPA",s=250, c="#58a8f9", edgecolor="k") #plot the 10% IPA data
df[df["IPA_molefrac"] == 0.2].plot.scatter("IPA_molefrac", "EP_generation_rate", ax=ax[0, 3], label="20% IPA",s=250, c="g",edgecolor="k") #plot the 20% IPA data
ax[0, 3].annotate("Pd\n1000 mM potassium formate", (0.02, 0.89), xycoords="axes fraction", fontsize=24, fontweight="bold") #add the catalyst label

df= DF.query("catalyst == 'Pd' & temperature_C == 75 & formate_mM == 2000 & stock_batch_number >= 0") #filter the data

ax[0, 4].errorbar(df.IPA_molefrac, df.EP_generation_rate, yerr=df.EP_generation_rate_std_err, c="k", capsize=6, elinewidth=1.5, markeredgewidth=1.5, zorder=0) #plot the standard error

df[df["IPA_molefrac"] == 0.0].plot.scatter("IPA_molefrac", "EP_generation_rate", ax=ax[0, 4], label="0% IPA",s=250, c="b", edgecolor="k") #plot the 0% IPA data
df[df["IPA_molefrac"] == 0.1].plot.scatter("IPA_molefrac", "EP_generation_rate", ax=ax[0, 4], label="10% IPA",s=250, c="#58a8f9", edgecolor="k") #plot the 10% IPA data
df[df["IPA_molefrac"] == 0.2].plot.scatter("IPA_molefrac", "EP_generation_rate", ax=ax[0, 4], label="20% IPA",s=250, c="g",edgecolor="k") #plot the 20% IPA data
ax[0, 4].annotate("Pd\n2000 mM potassium formate", (0.02, 0.89), xycoords="axes fraction", fontsize=24, fontweight="bold") #add the catalyst label

df= DF.query("catalyst == 'Pt' & temperature_C == 75 & formate_mM == 10 & stock_batch_number >= 0") #filter the data
ax[1, 0].errorbar(df.IPA_molefrac, df.EP_generation_rate, yerr=df.EP_generation_rate_std_err, c="k", capsize=6, elinewidth=1.5, markeredgewidth=1.5, zorder=0) #plot the standard error

df[df["IPA_molefrac"] == 0.0].plot.scatter("IPA_molefrac", "EP_generation_rate", ax=ax[1, 0], label="0% IPA",s=250, c="b", edgecolor="k") #plot the 0% IPA data
df[df["IPA_molefrac"] == 0.1].plot.scatter("IPA_molefrac", "EP_generation_rate", ax=ax[1, 0], label="10% IPA",s=250, c="#58a8f9", edgecolor="k") #plot the 10% IPA data
df[df["IPA_molefrac"] == 0.2].plot.scatter("IPA_molefrac", "EP_generation_rate", ax=ax[1, 0], label="20% IPA",s=250, c="g",edgecolor="k") #plot the 20% IPA data
ax[1,0].annotate("Pt\n10 mM potassium formate", (0.02, 0.89), xycoords="axes fraction", fontsize=24, fontweight="bold") #add the catalyst label


df= DF.query("catalyst == 'Pt' & temperature_C == 75 & formate_mM == 100 & stock_batch_number >= 0") #filter the data
ax[1, 1].errorbar(df.IPA_molefrac, df.EP_generation_rate, yerr=df.EP_generation_rate_std_err, c="k", capsize=6, elinewidth=1.5, markeredgewidth=1.5, zorder=0) #plot the standard error

df[df["IPA_molefrac"] == 0.0].plot.scatter("IPA_molefrac", "EP_generation_rate", ax=ax[1, 1], label="0% IPA",s=250, c="b", edgecolor="k") #plot the 0% IPA data
df[df["IPA_molefrac"] == 0.1].plot.scatter("IPA_molefrac", "EP_generation_rate", ax=ax[1, 1], label="10% IPA",s=250, c="#58a8f9", edgecolor="k") #plot the 10% IPA data
df[df["IPA_molefrac"] == 0.2].plot.scatter("IPA_molefrac", "EP_generation_rate", ax=ax[1, 1], label="20% IPA",s=250, c="g",edgecolor="k") #plot the 20% IPA data
ax[1,1].annotate("Pt\n100 mM potassium formate", (0.02, 0.89), xycoords="axes fraction", fontsize=24, fontweight="bold") #add the catalyst label

df= DF.query("catalyst == 'Pt' & temperature_C == 75 & formate_mM == 500 & stock_batch_number >= 0") #filter the data
ax[1, 2].errorbar(df.IPA_molefrac, df.EP_generation_rate, yerr=df.EP_generation_rate_std_err, c="k", capsize=6, elinewidth=1.5, markeredgewidth=1.5, zorder=0) #plot the standard error

df[df["IPA_molefrac"] == 0.0].plot.scatter("IPA_molefrac", "EP_generation_rate", ax=ax[1, 2], label="0% IPA",s=250, c="b", edgecolor="k") #plot the 0% IPA data
df[df["IPA_molefrac"] == 0.1].plot.scatter("IPA_molefrac", "EP_generation_rate", ax=ax[1, 2], label="10% IPA",s=250, c="#58a8f9", edgecolor="k") #plot the 10% IPA data
df[df["IPA_molefrac"] == 0.2].plot.scatter("IPA_molefrac", "EP_generation_rate", ax=ax[1, 2], label="20% IPA",s=250, c="g",edgecolor="k") #plot the 20% IPA data
ax[1, 2].annotate("Pt\n500 mM potassium formate", (0.02, 0.89), xycoords="axes fraction", fontsize=24, fontweight="bold") #add the catalyst label

df= DF.query("catalyst == 'Pt' & temperature_C == 75 & formate_mM == 1000 & stock_batch_number >= 0") #filter the data
ax[1, 3].errorbar(df.IPA_molefrac, df.EP_generation_rate, yerr=df.EP_generation_rate_std_err, c="k", capsize=6, elinewidth=1.5, markeredgewidth=1.5, zorder=0) #plot the standard error

df[df["IPA_molefrac"] == 0.0].plot.scatter("IPA_molefrac", "EP_generation_rate", ax=ax[1, 3], label="0% IPA",s=250, c="b", edgecolor="k") #plot the 0% IPA data
df[df["IPA_molefrac"] == 0.1].plot.scatter("IPA_molefrac", "EP_generation_rate", ax=ax[1, 3], label="10% IPA",s=250, c="#58a8f9", edgecolor="k") #plot the 10% IPA data
df[df["IPA_molefrac"] == 0.2].plot.scatter("IPA_molefrac", "EP_generation_rate", ax=ax[1, 3], label="20% IPA",s=250, c="g",edgecolor="k") #plot the 20% IPA data
ax[1,3].annotate("Pt\n1000 mM potassium formate", (0.02, 0.89), xycoords="axes fraction", fontsize=24, fontweight="bold") #add the catalyst label

for row in ax:
    for axi in row:
        axi.set_xlabel("IPA Concentration (mole/mole)", labelpad=5, fontsize=26) #add x axis label
        axi.set_ylabel("Ethylphenol Generation Rate (mM/g s)", labelpad=5, fontsize=26) #add y axis label
        axi.set_xticks([0, 0.1, 0.2]) #set x axis tick marks
        axi.set_xticklabels(["0", "0.1", "0.2"], fontsize=22) #set x axis tick labels
        axi.set_xlim(-0.05, 0.25) #set the x axis limits
        axi.set_ylim(-0.3, 20) #set the y axis limits
        axi.legend().set_visible(False) #hide the legend
plt.savefig("ethylphenol_generation_vs_IPA_concentration_all_900dpi.png", bbox_inches="tight", dpi=100) #save the figure as a 900 dpi .png
print('figure saved to "ethylphenol_generation_vs_IPA_concentration_all_900dpi.png"') #print success message
print("DPI actually 200 - fix this ")