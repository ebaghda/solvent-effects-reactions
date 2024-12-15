import matplotlib.pyplot as plt
import numpy as np
def plot_calibration_curve(x_data, y_data, x_label, y_label):

    # perform linear fit on the data
    # calculate first degree polynomial
    
    z = np.polyfit(x_data, y_data, 1)
    f = np.poly1d(z)
    
    # generate data for linear fit
    x_fit = np.linspace(np.min(x_data), np.max(x_data), 2)
    y_fit = f(x_fit)
    
    # generate the plot
    fig, ax = plt.subplots(figsize=[5,5])
    plt.scatter(x_data, y_data, s=14, c='darkred')
    plt.plot(x_fit, y_fit, 'k')
    
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.show()