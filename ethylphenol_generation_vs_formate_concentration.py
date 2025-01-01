import pandas as pd
import matplotlib.pyplot as plt
plt.style.use("./style/simple_bold.mplstyle") #select stylesheet

catalyst = "Pd" #select catalyst

def load_and_filter_data(filepath: str, catalyst: str) -> pd.DataFrame: #define a function to load and filter the data
    DF = pd.read_parquet(filepath) #import the data
    df = DF.query("time_min == 0 & catalyst == @catalyst") #filter the data
    return df #return the filtered data

def plot_ethylphenol_generation_rate_vs_formate_concentration(filepath: str, catalyst: str, dpi: int) -> None: #define the main function
    df = load_and_filter_data(filepath, catalyst) #load and filter data

    fig, ax = plt.subplots(figsize=(5,5)) #initialize figure
    plt.errorbar(df.query("IPA_molefrac == 0")["formate_mM"], df.query("IPA_molefrac == 0")["EP_generation_rate"], yerr=df.query("IPA_molefrac == 0")["EP_generation_rate_std_err"], fmt="", c='black', capsize=4, linewidth=1, zorder=0, marker="o", ls='none', markerfacecolor = 'b') #plot the standard error of each fit
    plt.errorbar(df.query("IPA_molefrac == 0.1")["formate_mM"], df.query("IPA_molefrac == 0.1")["EP_generation_rate"], yerr=df.query("IPA_molefrac == 0.1")["EP_generation_rate_std_err"], fmt="", c='black', capsize=4, linewidth=1, zorder=0, marker="^", ls='none', markerfacecolor = '#58a8f9') #plot the standard error of each fit
    plt.errorbar(df.query("IPA_molefrac == 0.2")["formate_mM"], df.query("IPA_molefrac == 0.2")["EP_generation_rate"], yerr=df.query("IPA_molefrac == 0.2")["EP_generation_rate_std_err"], fmt="", c='black', capsize=4, linewidth=1, zorder=0, marker="s", ls='none', markerfacecolor = 'g') #plot the standard error of each fit


    # plt.scatter(df_0pctIPA["formate_mM"], df_0pctIPA["EP_generation_rate"], marker='o', c='b', s=30) #plot the 0% IPA ethylphenol generation rates against formate concentration
    # plt.scatter(df_10pctIPA["formate_mM"], df_10pctIPA["EP_generation_rate"], marker='^', c="#58a8f9", s=30) #plot the 10% IPA ethylphenol generation rates against formate concentration
    # plt.scatter(df_20pctIPA["formate_mM"], df_20pctIPA["EP_generation_rate"], marker='s',  c='g', s=30) #plot the 20% IPA ethylphenol generation rates against formate concentration

    plt.ylabel("Ethylphenol Generation Rate (mM/g min)") #set the ylabel
    plt.xlabel("Formate Concentration (mM)") #set the xlabel
    ax.set_xscale('log') # select the x scaling 
    ax.set_yscale('linear') #set the y scaling 
    fig.savefig(f"ethylphenol_generation_vs_formate_concentration_{catalyst}_{dpi}dpi.png", dpi=dpi, bbox_inches='tight') #export the figure as a 900 dpi .png
    print(f"saved figure as \"ethylphenol_generation_vs_formate_concentration_{catalyst}_{dpi}dpi.png\"") #print success message

if __name__ == "__main__": #run script if it is called directly
    plot_ethylphenol_generation_rate_vs_formate_concentration(filepath=r"vinylphenol transfer hydrogenation(data).parquet", catalyst="Pd", dpi=300) #run script