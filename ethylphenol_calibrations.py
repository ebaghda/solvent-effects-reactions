import numpy as np #imporrt numpy
import matplotlib.pyplot as plt #import matplotlib pyplot package
import pandas as pd #import pandas
plt.style.use("./style/simple_bold.mplstyle") #set plot stylesheet

EP = pd.DataFrame() #initialize dataframe and manually populate with date
EP["concentration"] = np.array([30, 15, 7.5, 3.75, 1.875, 0.9375, 0.46875, 0.046875])
EP["EP_area"] = np.array([391.4, 195.7, 94.9, 47, 24.4, 13.9, 7.9, 3.7])
EP["ISTD_area"] = np.array([368.8, 391.1, 383.8, 384.5, 368.8, 388.1, 397, 391.9])
EP["peak_ratio"] = EP["EP_area"]/EP["ISTD_area"]
EP["RRF"] = EP["concentration"]*EP["ISTD_area"]/EP["EP_area"]/50
EP.to_csv(r'ethylphenol_calibrations.csv') #export the data to a .csv

from plot_calibration_curve import plot_calibration_curve #import custom calibration curve plotting helper function
fig, ax = plot_calibration_curve(EP["peak_ratio"], EP["concentration"], "Peak Ratio","Ethylphenol Concentration (mM)") #generate the calibration figure
fig.savefig("ethylphenol_calibrations_900dpi.png", dpi=900, bbox_inches='tight') #save figure as 900 dpi .png
print('figure saved as "ethylphenol_calibrations_900dpi.png"') #print success message