"""TODO

Add the labels "Pt" and "N mM formate" to the Pt plots """
import pandas as pd
import matplotlib.pyplot as plt
from set_fig_prefs import set_fig_prefs
set_fig_prefs()

DF = pd.read_csv(r"vinylphenol transfer hydrogenation(Pt_Data).csv", skiprows=2, encoding = "latin") #import the data

df = DF[(DF["temperature [° C]"] == 75) & (DF['time [min]'] <=30)] #filter for temperature = 75 °C 

index = 1 #select formate concentration
df = DF[(DF["[formate] [mM]"] == index)] #select formate concentration
df0 = df[df["[IPA] [mol/mol]"] == 0.0] #select [IPA] = 0%
df1 = df[df["[IPA] [mol/mol]"] == 0.1] #select [IPA] = 10%
df2 = df[df["[IPA] [mol/mol]"] == 0.2] #select [IPA] = 20%

index = 10 #select formate concentration
df = DF[(DF["[formate] [mM]"] == index)] #select formate concentration
df3 = df[df["[IPA] [mol/mol]"] == 0.0] #select [IPA] = 0%
df4 = df[df["[IPA] [mol/mol]"] == 0.1] #select [IPA] = 10%
df5 = df[df["[IPA] [mol/mol]"] == 0.2] #select [IPA] = 20%

index = 100 #select formate concentration
df = DF[(DF["[formate] [mM]"] == index)] #select formate concentration
df6 = df[df["[IPA] [mol/mol]"] == 0.0] #select [IPA] = 0%
df7 = df[df["[IPA] [mol/mol]"] == 0.1] #select [IPA] = 10%
df8 = df[df["[IPA] [mol/mol]"] == 0.2] #select [IPA] = 20%

index = 1000 #select formate concentration
df = DF[(DF["[formate] [mM]"] == index)] #select formate concentration
df9 = df[df["[IPA] [mol/mol]"] == 0.0] #select [IPA] = 0%
df10 = df[df["[IPA] [mol/mol]"] == 0.1] #select [IPA] = 10%
df11 = df[df["[IPA] [mol/mol]"] == 0.2] #select [IPA] = 20%


fig, ax1 = plt.subplots(1,4, figsize=(20,4.5), dpi = 70) #initialize figure
ax1[0].scatter(df0["time [min]"], df0["[ethylphenol] [mM]"], s=20, c="k") #select [IPA] = 20%
ax1[0].scatter(df1["time [min]"], df1["[ethylphenol] [mM]"], s=20, c="b") #select [IPA] = 20%
ax1[0].scatter(df2["time [min]"], df2["[ethylphenol] [mM]"], s=20, c="r") #select [IPA] = 20%
ax1[0].text(20, 17.5, "Pt\n1 mM formate")

ax1[1].scatter(df3["time [min]"], df3["[ethylphenol] [mM]"], s=20, c="k") #select [IPA] = 20%
ax1[1].scatter(df4["time [min]"], df4["[ethylphenol] [mM]"], s=20, c="b") #select [IPA] = 20%
ax1[1].scatter(df5["time [min]"], df5["[ethylphenol] [mM]"], s=20, c="r") #select [IPA] = 20%
ax1[1].text(19, 17.5, "Pt\n10 mM formate")

ax1[2].scatter(df6["time [min]"], df6["[ethylphenol] [mM]"], s=20, c="k") #select [IPA] = 20%
ax1[2].scatter(df7["time [min]"], df7["[ethylphenol] [mM]"], s=20, c="b") #select [IPA] = 20%
ax1[2].scatter(df8["time [min]"], df8["[ethylphenol] [mM]"], s=20, c="r") #select [IPA] = 20%
ax1[2].text(18, 17.5, "Pt\n100 mM formate")

ax1[3].scatter(df9["time [min]"], df9["[ethylphenol] [mM]"], s=20, c="k") #select [IPA] = 20%
ax1[3].scatter(df10["time [min]"], df10["[ethylphenol] [mM]"], s=20, c="b") #select [IPA] = 20%
ax1[3].scatter(df11["time [min]"], df11["[ethylphenol] [mM]"], s=20, c="r") #select [IPA] = 20%
ax1[3].text(17, 17.5, "Pt\n1000 mM formate")

for ax1 in ax1:
    ax1.set_xlabel("Time (min)")
    ax1.set_ylabel("Ethylphenol Concentration (mM)")
    ax1.legend(("0 mol% IPA", "10 mol% IPA", "20 mol% IPA"), loc="upper left")  #add legend
    ax1.set_ylim((0, 20))
    ax1.set_xlim((-1.5, 31.5))

plt.tight_layout()
plt.show()