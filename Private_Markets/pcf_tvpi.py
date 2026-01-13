# Calculating TVPI for Private Credit Fund

def calculate_tvpi(paid_in_capital, distributed_value, residual_value):
    """
    Calculates the Total Value to Paid-In Capital (TVPI) for a private fund.

    Args:
       paid_in_capital: The total capital contributed by investors.
       distributed_value: The total capital returned to investors so for.
       residual_value: The current unrealized value of a fund's investments.

    Returns:
       The TVPI as a multiple.
    """
    if paid_in_capital == 0:
        return None
    total_value = distributed_value + residual_value
    tvpi = total_value / paid_in_capital
    return tvpi

# Example Usage:
paid_in = 70000000 # $70 million paid in capital
distributions = 85000000 # $85 million in distributions
residual = 65000000 # $65 million in residual value

tvpi_result = calculate_tvpi(paid_in, distributions, residual)

print(f"The TVPI is: {tvpi_result:.2f}x")
