# Calculating Multiple On Invested Capital (MOIC)

def calculate_moic(total_value, invested_capital):
    """
    Calculates the Multiple on Invested Capital (MOIC).

    Args:
    total_value: The total value generated from the investment, including realized and unrealized gains.

    invested_capital: The total initial amount of capital invested.

    Returns:
    The MOIC value as a float, or None if invested capital is zero.
    """
    if invested_capital == 0:
        return None # Avoid division by zero
    else:
        return total_value / invested_capital

# Example usage for a single investment:
initial_investment_single = 1000000 # $1 million
total_returns_single = 3000000 # $3 million
moic_single = calculate_moic(total_returns_single, initial_investment_single)

print(f"MOIC for the single investment: {moic_single:.2f}x")

# Example usuage for a portfolio:
realized_value_portfolio = 260000000 # $260 million
unrealized_value_portfolio = 500000000 # $500 million
total_invested_portfolio = 200000000 # $200 million

total_value_portfolio = realized_value_portfolio + unrealized_value_portfolio
moic_portfolio = calculate_moic(total_value_portfolio, total_invested_portfolio)

print(f"MOIC for the portfolio: {moic_portfolio:.2f}x")
