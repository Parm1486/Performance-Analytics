# Calculating RVPI (Residual Value to Paid-In Capital) metric for a Private Credit fund

def calculate_rvpi(residual_value, paid_in_capital):
    """
    Calculates the Residual Value to Paid-In Capital (RVPI).

    Args:
       residual_value: The fair market value of all unrealized investments in the fund's portfolio.
       paid_in_capital: The total amount of capital contributed by investors.

    Returns:
       The RVPI ratio, or None if paid-in capital is zero.
    """
    if paid_in_capital == 0:
        return None # Avoid division by zero
    else:
        rvpi = residual_value / paid_in_capital
        return rvpi

# Example usage:
residual_value = 40000000 # in USD
paid_in_capital = 10000000 # in USD

rvpi_result = calculate_rvpi(residual_value, paid_in_capital)

if rvpi_result is not None:
    print(f"The RVPI is: {rvpi_result:.2f}")
else:
    print("Cannot calculate RVPI, paid-in capital is zero.")
