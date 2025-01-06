import pandas as pd
import matplotlib.pyplot as plt
plt.style.use("./style/simple_bold.mplstyle") #select stylesheet

def plot_ethylphenol_generation_rate_vs_formate_concentration(dpi: int) -> None: #define the main function
    for catalyst in ["Pd","Pt"]:
        filepath: str = f"./{catalyst}_fitting_results.parquet"
        df = pd.read_parquet(filepath) #import fitted concentration profile data
        print(df.head())

        fig, ax = plt.subplots(figsize=(5,5)) #initialize figure
        plt.errorbar(df.query("IPA_molefrac == 0")["formate_mM"], df.query("IPA_molefrac == 0")["mass_activity"], yerr=df.query("IPA_molefrac == 0")["mass_activity_stderr"], fmt="", c='black', capsize=4, linewidth=1, zorder=0, marker="o", ls='none', markerfacecolor = 'b') #plot the standard error of each fit
        plt.errorbar(df.query("IPA_molefrac == 0.1")["formate_mM"], df.query("IPA_molefrac == 0.1")["mass_activity"], yerr=df.query("IPA_molefrac == 0.1")["mass_activity_stderr"], fmt="", c='black', capsize=4, linewidth=1, zorder=0, marker="^", ls='none', markerfacecolor = '#58a8f9') #plot the standard error of each fit
        plt.errorbar(df.query("IPA_molefrac == 0.2")["formate_mM"], df.query("IPA_molefrac == 0.2")["mass_activity"], yerr=df.query("IPA_molefrac == 0.2")["mass_activity_stderr"], fmt="", c='black', capsize=4, linewidth=1, zorder=0, marker="s", ls='none', markerfacecolor = 'g') #plot the standard error of each fit
        ax.legend(["0 mol% IPA", "10 mol% IPA", "20 mol% IPA"])
        plt.ylabel("Ethylphenol Generation Rate (mM/g min)") #set the ylabel
        plt.xlabel("Formate Concentration (mM)") #set the xlabel
        ax.set_xscale('log') # select the x scaling 
        ax.set_yscale('linear') #set the y scaling 
        fig.savefig(f"ethylphenol_generation_vs_formate_concentration_{catalyst}_{dpi}dpi.png", dpi=dpi, bbox_inches='tight') #export the figure as a 900 dpi .png
        print(f"saved figure as \"ethylphenol_generation_vs_formate_concentration_{catalyst}_{dpi}dpi.png\"") #print success message

if __name__ == "__main__": #run script if it is called directly
    plot_ethylphenol_generation_rate_vs_formate_concentration(dpi=400) #run script