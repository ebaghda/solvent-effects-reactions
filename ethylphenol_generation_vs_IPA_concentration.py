import pandas as pd
import matplotlib.pyplot as plt

plt.style.use("./style/simple_bold.mplstyle") #set plot style

def load_and_filter_data(filepath: str) -> pd.DataFrame: #define a function to load and filter the data
    df = pd.read_parquet(filepath) #import the data
    df = df.query("temperature_C == 75 & time_min == 0 & stock_batch_number >= 0") #filter the data
    return df #return the filtered data

def plot_ethylphenol_generation_rate_vs_IPA_concentration_single_formate_concentration(filepath: str, formate_concentration: float, dpi: int) -> None: #define the main function
    
    DF = load_and_filter_data(filepath) #load and filter data

    for catalyst in DF["catalyst"].unique(): #loop over all catalyst
        fig, ax = plt.subplots(figsize=(5, 5)) #initialize figure

        legend = plt.legend(["0% IPA", "10% IPA", "20% IPA"], loc="upper left") #add a legend
        legend.set_visible(False) #hide the 
        
        df = DF.query("catalyst == @catalyst & formate_mM == @formate_concentration") #filter the data for the formate concentration
        if df.empty:
            print(f"no data found for catalyst = {catalyst} and formate concentration = {formate_concentration}")
            continue
        plt.errorbar(df[df["IPA_molefrac"] == 0.0]["IPA_molefrac"], df[df["IPA_molefrac"] == 0.0]["mass_activity"], yerr=df[df["IPA_molefrac"] == 0.0]["mass_activity_SE"], c="k", capsize=4, linewidth=1, marker='o', markerfacecolor='darkblue', ls='none') #plot 00% IPA data
        plt.errorbar(df[df["IPA_molefrac"] == 0.1]["IPA_molefrac"], df[df["IPA_molefrac"] == 0.1]["mass_activity"], yerr=df[df["IPA_molefrac"] == 0.1]["mass_activity_SE"], c="k", capsize=4, linewidth=1,marker='^', markerfacecolor='#58a8f9', ls='none') #plot 10% IPA data
        plt.errorbar(df[df["IPA_molefrac"] == 0.2]["IPA_molefrac"], df[df["IPA_molefrac"] == 0.2]["mass_activity"], yerr=df[df["IPA_molefrac"] == 0.2]["mass_activity_SE"], c="k", capsize=4, linewidth=1,marker='s', markerfacecolor='darkgreen', ls='none') #plot 20% IPA data
        
        plt.annotate(f"{catalyst}\n{formate_concentration} mM potassium formate", (0.02, 0.88), xycoords="axes fraction", fontweight="bold") #add the catalyst label
        if formate_concentration == 4000:
            ax.set_ylim(None, 14)
        if formate_concentration == 2000:
            ax.set_ylim(None, 26)
        if formate_concentration == 1000:
            ax.set_ylim(None, 32.5)
        if formate_concentration == 500:
            ax.set_ylim(None, 26)
        if formate_concentration == 100:
            ax.set_ylim(None, 0.65)
            
            

        plt.xlabel("IPA Concentration (mole/mole)", labelpad=15) #add x axis label
        plt.ylabel("Ethylphenol Generation Rate (mM/g min)", labelpad=15) #add y axis label
        ax.set_xticks([0, 0.1, 0.2]) #set x axis tick marks
        ax.set_xticklabels(["0", "0.1", "0.2"]) #set x axis tick labels

        plt.savefig(f"./linear-EP-gen-vs-IPA-conc-individual/ethylphenol_generation_vs_IPA_concentration_{catalyst}_{formate_concentration}mMPF_{dpi}dpi.png", bbox_inches="tight", dpi=900) #save the figure as a 900 dpi .png
        print(f'figure saved to "ethylphenol_generation_vs_IPA_concentration_{catalyst}_{formate_concentration}mMPF_{dpi}dpi.png"') #print success message


def plot_ethylphenol_generation_rate_vs_IPA_concentration_for_all_concentrations(filepath: str, dpi: int) -> None: #define a function to plot EP generation rate vs IPA concentration for all formate concentrations
    DF = load_and_filter_data(filepath) #load and filter data
    for formate_concentration in DF["formate_mM"].unique():
        plot_ethylphenol_generation_rate_vs_IPA_concentration_single_formate_concentration(filepath, formate_concentration, dpi)

        '''
        try:
            plot_ethylphenol_generation_rate_vs_IPA_concentration_single_formate_concentration(filepath, formate_concentration, dpi)
        except:
            print(f"Error plotting {formate_concentration} mM formate")
            '''
    print("All figures saved to \"linear-EP-gen-vs-IPA-conc-individual\" folder") #print success message

if __name__ == "__main__": #run script if it is called directly
    plot_ethylphenol_generation_rate_vs_IPA_concentration_for_all_concentrations(filepath=r"vinylphenol transfer hydrogenation(data)_fitted.parquet", dpi=900) #run script
