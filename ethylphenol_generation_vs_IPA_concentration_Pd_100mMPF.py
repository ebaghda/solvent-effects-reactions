import pandas as pd
import matplotlib.pyplot as plt
plt.style.use("./style/simple_bold.mplstyle") #set plot style

fig, ax = plt.subplots(figsize=(8, 8)) #create a figure and axis

DF = pd.read_parquet(r"vinylphenol transfer hydrogenation(data).parquet") #import the data
df = DF[(DF["catalyst"] == "Pd") & (DF["temperature_C"] == 75) & (DF["formate_mM"] == 100) & (DF["stock_batch_number"] >= 0)] #filter the data

plt.errorbar(df[df["IPA_molefrac"] >= 0.0]["IPA_molefrac"], df[df["IPA_molefrac"] >= 0.0]["EP_generation_rate"], yerr=df[df["IPA_molefrac"] >= 0.0]["EP_generation_rate_std_err"], c="k", capsize=4, linewidth=1, zorder=0) #plot the standard error

df[df["IPA_molefrac"] == 0.0].plot.scatter("IPA_molefrac", "EP_generation_rate", ax=ax, label="0% IPA",s=60, c="b", edgecolor="k") #plot the 0% IPA data
df[df["IPA_molefrac"] == 0.1].plot.scatter("IPA_molefrac", "EP_generation_rate", ax=ax, label="10% IPA",s=60, c="#58a8f9", edgecolor="k") #plot the 10% IPA data
df[df["IPA_molefrac"] == 0.2].plot.scatter("IPA_molefrac", "EP_generation_rate", ax=ax, label="20% IPA",s=60, c="g",edgecolor="k") #plot the 20% IPA data

plt.xlabel("IPA Concentration (mole/mole)", labelpad=15, fontsize=24) #add x axis label
plt.ylabel("Ethylphenol Generation Rate (mM/g s)", labelpad=15, fontsize=24) #add y axis label
ax.set_xticklabels(["0", "0.1", "0.2"], fontsize=20) #set x axis tick labels
ax.set_yticklabels(["0", "0.2", "0.4", "0.6", "0.8", "1.0"], fontsize=20) #set y axis tick labels
ax.set_xticks([0, 0.1, 0.2]) #set x axis tick marks
ax.set_ylim(-0.05, None) #set the y axis limits
# ax.set_yticks([0, 0.2, 0.4, 0.6, 0.8, 1.0]) #set the y axis tick marks
ax.legend().set_visible(False) #hide the legend
plt.annotate("Pd\n100 mM potassium formate", (0.02, 0.85), xycoords="axes fraction", fontsize=24, fontweight="bold") #add the catalyst label
plt.savefig("ethylphenol_generation_vs_IPA_concentration_Pd_100mMPF_900dpi.png", bbox_inches="tight", dpi=900) #save the figure as a 900 dpi .png
print('figure saved to "ethylphenol_generation_vs_IPA_concentration_Pd_100mMPF_900dpi.png"') #print success message