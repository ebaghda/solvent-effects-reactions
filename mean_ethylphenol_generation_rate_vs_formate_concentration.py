import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use("./style/simple_bold.mplstyle") #set plot style

def  plot_mean_ethylphenol_generation_vs_formate_concentration(catalyst: str = "Pd", dpi: int = 900, show_replicates: bool = False):
    from mean_linear_fit_results import aggregate_replicates
    df = aggregate_replicates()

    fig, ax = plt.subplots(figsize=(5,5)) #initialize figure
    # plot individual initial mass activities
    if show_replicates:
        plt.errorbar(df[(df["catalyst"] == catalyst)&(df["IPA_molefrac"] == 0)]["formate_mM"], df[(df["catalyst"] == catalyst)&(df["IPA_molefrac"] == 0)]["mass_activity"], yerr=df[(df["catalyst"] == catalyst)&(df["IPA_molefrac"] == 0)]["mass_activity_SE"], fmt="", c='gray', capsize=4, linewidth=1, zorder=0, marker="o", ls='none', markerfacecolor = 'gray')
    
        plt.errorbar(df[(df["catalyst"] == catalyst)&(df["IPA_molefrac"] == 0.1)]["formate_mM"], df[(df["catalyst"] == catalyst)&(df["IPA_molefrac"] == 0.1)]["mass_activity"], yerr=df[(df["catalyst"] == catalyst)&(df["IPA_molefrac"] == 0.1)]["mass_activity_SE"], fmt="", c='gray', capsize=4, linewidth=1, zorder=0, marker="^", ls='none', markerfacecolor = 'gray')

        plt.errorbar(df[(df["catalyst"] == catalyst)&(df["IPA_molefrac"] == 0.2)]["formate_mM"], df[(df["catalyst"] == catalyst)&(df["IPA_molefrac"] == 0.2)]["mass_activity"], yerr=df[(df["catalyst"] == catalyst)&(df["IPA_molefrac"] == 0.2)]["mass_activity_SE"], fmt="", c='gray', capsize=4, linewidth=1, zorder=0, marker="s", ls='none', markerfacecolor = 'gray')

    # plot the mean inital mass activities
    plt.errorbar(df[(df["catalyst"] == catalyst)&(df["IPA_molefrac"] == 0)]["formate_mM"], df[(df["catalyst"] == catalyst)&(df["IPA_molefrac"] == 0)]["mean_mass_activity"], yerr=df[(df["catalyst"] == catalyst)&(df["IPA_molefrac"] == 0)]["mean_mass_activity_SE"], fmt="", c='black', capsize=4, linewidth=1, zorder=0, marker="o", ls='none', markerfacecolor = 'b')
    
    plt.errorbar(df[(df["catalyst"] == catalyst)&(df["IPA_molefrac"] == 0.1)]["formate_mM"], df[(df["catalyst"] == catalyst)&(df["IPA_molefrac"] == 0.1)]["mean_mass_activity"], yerr=df[(df["catalyst"] == catalyst)&(df["IPA_molefrac"] == 0.1)]["mean_mass_activity_SE"], fmt="", c='black', capsize=4, linewidth=1, zorder=0, marker="^", ls='none', markerfacecolor = '#58a8f9')

    plt.errorbar(df[(df["catalyst"] == catalyst)&(df["IPA_molefrac"] == 0.2)]["formate_mM"], df[(df["catalyst"] == catalyst)&(df["IPA_molefrac"] == 0.2)]["mean_mass_activity"], yerr=df[(df["catalyst"] == catalyst)&(df["IPA_molefrac"] == 0.2)]["mean_mass_activity_SE"], fmt="", c='black', capsize=4, linewidth=1, zorder=0, marker="s", ls='none', markerfacecolor = 'g')

    ax.legend(["0 mol% IPA", "10 mol% IPA", "20 mol% IPA"])
    plt.ylabel("Ethylphenol Generation Rate (mM/g min)") #set the ylabel
    plt.xlabel("Formate Concentration (mM)") #set the xlabel
    ax.set_xscale('log') # select the x scaling 
    ax.set_yscale('linear') #set the y scaling 
    fig.savefig(f"mean_ethylphenol_generation_vs_formate_concentration_{catalyst}_{dpi}dpi.png", dpi=dpi, bbox_inches='tight') #export the figure as a 900 dpi .png
    ax.set_xlim((4, 7000))
    ax.set_ylim((None, 30))
    fig.savefig(f"mean_ethylphenol_generation_vs_formate_concentration_{catalyst}_{dpi}dpi_truncated.png", dpi=dpi, bbox_inches='tight') #export the figure as a 900 dpi .png
       
    print(f"saved figure as \"ethylphenol_generation_vs_formate_concentration_{catalyst}_{dpi}dpi.png\"") #print success message
    return fig, ax

if __name__ == "__main__":
 plot_mean_ethylphenol_generation_vs_formate_concentration(show_replicates=False)