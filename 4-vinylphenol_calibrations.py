import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from linear_fit import linear_fit
plt.style.use("./style/simple_bold.mplstyle") #set plot style

# build 4-vinylphenol calibration data = VP Dataframe
VP = pd.DataFrame()
VP["concentration"] = np.array([0.03125, 0.3125, 3.125, 6.25, 12.5, 25, 50])
VP["VP_area"] = np.array([0.41, 1.6, 27.2, 64.7, 136, 294, 590.8])
VP["ISTD_area"] = np.array([394.5, 392.4, 394.4, 412.5, 382.6, 377.7, 366.9])
VP["peak_ratio"] = VP["VP_area"]/VP["ISTD_area"]
VP["RRF"] = VP["concentration"]*VP["ISTD_area"]/VP["VP_area"]/50
VP.to_csv(r"4-vinylphenol_calibrations.csv")

## generate figures

# plot calibration curve
from plot_calibration_curve import plot_calibration_curve
plot_calibration_curve(VP["peak_ratio"], VP["concentration"], "Peak Ratio","4-Vinylphenol Concentration (mM)")