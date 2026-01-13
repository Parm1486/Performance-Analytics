# Calculating yeilds in Private Credit Fund (Current Yeild and IRR/XIRR) 

import pandas as pd

# Assuming you have a DataFrame with quarterly data
# Example data (replace with your actual data)
data = {'Quarter': ['Q1 2024', 'Q2 2024', 'Q3 2024', 'Q4 2024'],
        'Interest_Income': [2.1e9, 2.2e9, 2.3e9, 2.4e9],
        'Average_Assets_Fair_Value': [88e9, 89e9, 90.4e9, 91e9]}

df = pd.DataFrame(data)

# Calculate Current Yeild for each quarter
df['Current_Yeild_Quarterly'] = df['Interest_Income'] / df['Average_Assets_Fair_Value']

# Annualize the Current Yeild (assuming 4 quarters in a year)
df['Current_Yeild_Annualized'] = df['Current_Yeild_Quarterly']*4

print(df)


# XIRR Calculation

from scipy.optimize import newton
from datetime import datetime

# Function to compute XIRR
def compute_xirr(cashflows, cashflow_dates):
    # Convert dates into days since the first date
    day_counts = [(date - cashflow_dates[0]).days for date in cashflow_dates]
    
    # Define NPV function for XIRR
    def npv_equation(rate):
        return sum(cash / ((1 + rate) ** (days / 365)) for cash, days in zip(cashflows, day_counts))
        
   # Solve for the rate that zeroes the NPV
    return newton(npv_equation, x0=0.1) # Initial Guess:10%

# Example A General Investment Scenario
cashflows = [-1500, 400, 800, 1900]
cashflow_dates = [datetime(2023, 1, 1),
                  datetime(2023, 4, 1),
                  datetime(2023, 9, 1),
                  datetime(2024, 1, 1)]

# Calculate the XIRR
annualized_return = compute_xirr(cashflows, cashflow_dates)
print(f"Annualized Return (XIRR): {annualized_return:,.2%}")     

# Example 2: Real Estate Investment
property_cashflows = [-60000, 6000, 6000, 75000]
property_dates = [
    datetime(2022, 1, 1),
    datetime(2022, 7, 1),
    datetime(2023, 1, 1),
    datetime(2023, 7, 1)
]

# Compute the property XIRR
property_return = compute_xirr(property_cashflows, property_dates)
print(f"Property Investment XIRR: {property_return:.2%}")

# Portfolio XIRR Calculation
portfolio_cashflows = {
    "Real Estate": [-80000, 10000, 15000, 100000],
    "Stock Investments": [-50000, 12000, 13000, 70000]
}

portfolio_dates = {
    "Real Estate": [
        datetime(2021, 1, 1),
        datetime(2021, 7, 1),
        datetime(2022, 1, 1),
        datetime(2022, 12, 31)
    ],
    "Stock Investments": [
        datetime(2022, 2, 1),
        datetime(2022, 8, 1),
        datetime(2023, 2, 1),
        datetime(2023, 8, 1)
    ]
}

# Compute XIRR for each investment 
for asset, flows in portfolio_cashflows.items():
    asset_dates = portfolio_dates[asset]
    asset_xirr = compute_xirr(flows, asset_dates)
    print(f"{asset} Annualized Return (XIRR): {asset_xirr:.2%}")
