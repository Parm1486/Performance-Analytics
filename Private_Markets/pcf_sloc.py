# Calculating Subscription Lines of Credit for Private Credit Funds

advance_rate = 0.7 # 70% advance rate

# Assume initial uncalled capital equals the full commitment
uncalled_capital = investor_commitments

# Calculate the borrowing base
borrowing_base = sum([uncalled_capital[investor] * advance_rate for investor in uncalled_capital])

print(f"Total Uncalled Capital: ${sum(uncalled_capital.values()): .2f}")
print(f"Calculated Borrowing Base: ${borrowing_base: .2f}")

# Example of a capital call
capital_call = 2000000

# Update uncalled capital after the capital call
for investor in uncalled_capital:
    uncalled_capital[investor] -= (capital_call / len(uncalled_capital))

 # Recalculate borrowing base
borrowing_base = sum([uncalled_capital[investor] * advance_rate for investor in uncalled_capital])

print(f"Uncalled Capital After Call: ${sum(uncalled_capital.values()): .2f}")
print(f"New Borrowing Base: ${borrowing_base: .2f}")
