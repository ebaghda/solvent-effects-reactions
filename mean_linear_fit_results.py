import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use("./style/simple_bold.mplstyle") #set plot style

def aggregate_replicates(filename: str = r"vinylphenol transfer hydrogenation(data)_fitted.parquet") -> pd.DataFrame:
    df = pd.read_parquet(filename)

    df["mean_mass_activity"] = np.nan
    df["mean_mass_activity_n"] = np.nan #number of replicates
    df["mean_mass_activity_SE"] = np.nan

    for catalyst in df.catalyst.unique():
        for formate_concentration in sorted(df.formate_mM.unique(), reverse=False):
            for IPA_concentration in sorted(df.IPA_molefrac.unique(), reverse=False):
            
                mask = (df["catalyst"] == catalyst) & (df["formate_mM"] == formate_concentration) & (df["IPA_molefrac"] == IPA_concentration)

                df.loc[mask, "mean_mass_activity"] = df.loc[mask, "mass_activity"].mean()
                 
                 # Calculate the propagated standard error of the mean (SEM)
                n = len(df.loc[mask, "mass_activity_SE"].unique())
                if n > 1:
                    mean_mass_activity_SE = np.sqrt(np.sum(df.loc[mask, "mass_activity_SE"]**2)) / n
                else:
                    try: mean_mass_activity_SE = df.loc[mask, "mass_activity_SE"].unique()[0]
                    except:
                        pass 

                df["mean_mass_activity_n"] = n
                df.loc[mask, "mean_mass_activity_SE"] = mean_mass_activity_SE
    df.to_parquet(filename.replace(".parquet", "_averaged.parquet"))
    print(f"Fitted data saved to {filename.replace('.parquet', '_fitted.parquet')}")
    return df

if __name__ == "__main__":
    df = aggregate_replicates()
    catalyst = "Pd"
    dpi = 900
    print(df[df["catalyst"] == "Pd"].head()) # Print the head of the aggregated DataFrame for inspection
    x = df[df["catalyst"] == "Pd"]["formate_mM"]
    y = df[df["catalyst"] == "Pd"]["mean_mass_activity"]
    yerror = df[df["catalyst"] == "Pd"]["mean_mass_activity_SE"]
    # plt.errorbar(x, y, yerr = yerror, ls='none', marker='o')
    fig, ax = plt.subplots(figsize=(5,5)) #initialize figure

    plt.errorbar(df[(df["catalyst"] == "Pd")&(df["IPA_molefrac"] == 0)]["formate_mM"], df[(df["catalyst"] == "Pd")&(df["IPA_molefrac"] == 0)]["mean_mass_activity"], yerr=df[(df["catalyst"] == "Pd")&(df["IPA_molefrac"] == 0)]["mean_mass_activity_SE"], fmt="", c='black', capsize=4, linewidth=1, zorder=0, marker="o", ls='none', markerfacecolor = 'b')
    
    plt.errorbar(df[(df["catalyst"] == "Pd")&(df["IPA_molefrac"] == 0.1)]["formate_mM"], df[(df["catalyst"] == "Pd")&(df["IPA_molefrac"] == 0.1)]["mean_mass_activity"], yerr=df[(df["catalyst"] == "Pd")&(df["IPA_molefrac"] == 0.1)]["mean_mass_activity_SE"], fmt="", c='black', capsize=4, linewidth=1, zorder=0, marker="^", ls='none', markerfacecolor = '#58a8f9')

    plt.errorbar(df[(df["catalyst"] == "Pd")&(df["IPA_molefrac"] == 0.2)]["formate_mM"], df[(df["catalyst"] == "Pd")&(df["IPA_molefrac"] == 0.2)]["mean_mass_activity"], yerr=df[(df["catalyst"] == "Pd")&(df["IPA_molefrac"] == 0.2)]["mean_mass_activity_SE"], fmt="", c='black', capsize=4, linewidth=1, zorder=0, marker="s", ls='none', markerfacecolor = 'g')

    ax.legend(["0 mol% IPA", "10 mol% IPA", "20 mol% IPA"])
    plt.ylabel("Ethylphenol Generation Rate (mM/g min)") #set the ylabel
    plt.xlabel("Formate Concentration (mM)") #set the xlabel
    ax.set_xscale('log') # select the x scaling 
    ax.set_yscale('linear') #set the y scaling 
    fig.savefig(f"mean_ethylphenol_generation_vs_formate_concentration_{catalyst}_{dpi}dpi.png", dpi=dpi, bbox_inches='tight') #export the figure as a 900 dpi .png
    print(f"saved figure as \"ethylphenol_generation_vs_formate_concentration_{catalyst}_{dpi}dpi.png\"") #print success message
    plt.show()