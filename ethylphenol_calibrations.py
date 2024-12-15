import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# initialize figure preferences
from set_fig_prefs import set_fig_prefs
set_fig_prefs()
#fig_dpi = 90 #set figure dpi

# build ethylphenol calibration data = EP Dataframe

EP = pd.DataFrame()
EP.concentration = np.array([30, 15, 7.5, 3.75, 1.875, 0.9375, 0.46875, 0.046875])
EP.EP_area = np.array([391.4, 195.7, 94.9, 47, 24.4, 13.9, 7.9, 3.7])
EP.ISTD_area = np.array([368.8, 391.1, 383.8, 384.5, 368.8, 388.1, 397, 391.9])
EP.peak_ratio = EP.EP_area/EP.ISTD_area
EP.RRF = EP.concentration*EP.ISTD_area/EP.EP_area/50

# generate figures

fig, ax = plt.subplots()
plt.scatter(EP.concentration, EP.RRF, 16, "Black")
plt.xlabel("Ethylphenol Concentration (mM)")
plt.ylabel("Relative Response Factor (-)")
plt.show()
