import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from linear_fit import linear_fit
# initialize figure preferences
from set_fig_prefs import set_fig_prefs
set_fig_prefs()
#fig_dpi = 90 #set figure dpi

VP = pd.read_csv(r"4-vinylphenol_calibrations.csv")

# plot RRF vs. concentration
fig, ax = plt.subplots()
plt.scatter(VP["concentration"], VP["RRF"], s=20, c="Black")
plt.xlabel("4-Vinylphenol Concentration (mM)")
plt.ylabel("Relative Response Factor (-)")
plt.show()