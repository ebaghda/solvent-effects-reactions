import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from linear_fit import linear_fit
plt.style.use("./style/simple_bold.mplstyle") #set plot style

EP = pd.read_csv(r"ethylphenol_calibrations.csv")

# plot RRF vs. concentration
fig, ax = plt.subplots()
plt.scatter(EP["concentration"], EP["RRF"], s=20, c="Black")
plt.xlabel("Ethylphenol Concentration (mM)")
plt.ylabel("Relative Response Factor (-)")
plt.savefig("ethylphenol_RRF_900dpi.png", dpi=900, bbox_inches='tight')
plt.show()