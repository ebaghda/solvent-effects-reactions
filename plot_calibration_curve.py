import matplotlib.pyplot as plt
import numpy as np

def plot_calibration_curve(x_data, y_data, x_label, y_label):

    # perform linear fit on the data
    # calculate first degree polynomial
    fit_coefs = np.polynomial.Polynomial.fit(x_data, y_data, deg=1,domain=[-1, 1])
    fit_line = np.polynomial.Polynomial.linspace(fit_coefs, 2, domain=[np.min(x_data), np.max(x_data)])
    
    #calculate fit error
    from linear_fit import linear_fit
    fit_coefficients, standard_errors, corr_coef = linear_fit(x_data, y_data, True)
    
    # generate the plot
    fig, ax = plt.subplots()
    plt.scatter(x_data, y_data, s=20, c='darkred')
    plt.plot(fit_line[0], fit_line[1], 'k')
    
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    #plt.annotate(fit_coefs, [np.min(x_data), np.max(y_data)])
    plt.annotate("concentration = "+ np.array2string(fit_coefficients[0], precision=2)+"±"+np.array2string(standard_errors[0], precision=2)+" + "+np.array2string(fit_coefficients[1], precision=2) +"±"+np.array2string(standard_errors[1], precision=2) +"*(peak ratio)\nCorrelation Coefficient:"+np.array2string(corr_coef, precision=4), (np.min(x_data), np.max(y_data)-10))
    #plt.annotate(standard_errors, [np.min(x_data), np.max(y_data)*1/3])
    plt.show()