import numpy as np # import numpy
import matplotlib.pyplot as plt #import matplotlib pyplot library
import pandas as pd #import pandas
plt.style.use("./style/simple_bold.mplstyle") #set plot stylesheet

VP = pd.read_csv(r"4-vinylphenol_calibrations.csv") #import the calibration data

fig, ax = plt.subplots() #initialize the figure
plt.scatter(VP["concentration"], VP["RRF"], s=20, c="Black") #plot the calibration data
plt.xlabel("4-Vinylphenol Concentration (mM)") #label x axis
plt.ylabel("Relative Response Factor (-)") #label y axis
plt.savefig("4-vinylphenol_RRF_900dpi.png", dpi=900, bbox_inches='tight') #save the figure as a 900 dpi .png
print('figure saved as "4-vinylphenol_RRF_900dpi.png"') #print success message