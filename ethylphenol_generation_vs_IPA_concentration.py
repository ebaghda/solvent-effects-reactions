import pandas as pd
import matplotlib.pyplot as plt
plt.style.use("./style/simple_bold.mplstyle") #set plot style

fig, ax = plt.subplots(figsize=(8, 8)) #create a figure and axis

DF = pd.read_parquet(r"vinylphenol transfer hydrogenation(data).parquet") #import the data
df = DF[(DF["catalyst"] == "Pd") & (DF["temperature_C"] == 75) & (DF["formate_mM"] == 100) & (DF["stock_batch_number"] >= 0)] #filter the data

plt.errorbar(df[df["IPA_molefrac"] >= 0.0]["IPA_molefrac"], df[df["IPA_molefrac"] >= 0.0]["EP_generation_rate"], yerr=df[df["IPA_molefrac"] >= 0.0]["EP_generation_rate_std_err"], c="k", capsize=4, linewidth=1, zorder=0)

df[df["IPA_molefrac"] == 0.0].plot.scatter("IPA_molefrac", "EP_generation_rate", ax=ax, label="0% IPA",s=30, c="b")
df[df["IPA_molefrac"] == 0.1].plot.scatter("IPA_molefrac", "EP_generation_rate", ax=ax, label="10% IPA",s=30, c="#58a8f9")
df[df["IPA_molefrac"] == 0.2].plot.scatter("IPA_molefrac", "EP_generation_rate", ax=ax, label="20% IPA",s=30, c="g")

plt.xlabel("IPA Concentration (mole/mole)")
plt.ylabel("Ethylphenol Generation Rate (mM/g s)")
ax.set_xticks([0, 0.1, 0.2])
ax.set_ylim(-0.1, 1.1)
ax.set_yticks([0, 0.2, 0.4, 0.6, 0.8, 1.0])
ax.legend().set_visible(False) #hide the legend
plt.savefig("ethylphenol_generation_vs_IPA_concentration_900dpi.png", bbox_inches="tight", dpi=900)
print('figure saved to "ethylphenol_generation_vs_IPA_concentration_900dpi.png"')