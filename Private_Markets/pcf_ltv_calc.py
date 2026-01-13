# LTV to Value (LTV) Calculation for Private Credit Fund

def calculate_ltv(loan_amount, asset_value):
    """
    Calculates the Loan-to-Value (LTV) ratio.

    Args:
      loan_amount: The amount of the loan.
      asset_value: The appraised value of the underlying asset (portfolio company value).

    Returns:
      The LTV ratio as percentage.
      Returns None if the asset value is zero to avoid division by zero.
    """
    if asset_value == 0:
        return None # Or handle the case as appropriate (e.g., raise an error)
    return (loan_amount / asset_value)* 100

# Example usage:
loan = 15000000 # Example loan amount (e.g., for a portfolio company)
asset = 20000000 # Example asset value (e.g., appraised value of the portfolio company)

ltv_ratio = calculate_ltv(loan, asset)

if ltv_ratio is not None:
    print(f"The Loan-to-Value (LTV) ratios is: {ltv_ratio:.2f}%")
else:
    print("Cannot calculate LTV as the asset value is zero.")
