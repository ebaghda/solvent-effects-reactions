import pandas as pd
import matplotlib.pyplot as plt

plt.style.use("./style/simple_bold.mplstyle") #set plot style

#helper functions
def load_and_filter_data(filepath: str, rxn_temperature: float, catalyst: str) -> pd.DataFrame: #define a function to load and filter the data
    DF = pd.read_parquet(r"vinylphenol transfer hydrogenation(data).parquet") #import the data
    DF = DF[(DF["temperature_C"] == 75) & (DF.catalyst == catalyst)] #filter for temperature = 75 °C and Pd catalyst
    return DF #return the filtered data

def plot_concentration_profiles(df:pd.DataFrame, ax: plt.Axes, formate_mM: float, catalyst: str) -> None: #define a function to plot the concentration profiles
    for replicate in range(1,4): #loop over each replicate

        (ax.plot(
            df.query("IPA_molefrac == 0 & formate_mM == @formate_mM & replicate == @replicate")["time_min"], 
            df.query("IPA_molefrac == 0 & formate_mM == @formate_mM & replicate == @replicate")["ethylphenol_mM"], markerfacecolor="darkblue", markeredgecolor='k', marker="s", c="darkblue", ls=':', lw='1') #select [IPA] = 00%
         )

        (ax.plot(
            df.query("IPA_molefrac == 0.1 & formate_mM == @formate_mM & replicate == @replicate")["time_min"], 
            df.query("IPA_molefrac == 0.1 & formate_mM == @formate_mM & replicate == @replicate")["ethylphenol_mM"], markerfacecolor="#58a8f9", markeredgecolor='k', marker="^", c="#3898a9", ls=':', lw='1') #select [IPA] = 10%
        )
        (ax.plot(
            df.query("IPA_molefrac == 0.2 & formate_mM == @formate_mM & replicate == @replicate")["time_min"], 
            df.query("IPA_molefrac == 0.2 & formate_mM == @formate_mM & replicate == @replicate")["ethylphenol_mM"], markerfacecolor="darkgreen", markeredgecolor='k', marker="o", c="darkgreen", ls=':', lw='1') #select [IPA] = 20%
        )
    ax.annotate(f"{catalyst}\n{formate_mM} mM potassium formate", (0.02, 0.7), xycoords="axes fraction", fontweight="bold") #add the catalyst label to the plot

#main function
def plot_ethylphenol_concentration_profiles(filepath: str, rxn_temperature: float, catalyst: str, formate_concentrations: list[float], dpi: int) -> None: #define the main function

    DF = load_and_filter_data(filepath, rxn_temperature, catalyst) #load and filter data
    
    if not formate_concentrations: #if formate concentrations are not specified
        formate_concentrations = sorted(DF.formate_mM.unique()) #get unique formate concentrations
    
    fig, ax = plt.subplots(1,len(formate_concentrations), figsize=(5*len(formate_concentrations),5), dpi = 200) #initialize figure
    for i in range(len(formate_concentrations)): #loop over each formate concentration
        plot_concentration_profiles(DF, ax[i], formate_concentrations[i], catalyst) #plot concentration profiles

    for ax in ax: #loop over each axis object
        ax.set_xlabel("Time (min)") #set x label
        ax.set_ylabel("Ethylphenol Concentration (mM)") #set y label        
        ax.legend(("0 mol% IPA", "10 mol% IPA", "20 mol% IPA"), loc="upper left")  #add legend
        ax.set_ylim((0, 30)) #set the y axis limits
        ax.set_xlim((-1.5, 31.5)) #set x axis limits
    
    plt.tight_layout() #correct the layout
    fig.savefig(f"ethylphenol_concentration_profiles_{catalyst}_{dpi}dpi.png", dpi=dpi) #export png file
    print(f"figure saved to \"ethylphenol_concentration_profiles_{catalyst}_{dpi}dpi.png\"") #print success statement 

if __name__ == "__main__": #run script if it is called directly
    plot_ethylphenol_concentration_profiles(filepath=r"vinylphenol transfer hydrogenation(data).parquet", rxn_temperature=75, catalyst="Pd", formate_concentrations=[], dpi=200) #run script
