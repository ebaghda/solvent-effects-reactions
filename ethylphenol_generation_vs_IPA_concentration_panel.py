import pandas as pd
import matplotlib.pyplot as plt

plt.style.use("./style/simple_bold.mplstyle") #set plot style

def load_and_filter_data(filepath: str, catalyst: str) -> pd.DataFrame: #define a function to load and filter the data
    DF = pd.read_parquet(filepath) #import the data
    df = DF.query("catalyst == @catalyst & temperature_C == 75 & time_min == 0") #filter the data
    return df #return the filtered data

def plot_ethylphenol_generation_rate_vs_IPA_concentration_panel(filepath: str, catalyst: str, formate_concentrations: list[float], dpi: int) -> None: #define the main function
    DF = load_and_filter_data(filepath, catalyst) #load and filter data

    if not formate_concentrations: #if formate_concentrations is empty
        formate_concentrations = sorted(DF.formate_mM.unique()) #get unique formate concentrations
   
    fig, ax = plt.subplots(1,len(formate_concentrations), figsize=(5*len(formate_concentrations),5)) #initialize figure
    
    for i in range(len(formate_concentrations)): #for each formate concentration
        formate_concentration = formate_concentrations[i] #get the current formate concentration
        df = DF.query("formate_mM == @formate_concentration") #filter the data for the current formate concentration

        legend = ax[1].legend(["0% IPA", "10% IPA", "20% IPA"], loc="upper left") #add the legend
        legend.set_visible(False) #hide the legend

        ax[i].errorbar(df.query("IPA_molefrac == 0")["IPA_molefrac"], df.query("IPA_molefrac == 0")["mass_activity"], yerr=df.query("IPA_molefrac == 0")["mass_activity_SE"], fmt="", c='black', capsize=4, linewidth=1, zorder=0, marker="o", ls='none', markerfacecolor = 'darkblue') #plot the 00% IPA data
        ax[i].errorbar(df.query("IPA_molefrac == 0.1")["IPA_molefrac"], df.query("IPA_molefrac == 0.1")["mass_activity"], yerr=df.query("IPA_molefrac == 0.1")["mass_activity_SE"], fmt="", c='black', capsize=4, linewidth=1, zorder=0, marker="^", ls='none', markerfacecolor = '#58a8f9') #plot 10% IPA data
        ax[i].errorbar(df.query("IPA_molefrac == 0.2")["IPA_molefrac"], df.query("IPA_molefrac == 0.2")["mass_activity"], yerr=df.query("IPA_molefrac == 0.2")["mass_activity_SE"], fmt="", c='black', capsize=4, linewidth=1, zorder=0, marker="s", ls='none', markerfacecolor = 'darkgreen') #plot 20% IPA data
        
        ax[i].annotate(f"{catalyst}\n{formate_concentration} mM potassium formate", (0.02, 0.89), xycoords="axes fraction", fontweight="bold") #add the catalyst label
        
        ax[i].set_xlabel("IPA Concentration (mole/mole)", labelpad=5) #add x axis label
        ax[i].set_ylabel("Ethylphenol Generation Rate (mM/g min)", labelpad=5) #add y axis label
        ax[i].set_xticks([0, 0.1, 0.2]) #set x axis tick marks
        ax[i].set_xticklabels(["0", "0.1", "0.2"]) #set x axis tick labels
        ax[i].set_xlim(-0.05, 0.25) #set the x axis limits
        ax[i].set_ylim(-0.3, 27) #set the y axis limits
        
    plt.tight_layout() #correct the layout
    fig.savefig(f"ethylphenol_generation_vs_IPA_concentration_panel_{catalyst}_{dpi}dpi.png", bbox_inches="tight", dpi=dpi) #save the figure as a 900 dpi .png
    print(f'figure saved to "ethylphenol_generation_vs_IPA_concentration_panel_{catalyst}_{dpi}dpi.png"') #print success message

if __name__ == "__main__": #run script if it is called directly
    plot_ethylphenol_generation_rate_vs_IPA_concentration_panel(filepath=r"vinylphenol transfer hydrogenation(data)_fitted.parquet", catalyst = 'Pd',formate_concentrations=[], dpi=250) #run script