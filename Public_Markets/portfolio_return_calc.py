# Getting Historical Returns from portfolios/ assets, converting it to comparable form and indexing.  

def get_ffme_returns():
    me_m = pd.read_csv("path/file.csv",
                   header=0, index_col=0, parse_dates=True, date_format= "%Y-%m", na_values=-99.99
                  )
    rets = me_m[['Column']]
    rets = rets/100
    rets.index = pd.to_datetime(rets.index, format= "%Y%m")
    rets.index = rets.index.to_period('M')
    return rets

## Calculating Market Cap, Weight, and Total Weighted Returns

def get_total_market_index_returns():
    """
    Load portfolio data and derive the returns of a capweighted total market index
    """
    ind_mktcap = ind_nfirms * ind_size
    total_mktcap = ind_mktcap.sum(axis="columns")
    ind_capweight = ind_mktcap.divide(total_mktcap, axis ="rows")
    total_market_return = (ind_capweight * ind_return).sum(axis="columns")
    return total_market_return

### Calculate annualize returns.

def annualize_rets(r, periods_per_year):
    """
    Annaulize a set of returns, Infer the periods per year.
    """
    compounded_growth = (1+r).prod()
    n_periods = r.shape[0]
    return compounded_growth**(periods_per_year/n_periods)-1

#### Calculate portfolio return.

def portfolio_return(weights, returns):
    """
    Weights -> Returns
    """
    return weights.T @ returns





