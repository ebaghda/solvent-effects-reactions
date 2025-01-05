import pandas as pd
import matplotlib.pyplot as plt

#delete png files in current folder
import os
for file in os.listdir():
    if file.endswith(".png"):
        os.remove(file) 

#delete png files in EP-gen-vs-IPA-conc-individual folder
for file in os.listdir(r"./EP-gen-vs-IPA-conc-individual"):
    if file.endswith(".png"):
        os.remove(f"./EP-gen-vs-IPA-conc-individual/{file}") 

## IMPORT DATA & CONVERT TO PARQUET
from csv_to_parquet import csv_to_parquet
csv_to_parquet("vinylphenol transfer hydrogenation(data).csv")
DF = pd.read_parquet("vinylphenol transfer hydrogenation(data).parquet")

## FILTER DATA FOR EXTRANEOUS REACTIONS -- this is not used later...
# DF = DF.query("temperature_C == 75 & time_min <= 30 & formate_mM > 1 & (rxn_label != 101) | (rxn_label != 102) | (rxn_label != 103)")

## PERFORM FITTING FOR REACTIONS RATES
#TODO: Add fitting code here

## GENERATE FIGURES

# PLOT EP CONCENTRATION VS TIME FOR EACH CATALYST
from ethylphenol_concentration_profiles import plot_ethylphenol_concentration_profiles
for catalyst in DF.catalyst.unique():
    plot_ethylphenol_concentration_profiles(filepath=r"vinylphenol transfer hydrogenation(data).parquet", rxn_temperature=75, catalyst=catalyst, formate_concentrations=[], dpi=200) #run script

# PLOT EP GENERATION RATE VS FORMATE CONCENTRATION
from ethylphenol_generation_vs_formate_concentration import plot_ethylphenol_generation_rate_vs_formate_concentration
for catalyst in DF.catalyst.unique():
    plot_ethylphenol_generation_rate_vs_formate_concentration(filepath=r"vinylphenol transfer hydrogenation(data).parquet", catalyst=catalyst, dpi=900) #run script

# PLOT EP GENERATION RATE VS IPA CONCENTRATION PANEL
from ethylphenol_generation_vs_IPA_concentration_panel import plot_ethylphenol_generation_rate_vs_IPA_concentration_panel
for catalyst in DF.catalyst.unique():
    plot_ethylphenol_generation_rate_vs_IPA_concentration_panel(filepath=r"vinylphenol transfer hydrogenation(data).parquet", catalyst = catalyst,formate_concentrations=[], dpi=300) #run script


from ethylphenol_generation_vs_IPA_concentration import plot_ethylphenol_generation_rate_vs_IPA_concentration_for_all_concentrations
plot_ethylphenol_generation_rate_vs_IPA_concentration_for_all_concentrations(filepath=r"vinylphenol transfer hydrogenation(data).parquet", dpi=200) #run scriptPA_concentration_for_all_concentrations

print("Completed running main.py")