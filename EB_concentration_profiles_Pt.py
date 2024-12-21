import pandas as pd
import matplotlib.pyplot as plt
from set_fig_prefs import set_fig_prefs
set_fig_prefs()

DF = pd.read_csv(r"vinylphenol transfer hydrogenation(data).csv", skiprows=[1,2], encoding = "latin") #import the data
DF = DF[(DF["temperature_C"] == 75) & (DF['time_min'] <=30) & (DF.catalyst == "Pt")] #filter for temperature = 75 °C and Pt catalyst and time <= 30 min

index = 1 #select formate concentration
df = DF[(DF["formate_mM"] == index)] #select formate concentration
df0 = df[df["IPA_molefrac"] == 0.0] #select [IPA] = 0%
df1 = df[df["IPA_molefrac"] == 0.1] #select [IPA] = 10%
df2 = df[df["IPA_molefrac"] == 0.2] #select [IPA] = 20%

index = 10 #select formate concentration
df = DF[(DF["formate_mM"] == index)] #select formate concentration
df3 = df[df["IPA_molefrac"] == 0.0] #select [IPA] = 0%
df4 = df[df["IPA_molefrac"] == 0.1] #select [IPA] = 10%
df5 = df[df["IPA_molefrac"] == 0.2] #select [IPA] = 20%

index = 100 #select formate concentration
df = DF[(DF["formate_mM"] == index)] #select formate concentration
df6 = df[df["IPA_molefrac"] == 0.0] #select [IPA] = 0%
df7 = df[df["IPA_molefrac"] == 0.1] #select [IPA] = 10%
df8 = df[df["IPA_molefrac"] == 0.2] #select [IPA] = 20%

index = 1000 #select formate concentration
df = DF[(DF["formate_mM"] == index)] #select formate concentration
df9 = df[df["IPA_molefrac"] == 0.0] #select [IPA] = 0%
df10 = df[df["IPA_molefrac"] == 0.1] #select [IPA] = 10%
df11 = df[df["IPA_molefrac"] == 0.2] #select [IPA] = 20%


fig, ax1 = plt.subplots(1,4, figsize=(20,4.5), dpi = 70) #initialize figure
ax1[0].scatter(df0["time_min"], df0["ethylphenol_mM"], s=20, c="darkgreen") #select [IPA] = 0%
ax1[0].scatter(df1["time_min"], df1["ethylphenol_mM"], s=20, c="darkblue") #select [IPA] = 10%
ax1[0].scatter(df2["time_min"], df2["ethylphenol_mM"], s=20, c="crimson") #select [IPA] = 20%
ax1[0].text(20, 17.5, "Pt\n1 mM formate")

ax1[1].scatter(df3["time_min"], df3["ethylphenol_mM"], s=20, c="darkgreen") #select [IPA] = 0%
ax1[1].scatter(df4["time_min"], df4["ethylphenol_mM"], s=20, c="darkblue") #select [IPA] = 10%
ax1[1].scatter(df5["time_min"], df5["ethylphenol_mM"], s=20, c="crimson") #select [IPA] = 20%
ax1[1].text(19, 17.5, "Pt\n10 mM formate")

ax1[2].scatter(df6["time_min"], df6["ethylphenol_mM"], s=20, c="darkgreen") #select [IPA] = 0%
ax1[2].scatter(df7["time_min"], df7["ethylphenol_mM"], s=20, c="darkblue") #select [IPA] = 10%
ax1[2].scatter(df8["time_min"], df8["ethylphenol_mM"], s=20, c="crimson") #select [IPA] = 20%
ax1[2].text(18, 17.5, "Pt\n100 mM formate")

ax1[3].scatter(df9["time_min"], df9["ethylphenol_mM"], s=20, c="darkgreen") #select [IPA] = 0%
ax1[3].scatter(df10["time_min"], df10["ethylphenol_mM"], s=20, c="darkblue") #select [IPA] = 10%
ax1[3].scatter(df11["time_min"], df11["ethylphenol_mM"], s=20, c="crimson") #select [IPA] = 20%
ax1[3].text(17, 17.5, "Pt\n1000 mM formate")

for ax1 in ax1:
    ax1.set_xlabel("Time (min)")
    ax1.set_ylabel("Ethylphenol Concentration (mM)")
    ax1.legend(("0 mol% IPA", "10 mol% IPA", "20 mol% IPA"), loc="upper left")  #add legend
    ax1.set_ylim((0, 20))
    ax1.set_xlim((-1.5, 31.5))

plt.tight_layout()
plt.show()
print("done")