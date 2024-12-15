import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
# ethylphenol calibration data = EP

EP = pd.DataFrame()
EP.concentration = np.array([30, 15, 7.5, 3.75, 1.875, 0.9375, 0.46875, 0.046875])
EP.EP_area = np.array([391.4, 195.7, 94.9, 47, 24.4, 13.9, 7.9, 3.7])
EP.ISTD_area = np.array([368.8, 391.1, 383.8, 384.5, 368.8, 388.1, 397, 391.9])
EP.peak_ratio = EP.EP_area/EP.ISTD_area
EP.RRF = EP.concentration*EP.ISTD_area/EP.EP_area/50
print(EP.RRF)

plt.scatter(EP.concentration, EP.RRF, 6)
plt.xlabel("Ethylphenol Concentration (mM)")
plt.ylabel("Relative Response Factor (-)")
plt.show()
