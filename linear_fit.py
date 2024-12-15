
import numpy as np
def linear_fit(x,y,verbose):
    
    # Polynomial degree
    degree = 1

    # Construct design matrix
    X = np.vander(x, degree + 1)

    # Solve for coefficients manually
    XtX_inv = np.linalg.inv(X.T @ X)  # (X^T X)^(-1)
    beta_hat = XtX_inv @ X.T @ y      # Coefficients

    # Compute residuals
    y_fit = X @ beta_hat
    residuals = y - y_fit

    # Residual variance
    n = len(y)  # Number of data points
    p = degree + 1  # Number of coefficients
    residual_variance = np.sum(residuals**2) / (n - p)

    # Covariance matrix of coefficients
    cov_matrix = residual_variance * XtX_inv

    # Standard errors of coefficients
    standard_errors = np.sqrt(np.diag(cov_matrix))
    if verbose:
        print("Coefficients:", beta_hat)
        print("Standard Errors:", standard_errors)

    # flip arrays to match polynomial notation a*x^0 + b*x^1 + c*x^2...
    beta_hat = np.flip(beta_hat)
    standard_errors = np.flip(standard_errors)

    return beta_hat, standard_errors