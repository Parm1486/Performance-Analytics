# Calculate the Distributed to Paid-In Capital for a private credit fund

## Gross Distributed to Paid-In Capital for a private credit fund
def calculate_dpi(cumulative_distributions, paid_in_capital):
    """
    Calculates the Distributed to Paid-In Capital (DPI) for a private credit fund.

    Args:
       Cumulative_distributions: The total amount of cash distributions made to investors.
       paid_in_capital: The total capital contributed by investors.

    Returns:
       The DPI value, which represents the ratio of distributions to paid in capital.
    """
    if paid_in_capital == 0:
        return None # Avoid division by zero
    else:
        return cumulative_distributions / paid_in_capital

# Example usage:
cumulative_distributions = 120000000 # Example value in USD
paid_in_capital = 80000000 # Example value in USD

dpi = calculate_dpi(cumulative_distributions, paid_in_capital)
print(f"The DPI for the private credit fund is: {dpi:.2f}x")


### Net Distributed to Paid-In Capital for a private credit fund
def calculate_net_dpi(cumulative_distributions, total_fees_expenses, paid_in_capital):
    """
    Calculates the Net Distributed to Paid-In Capital (DPI) for a private credit fund.

    Args:
       Cumulative_distributions: The total amount of cash distributions made to investors.
       total_fees_expenses: The total fees and expenses deducted by the GP.
       paid_in_capital: The total capital contributed by investors.

    Returns:
       The Net DPI value, which represents the ratio of net distributions to paid in capital.
    """
    if paid_in_capital == 0:
        return None # Avoid division by zero
    else:
        return (cumulative_distributions - total_fees_expenses) / paid_in_capital

# Example usage:
cumulative_distributions = 120000000 # Example value in USD
total_fees_expenses = 10000000 # Example value in USD
paid_in_capital = 80000000 # Example value in USD

net_dpi = calculate_net_dpi(cumulative_distributions,total_fees_expenses, paid_in_capital)

# Print the results
print(f"Total Distributions: ${cumulative_distributions:.2f}")
print(f"Total Fees and Expenses: ${total_fees_expenses:.2f}")
print(f"Total Capital Called: ${paid_in_capital:.2f}")
print(f"Net DPI: {net_dpi:.2f}x")
