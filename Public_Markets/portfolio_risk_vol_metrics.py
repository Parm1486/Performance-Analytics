# Calculate Annualize Volatility of Asset

def annualize_vol(r, periods_per_year):
    """
    Annualizes the vol of a set of returns
    Infer the periods per year
    """
    return r.std()*(periods_per_year**0.5)

## Calcualte Portfolio Volatility

def portfolio_vol(weights, covmat):
    """
    Weights -> Vol
    """
    return (weights.T @ covmat @ weights)**0.5

### Calculate Historic Value at Risk

import numpy as np
def var_historic(r, level=5):
    """
    Return the historic Value at Risk at a specified level
    i.e. returns the number such that "level" percent of returns
    fall below that number, and the (100-level) percent are above
    """
    if isinstance(r, pd.DataFrame):
        return r.aggregate(var_historic, level=level)
    elif isinstance(r, pd.Series):
        return -np.percentile(r, level)
    else:
        raise TypeError("Expected r to be Series or DataFrame")

#### Calculate Gaussian Value at Risk

from scipy.stats import norm
def var_gaussian(r, level=5, modified=False):
    """
    Returns the Parametric Gaussian Varof a Series or DataFrame
    If "modified" is True, then the modified VaR is returned, 
    using the Cornish-Fisher modification
    """
    # compute the Z score assuming it was Gaussian
    z = norm.ppf(level/100)
    if modified:
        # modify the Z score based on observed skewness and kurtosis
        s = skewness(r)
        k = kurtosis(r)
        z = (z + 
                 (z**2 -1)*s/6 +
                 (z**3 -3*z)*(k-3)/24-
                 (2*z**3 - 5*z)*(s**2)/36
            )
        
    return -(r.mean() + z*r.std(ddof=0))

##### Calculate Conditional Value at Risk

def cvar_historic(r, level=5):
    """
    Computes the Conditional VaR of Series or DataFrame
    """
    if isinstance(r, pd.Series):
        is_beyond = r <= -var_historic(r, level=level)
        return -r[is_beyond].mean()
    elif isinstance(r, pd.DataFrame):
        return r.aggregate(cvar_historic, level=level)
    else:
        raise TypeError("Expected r to be a Series or DataFrame")

