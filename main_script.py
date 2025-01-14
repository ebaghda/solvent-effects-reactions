import pandas as pd
import matplotlib.pyplot as plt

single_axis_dpi = 600 #set figure resolution for all single axis figures
panel_dpi = 200 #set figure resolution for all panel figures (keep lower)

#delete png files in current folder
import os
for file in os.listdir():
    if file.endswith(".png"):
        os.remove(file) 
def delete_pngs_in_subfolder(subfolder_name:str) -> None: #delete the png files in a specified subfolder
    for file in os.listdir(f"./{subfolder_name}"):
        if file.endswith(".png"):
            os.remove(f"./{subfolder_name}/{file}") 
            
#delete png files in subfolder: "linear-EP-gen-vs-IPA-conc-individual"
delete_pngs_in_subfolder("linear-EP-gen-vs-IPA-conc-individual")
#delete png files in subfolder: "fitted-concentration-profiles"
delete_pngs_in_subfolder("fitted-concentration-profiles")
delete_pngs_in_subfolder("fitted-concentration-profiles/linear")
delete_pngs_in_subfolder("fitted-concentration-profiles/first-order")

## IMPORT DATA & CONVERT TO PARQUET
from csv_to_parquet import csv_to_parquet
csv_to_parquet("vinylphenol transfer hydrogenation(data).csv")
DF = pd.read_parquet("vinylphenol transfer hydrogenation(data).parquet")

## PERFORM FITTING FOR REACTIONS RATES
#linear fit
from rate_fitting import plot_fitting_results
plot_fitting_results(r"vinylphenol transfer hydrogenation(data).parquet", dpi = panel_dpi, catalyst="Pd", vertical_layout=False)
plot_fitting_results(r"vinylphenol transfer hydrogenation(data).parquet", dpi = panel_dpi, catalyst="Pt", vertical_layout=False)

#first order fit
from first_order_fit import first_order_fit_ethylphenol_concentration_profiles_and_write_to_DataFrame
first_order_fit_ethylphenol_concentration_profiles_and_write_to_DataFrame()
#TODO: wrap function in function to genreate panel
print("need to wrap first order fits to get panel")

## GENERATE FIGURES

# PLOT EP CONCENTRATION VS TIME FOR EACH CATALYST
from ethylphenol_concentration_profiles import plot_ethylphenol_concentration_profiles
for catalyst in DF.catalyst.unique():
    plot_ethylphenol_concentration_profiles(filepath=r"vinylphenol transfer hydrogenation(data).parquet", rxn_temperature=75, catalyst=catalyst, formate_concentrations=[], dpi=panel_dpi) #run script

# PLOT EP GENERATION RATE VS FORMATE CONCENTRATION
from ethylphenol_generation_vs_formate_concentration import plot_ethylphenol_generation_rate_vs_formate_concentration
plot_ethylphenol_generation_rate_vs_formate_concentration(dpi=single_axis_dpi) #run script

# PLOT EP GENERATION RATE VS IPA CONCENTRATION PANEL
from ethylphenol_generation_vs_IPA_concentration_panel import plot_ethylphenol_generation_rate_vs_IPA_concentration_panel
for catalyst in DF.catalyst.unique():
    plot_ethylphenol_generation_rate_vs_IPA_concentration_panel(filepath=r"vinylphenol transfer hydrogenation(data).parquet", catalyst = catalyst,formate_concentrations=[], dpi=panel_dpi) #run script


from ethylphenol_generation_vs_IPA_concentration import plot_ethylphenol_generation_rate_vs_IPA_concentration_for_all_concentrations
plot_ethylphenol_generation_rate_vs_IPA_concentration_for_all_concentrations(filepath=r"vinylphenol transfer hydrogenation(data).parquet", dpi=single_axis_dpi) #run scriptPA_concentration_for_all_concentrations

print("Completed running main_script.py")