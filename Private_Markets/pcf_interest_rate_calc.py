# Calculating Interest rates for a Private Credit Fund

## Calculating Simple Interest Calculation
def calculate_simple_interest(principal, annual_rate, time_in_years):
    """
    Calculates simple interests.

    Args:
        principal (float): The initial amount of the loan/investment.
        annual_rate (float): The annual interest rate (as a decimal, e.g., 0.05 for 5%).
        time_in_years (float): The duration of the loan/investment in years.

    Returns:
        float: The calculated simple interest.
    """
    interest = principal * annual_rate * time_in_years
    return interest

# Example Usage:
principal_amount = 1000000 # $1000000
annual_interest_rate = 0.075 # 7.5%
loan_term_years = 3

simple_interest = calculate_simple_interest(principal_amount, annual_interest_rate, loan_term_years)
print(f"Simple Interest: ${simple_interest:.2f}")

### Compound Interest Calculation
def calculate_compound_interest(principal, annual_rate, compounding_frequency, time_in_years):
    """
    Calculates compound interests.

    Args:
        principal (float): The initial amount of the loan/investment.
        annual_rate (float): The annual interest rate (as a decimal).
        compounding_frequency (int): Number of times interest is compounded per year (e.g., 12 for monthly).
        time_in_years (float): The duration of the loan/investment in years.

    Returns:
        float: The final amount after compounding.
    """
    final_amount = principal * (1 + (annual_rate / compounding_frequency))**(compounding_frequency * time_in_years)
    return final_amount

# Example usage:
principal_amount = 500000 # $500,000
annual_interest_rate = 0.08 # 8%
compounding_periods_per_year = 12 # Monthly Compounding
loan_term_years = 5

final_value = calculate_compound_interest(principal_amount, annual_interest_rate, compounding_periods_per_year, loan_term_years)
interest_earned = final_value - principal_amount
print(f"Final Amount (Compound Interest): ${final_value:.2f}")
print(f"Interest Earned: ${interest_earned:.2f}")

#### Floating Rate of Interest
def calculate_floating_interest(principal, benchmark_rate, spread_bps, time_in_years):
    """
    Calculates interest for a floating rate loan (simplified).

    Args:
        principal (float): The principal amount.
        benchmark_rate (float): The current benchmark rate (e.g., SOFR, as a decimal).
        spread_bps (float): The spread in basis points (e.g., 200 for 2%).
        time_in_years (float): The loan term in years.

    Returns:
        float: The calculated interest for the period.
    """
    # Convert basis points to a decimal
    spread_decimal = spread_bps / 10000
    effective_rate = benchmark_rate + spread_decimal
    interest = principal * effective_rate * time_in_years # Simplified for annual calculation
    return interest

# Example usage (assuming you have a way to get the benchmark rate):
current_sofr = 0.0525 # 5.25%
spread_in_bps = 250 # 250 basis points (2.5%)

floating_interest = calculate_floating_interest(principal_amount, current_sofr, spread_in_bps, loan_term_years)
print(f"Floating Rate Interest (Simplified): ${floating_interest:.2f}")
