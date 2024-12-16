import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from linear_fit import linear_fit
# initialize figure preferences
from set_fig_prefs import set_fig_prefs
set_fig_prefs()
#fig_dpi = 90 #set figure dpi

EP = pd.read_csv(r"ethylphenol_calibrations.csv")

# plot RRF vs. concentration
fig, ax = plt.subplots()
plt.scatter(EP["concentration"], EP["RRF"], s=20, c="Black")
plt.xlabel("Ethylphenol Concentration (mM)")
plt.ylabel("Relative Response Factor (-)")
plt.show()