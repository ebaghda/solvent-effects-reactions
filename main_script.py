'''
Main sript is intended to be the only function called for the project to run 
Main script is organized in the following mannner:
0. Initalization: jset figure resultion, clean up unnecessary files
1. data import, data cleaning, and write to parqet file for later read/write 
2. Visualize ethylphenol concentration profiles
3. Perform first-order fitting, write results to dataframe, and visualize fits
4. Perform linear fitting, write results to dataframs, and visualize fits
'''
### ---------- 0: INITIALIZATION ----------
## User-defined parameters for figure resolution (lower dpi is faster code completion):
single_axis_dpi = 600 #set figure resolution for all single axis figures - use 900 for publication-quality
panel_dpi = 400 #set figure resolution for all panel figures (keep lower) - use 400(?) for publicaiton-quality

#delete png and parquet files in current folder - this prevents multiple files from accumulating upon dpi changes or figure re-naming
import os
for file in os.listdir():
    if file.endswith(".png") or file.endswith(".parquet"):
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

### 1. --------------- DATA IMPORT AND CLEANING ---------------
## IMPORT DATA & CONVERT TO PARQUET
from csv_to_parquet import csv_to_parquet
csv_to_parquet("vinylphenol transfer hydrogenation(data).csv")

### 2. --------------- PLOT ETHYLPHENOL CONCENTRAION PROFILES ---------------

## PLOT EP CONCENTRATION VS TIME FOR EACH CATALYST
from ethylphenol_concentration_profiles import plot_ethylphenol_concentration_profiles
for catalyst in ["Pd", "Pt"]:
    plot_ethylphenol_concentration_profiles(filepath=r"vinylphenol transfer hydrogenation(data).parquet", rxn_temperature=75, catalyst=catalyst, formate_concentrations=[], dpi=panel_dpi) #run script

### 3. --------------- PERFORM LINEAR FITTING ---------------
## PERFORM LINEAR FITTING FOR REACTION RATES
from linear_fit_inplace import linear_fit_all_and_rewrite_in_dataframe
linear_fit_all_and_rewrite_in_dataframe()

## PLOT CONCETRATION PROFILES WITH FITS
#plot linear fit
from rate_fitting import plot_fitting_results
plot_fitting_results(r"vinylphenol transfer hydrogenation(data).parquet", dpi = panel_dpi, catalyst="Pd", vertical_layout=False)
plot_fitting_results(r"vinylphenol transfer hydrogenation(data).parquet", dpi = panel_dpi, catalyst="Pt", vertical_layout=False)

## PLOT LINEAR EP GENERATION RATE VS FORMATE CONCENTRATION
#plot initial reaction rate versus formate concentration
from ethylphenol_generation_vs_formate_concentration import plot_ethylphenol_generation_rate_vs_formate_concentration
plot_ethylphenol_generation_rate_vs_formate_concentration(dpi=single_axis_dpi) #run script
#plot mean initial reaction rate vs formate concentration
from mean_ethylphenol_generation_rate_vs_formate_concentration import plot_mean_ethylphenol_generation_vs_formate_concentration
plot_mean_ethylphenol_generation_vs_formate_concentration()

## PLOT EP GENERATION RATE VS IPA CONCENTRATION PANEL
from ethylphenol_generation_vs_IPA_concentration_panel import plot_ethylphenol_generation_rate_vs_IPA_concentration_panel
for catalyst in ["Pd", "Pt"]:
    plot_ethylphenol_generation_rate_vs_IPA_concentration_panel(filepath=r"vinylphenol transfer hydrogenation(data)_fitted.parquet", catalyst = catalyst,formate_concentrations=[], dpi=panel_dpi) #run script

#
from ethylphenol_generation_vs_IPA_concentration import plot_ethylphenol_generation_rate_vs_IPA_concentration_for_all_concentrations
plot_ethylphenol_generation_rate_vs_IPA_concentration_for_all_concentrations(filepath=r"vinylphenol transfer hydrogenation(data)_fitted.parquet", dpi=single_axis_dpi) #run script




### 4. --------------- PERFORM FIRST-ORDER FITTING ---------------

## PERFORM FIRST ORDER FITTING FOR RATE CONSTANTS
from first_order_fit_inplace import fit_all_and_rewrite_in_dataframe
fit_all_and_rewrite_in_dataframe()

#plot first order fit over concentration profiles
from first_order_fit import first_order_fit_ethylphenol_concentration_profiles
first_order_fit_ethylphenol_concentration_profiles()

#plot first-order rate constant versus formate concentration
from first_order_rate_constant_vs_formate_concentration import plot_rate_constant_vs_formate_concentration
plot_rate_constant_vs_formate_concentration(r"vinylphenol transfer hydrogenation(data)_fitted.parquet", "Pd")

#TODO: wrap function in function to generate  panel
print("need to wrap first order fits to get panel")

print("Completed running main_script.py")