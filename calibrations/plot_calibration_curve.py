import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

def plot_calibration_curve1(x_data, y_data, x_label, y_label): #define function
    fit_params = linregress(x_data, y_data) #fit the data using linear fit
    print(fit_params) #print the fit parameters
    fig, ax = plt.subplots() #initialize figure
    plt.scatter(x_data, y_data, s=20, c='darkred') #plot the calibration data
    plt.plot(x_data, fit_params.slope*x_data+fit_params.intercept, 'k') #plot the linear fit
    plt.xlabel(x_label) #add x axis label
    plt.ylabel(y_label) #add y axis label
    plt.annotate("concentration = "+ 
                 np.array2string(fit_params.slope, precision=2)+"±"+
                 np.array2string(fit_params.stderr, precision=2)+" + "+
                 np.array2string(fit_params.intercept, precision=2) +"±"+
                 np.array2string(fit_params.intercept_stderr, precision=2) +" * (peak ratio)\ncorrelation coefficient: "+
                 np.array2string(fit_params.rvalue, precision=4), 
                 xy=(0.15,0.78), xycoords="figure fraction", fontsize=12) #add the fit equation and line to the plot
    print("returned plot to fig, ax)") #print success message
    return fig, ax #return fig, ax objects