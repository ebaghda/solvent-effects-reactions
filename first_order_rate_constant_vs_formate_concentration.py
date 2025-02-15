import pandas as pd
import matplotlib.pyplot as plt
plt.style.use("./style/simple_bold.mplstyle") #select stylesheet

def plot_rate_constant_vs_formate_concentration(filepath: str, catalyst: str, dpi: int = 600):
    # Load the fitted data
    df = pd.read_parquet(filepath)
    
    # Filter the data for the specified catalyst
    df = df.query("catalyst == @catalyst & formate_mM > 100")
        
    # Plot the data
    fig, ax = plt.subplots(figsize=(5, 5))
    ax.errorbar(df[df["IPA_molefrac"] == 0]['formate_mM'], df[df["IPA_molefrac"] == 0]['rate_constant'], yerr=df[df["IPA_molefrac"] == 0]['rate_constant_SE'],c="k", capsize=4, linewidth=1, marker='o', markerfacecolor='darkblue', ls='none') #plot the 0% IPA data
    
    ax.errorbar(df[df["IPA_molefrac"] == 0.1]['formate_mM'], df[df["IPA_molefrac"] == 0.1]['rate_constant'], yerr=df[df["IPA_molefrac"] == 0.1]['rate_constant_SE'], c="k", capsize=4, linewidth=1, marker='^', markerfacecolor='#58a8f9', ls='none') #plot the 10% IPA data
    
    ax.errorbar(df[df["IPA_molefrac"] == 0.2]['formate_mM'], df[df["IPA_molefrac"] == 0.2]['rate_constant'], yerr=df[df["IPA_molefrac"] == 0.2]['rate_constant_SE'], c="k", capsize=4, linewidth=1, marker='s', markerfacecolor='darkgreen', ls='none') #plot the 20% IPA data

    plt.xlabel('Formate Concentration (mM)')
    plt.ylabel('Rate Constant (1/g min)')
    # ax.set_ylim((0, 2))
    ax.legend(["0 mol% IPA", "10 mol% IPA", "20 mol% IPA"])
    ax.set_xscale('log') # select the x scaling 
    ax.set_yscale('linear') #set the y scaling 
    
    plt.savefig(f'first_order_rate_constant_vs_formate_concentration_{catalyst}_{dpi}dpi.png', dpi=dpi, bbox_inches='tight')
    print(f'Plot saved as rate_constant_vs_formate_concentration_{catalyst}_{dpi}dpi.png')

if __name__ == "__main__":
    filepath = r"vinylphenol transfer hydrogenation(data)_fitted.parquet"
    catalyst = "Pd"
    plot_rate_constant_vs_formate_concentration(filepath, catalyst)