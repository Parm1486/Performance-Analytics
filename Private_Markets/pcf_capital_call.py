# Calculating Capital Calls for Private Credit Fund
# Sample data: Investor commitments and a required Capital amount
import pandas as pd

investor_commitments = {
    'LP1': 2000000,
    'LP2': 1000000,
    'LP3': 3000000 
}

total_committed_capital = sum(investor_commitments.values())
required_capital_call_amount = 1500000 #Fund required

#Calculate each investor's pro rata share of the capital call
capital_calls = {}
for investor, commitment in investor_commitments.items():
    pro_rata_share = commitment / total_committed_capital
    capital_calls[investor] = required_capital_call_amount * pro_rata_share

# Print the calculated capital calls for each investor
print("Capital Call Amounts:")
for investor, amount in capital_calls.items():
    print(f"{investor}: ${amount}")

# Example of how to track uncalled capital (simplified)
uncalled_capital = {}
for investor, commitment in investor_commitments.items():
    uncalled_capital[investor] = commitment - capital_calls[investor]

print("\nRemaining Uncalled Capital:")
for investor, amount in uncalled_capital.items():
    print(f"{investor}: ${amount: .2f}")
