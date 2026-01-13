# Calculating Subscription Lines of Credit for Private Credit Funds

advance_rate = 0.7 # 70% advance rate

# Assume initial uncalled capital equals the full commitment
uncalled_capital = investor_commitments

# Calculate the borrowing base
borrowing_base = sum([uncalled_capital[investor] * advance_rate for investor in uncalled_capital])

print(f"Total Uncalled Capital: ${sum(uncalled_capital.values()): .2f}")
print(f"Calculated Borrowing Base: ${borrowing_base: .2f}")
