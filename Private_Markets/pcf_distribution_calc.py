# Distribution Calculation of Private Credit Fund

import numpy as np

# Sample Data 
data = {
    'Date': pd.to_datetime(['2020-01-01', '2020-06-30', '2021-01-01', '2021-12-31', '2022-06-30']),
    'Type': ['Contribution', 'Distribution', 'Contribution', 'Distribution', 'Distribution'],
    'Amount': [-100000, 10000, -50000, 75000, 120000],
    'Partner': ['LP', 'LP', 'LP', 'LP', 'Both']

}

cash_flows = pd.DataFrame(data)

# Waterfall Terms (replace with your specific terms)
preferred_return_rate = 0.08 # 8% annual preferred return
gp_catch_up_pct = 0.20 # 20% catch-up
profit_split_lp = 0.80 # 80% to LPs after catch-up
profit_split_gp = 0.20 # 20% to GP after catch-up

# Calculate Waterfall
def calculate_waterfall(cash_flows, preferred_return_rate, gp_catch_up_pct, profit_split_lp, profit_split_gp):
    lp_cumulative_distributions = 0
    gp_cumulative_distributions = 0 
    lp_total_contributions = cash_flows[cash_flows['Type'] == 'Contribution']['Amount'].sum() * -1 # Make contributions positive

    # Sort cash flows by date
    cash_flows = cash_flows.sort_values('Date')

    # Iterate through cash flows and apply waterfall logic
    for index, row in cash_flows.iterrows():
        date = row['Date']
        cf_amount = row['Amount']
        partner = row['Partner']

        if partner == 'LP' and row['Type'] == 'Contribution':
            # This is a simplification; a real model would handle timing more precisely.
            pass

        elif partner == 'LP' and row['Type'] == 'Distribution':
            # Calculate preferred return amount based on contributions and time. 
            # This is a simplification and would require more complex calculation considering dates.
            preferred_return_amount = lp_total_contributions * preferred_return_rate

            # Tier 1: Return of Capital (to LPs)
            if lp_cumulative_distributions < lp_total_contributions:
                allocation_to_lp = min(cf_amount, lp_total_contributions - lp_cumulative_distributions)
                lp_cumulative_distributions += allocation_to_lp
                cf_amount -= allocation_to_lp
                print(f"{date}: LP received {allocation_to_lp:.2f} (Return of Capital)")

            # Tier 2: Preferred Return (to LPs)
            if cf_amount > 0 and lp_cumulative_distributions < lp_total_contributions + preferred_return_amount:
                # This is a simplification; a real model would handle timing more precisely.
                allocation_to_lp = min(cf_amount, lp_total_contributions + preferred_return_amount - lp_cumulative_distributions)
                lp_cumulative_distributions += allocation_to_lp
                cf_amount -= allocation_to_lp
                print(f"{date}: LP received {allocation_to_lp:.2f} (Preferred Return)")

            # Tier 3: GP Catch-up (to GP)
            if cf_amount > 0 and gp_cumulative_distributions < lp_cumulative_distributions * gp_catch_up_pct:
                # This is a simplification; a real model would handle timing more precisely.
                allocation_to_gp = min(cf_amount, lp_cumulative_distributions * gp_catch_up_pct - gp_cumulative_distributions)
                gp_cumulative_distributions += allocation_to_gp
                cf_amount -= allocation_to_gp
                print(f"{date}: GP received {allocation_to_gp:.2f} (Catch-up)")

            # Tier 4: Profit Split
            if cf_amount > 0:
                allocation_to_lp = cf_amount * profit_split_lp
                allocation_to_gp = cf_amount * profit_split_gp
                lp_cummulative_distributions += allocation_to_lp
                gp_cummulative_distributions += allocation_to_gp
                cf_amount = 0
                print(f"{date}: LP received {allocation_to_lp:.2f}, GP received {allocation_to_gp:.2f} (Profit Split)")

        elif partner == 'Both' and row['Type'] == 'Distribution':
            # Handle distribution to both parties
            # ...(apply waterfall logic similarly to LP distributions, splitting according to tiers)
            print(f"{date}: Distribution to Both - Waterfall logic applied")


# Run the waterfall calculation
calculate_waterfall(cash_flows, preferred_return_rate, gp_catch_up_pct, profit_split_lp, profit_split_gp)
