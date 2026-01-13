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
