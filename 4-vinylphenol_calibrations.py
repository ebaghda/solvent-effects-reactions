import numpy as np #import numpy
import matplotlib.pyplot as plt #import matplotlib pyplot library
import pandas as pd #import pandas
plt.style.use("./style/simple_bold.mplstyle") #set plot style

# build 4-vinylphenol calibration data = VP Dataframe
VP = pd.DataFrame() #initialize the dataframe
# manually add calibration data
VP["concentration"] = np.array([0.03125, 0.3125, 3.125, 6.25, 12.5, 25, 50]) 
VP["VP_area"] = np.array([0.41, 1.6, 27.2, 64.7, 136, 294, 590.8])
VP["ISTD_area"] = np.array([394.5, 392.4, 394.4, 412.5, 382.6, 377.7, 366.9])
VP["peak_ratio"] = VP["VP_area"]/VP["ISTD_area"]
VP["RRF"] = VP["concentration"]*VP["ISTD_area"]/VP["VP_area"]/50
VP.to_csv(r"4-vinylphenol_calibrations.csv") #export the data to a .csv

from plot_calibration_curve import plot_calibration_curve1 #import calibration curve plot assist function
fig, ax = plot_calibration_curve1(VP["peak_ratio"], VP["concentration"], "Peak Ratio","4-Vinylphenol Concentration (mM)") #plot the calibration curve
fig.savefig("4-vinylphenol_calibrations_900dpi.png", dpi=900, bbox_inches='tight') #save the figure as a 900 dpi .png
print("figure saved as\"4-vinylphenol_calibrations_900dpi.png\"") #print success message