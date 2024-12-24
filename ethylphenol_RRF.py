import numpy as np #import numpy
import matplotlib.pyplot as plt #import pyplot library
import pandas as pd #import pandas
plt.style.use("./style/simple_bold.mplstyle") #set plot stylesheet

EP = pd.read_csv(r"ethylphenol_calibrations.csv") #import data

# plot RRF vs. concentration
fig, ax = plt.subplots() #initialize figure
plt.scatter(EP["concentration"], EP["RRF"], s=20, c="Black") #plot data
plt.xlabel("Ethylphenol Concentration (mM)") #label x axis
plt.ylabel("Relative Response Factor (-)") #label y axis
plt.savefig("ethylphenol_RRF_900dpi.png", dpi=900, bbox_inches='tight') #save figure as 900 dpi .png
print("Figure saved as \"ethylphenol_RRF_900dpi.png\"") #print success message