# Calculate negative semideviation or downside deviation.

def semideviation(r):
    """
    Returns the semideviation aka negative semideviation of r
    r must be a Series or a DataFrame
    """
    is_negative = r < 0
    return r[is_negative].std(ddof=0)

## Calculate skewness without using scipy.stats.skew().

def skewness(r):
    """
    Alternative to scipy.stats.skew()
    Computes the skewness of the supplied Series or DataFrame
    Returns a float or a Series
    """
    demeaned_r = r - r.mean()
    # use the polpulation standard deviation, so set dof = 0
    sigma_r =r.std(ddof=0)
    exp = (demeaned_r**3).mean()
    return exp/sigma_r**3

### Calculate kurtosis without using scipy.stats.kurtosis().

def kurtosis(r):
    """
    Alternative to scipy.stats.kurtosis()
    Computes the kurtosis of the supplied Series or DataFrame
    Returns a float or a Series
    """
    demeaned_r = r - r.mean()
    # use the polpulation standard deviation, so set dof = 0
    sigma_r =r.std(ddof=0)
    exp = (demeaned_r**4).mean()
    return exp/sigma_r**4

#### Calculate p_value of portfolio without using scipy.stats.jarque_bera(r).

import scipy.stats

def is_normal(r, level=0.01):
    """
    Applies the Jarque-Bera test to determine if a Series is normal or not
    Test is applied at the 1% level of default
    Returns True if the hypothesis of the normality is accepted, False otherwise
    """
#    statistic, p_value = scipy.stats.jarque_bera(r)
    if isinstance(r, pd.DataFrame):
        return r.aggregate(is_normal)
    else:
        statistic, p_value = scipy.stats.jarque_bera(r)
        return p_value >level

 
