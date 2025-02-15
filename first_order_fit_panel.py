import pandas as pd #import pandas
import numpy as np #import numpy
import matplotlib.pyplot as plt #import matplotlib.pyplot
plt.style.use("./style/simple_bold.mplstyle") #set matplotlib stylesheet


def plot_first_order_fitting_results(filepath: str = r"vinylphenol transfer hydrogenation(data).parquet", dpi: int = 300, vertical_layout: bool = True, catalyst: str = "Pd"):

    ## Perform first order fitting on each ethylphenol concentration profile for a given catalyst
    from first_order_fit import first_order_fit_ethylphenol_concentration_profiles #import fitting function -> yields dataframe
    
    try: #look for the already generated parquet file
        df = pd.read_parquet(f"{catalyst}_first_order_fit_results.parquet")
    except: #if it doesn't exist, remake it
        df = first_order_fit_ethylphenol_concentration_profiles(r"vinylphenol transfer hydrogenation(data).parquet", dpi = dpi) 

    if vertical_layout: #if the function is called with vertical_layout=True
        fig, ax = plt.subplots(len(df.formate_mM.unique()), 1, figsize = (5, 5*len(df.formate_mM.unique())))
    else:
        fig, ax = plt.subplots(1, len(df.formate_mM.unique()), figsize = (5*len(df.formate_mM.unique()), 5))

    formate_concentrations = sorted(df.formate_mM.unique(), reverse=vertical_layout) #sort the formate concentrations

    for i in range(len(formate_concentrations)): #for each formate concentration
        formate_concentration = formate_concentrations[i] #get the current formate concentration
        df = df.query("formate_mM == @formate_concentration & catalyst == @catalyst") #filter the data

        legend = ax[1].legend(["0% IPA", "10% IPA", "20% IPA"], loc="upper left") #add the legend
        legend.set_visible(False) #hide the legend

        ax[i].errorbar(df.query("IPA_molefrac == 0")["IPA_molefrac"], df.query("IPA_molefrac == 0")["mass_normalized_rate_constant"], yerr=df.query("IPA_molefrac == 0")["mass_normalized_rate_constant_SE"], fmt="", c='black', capsize=4, linewidth=1, zorder=0, marker="o", ls='none', markerfacecolor = 'b') #plot the 00% IPA data
        ax[i].errorbar(df.query("IPA_molefrac == 0.1")["IPA_molefrac"], df.query("IPA_molefrac == 0.1")["mass_normalized_rate_constant"], yerr=df.query("IPA_molefrac == 0.1")["mass_normalized_rate_constant_SE"], fmt="", c='black', capsize=4, linewidth=1, zorder=0, marker="^", ls='none', markerfacecolor = '#58a8f9') #plot 10% IPA data
        ax[i].errorbar(df.query("IPA_molefrac == 0.2")["IPA_molefrac"], df.query("IPA_molefrac == 0.2")["mass_normalized_rate_constant"], yerr=df.query("IPA_molefrac == 0.2")["mass_normalized_rate_constant_SE"], fmt="", c='black', capsize=4, linewidth=1, zorder=0, marker="s", ls='none', markerfacecolor = 'g') #plot 20% IPA data
        
        ax[i].annotate(f"{catalyst}\n{formate_concentration} mM potassium formate", (0.02, 0.89), xycoords="axes fraction", fontweight="bold") #add the catalyst label
        
        ax[i].set_xlabel("IPA Concentration (mole/mole)", labelpad=5) #add x axis label
        ax[i].set_ylabel("Apparent Rate Constant (1/g min)", labelpad=5) #add y axis label
        ax[i].set_xticks([0, 0.1, 0.2]) #set x axis tick marks
        ax[i].set_xticklabels(["0", "0.1", "0.2"]) #set x axis tick labels
        ax[i].set_xlim(-0.05, 0.25) #set the x axis limits
        ax[i].set_ylim(-0.3, 5) if catalyst == "Pd" else None #set the y axis limits
        
    plt.tight_layout() #correct the layout
    fig.savefig(f"ethylphenol_generation_vs_IPA_concentrationFIRSTORDERFIT_RESULT_panel_{catalyst}_{dpi}dpi.png", bbox_inches="tight", dpi=dpi) #save the figure as a 900 dpi .png
    fig.clf()
    print(f'figure saved to "ethylphenol_generation_vs_IPA_concentration_panel_{catalyst}_{dpi}dpi.png"') #print success message
        

if __name__ == "__main__":
    plot_first_order_fitting_results(r"vinylphenol transfer hydrogenation(data).parquet", dpi = 250, vertical_layout=False, catalyst = "Pd")
    plot_first_order_fitting_results(r"vinylphenol transfer hydrogenation(data).parquet", dpi = 250, vertical_layout=False, catalyst = "Pt")
