import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from linear_fit import linear_fit
plt.style.use("./style/simple_bold.mplstyle") #set plot style

VP = pd.read_csv(r"4-vinylphenol_calibrations.csv")

# plot RRF vs. concentration
fig, ax = plt.subplots()
plt.scatter(VP["concentration"], VP["RRF"], s=20, c="Black")
plt.xlabel("4-Vinylphenol Concentration (mM)")
plt.ylabel("Relative Response Factor (-)")
plt.savefig("4-vinylphenol_RRF_900dpi.png", dpi=900, bbox_inches='tight')
plt.show()