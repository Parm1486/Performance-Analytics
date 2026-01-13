# Calculate Net Asset Value(NAV) for Private Credit Fund

class PrivateCreditFund:
    def __init__(self, name, total_assets, total_liabilities, outstanding_shares):
        self.name = name
        self.total_assets = total_assets
        self.total_liabilities = total_liabilities
        self.outstanding_shares = outstanding_shares

    def calculate_nav(self):
        """
        Calculates the NAV per share of the fund.
        """
        return self.total_assets - self.total_liabilities

    def calculate_nav_per_share(self):
        """
        Calculates the NAV per share of the fund.
        """
        nav = self.calculate_nav()
        if self.outstanding_shares > 0:
            return nav / self.outstanding_shares
        else:
            return None

# Example usage:
fund_assets = 500000000  # $500 million
fund_liabilities = 50000000 # $50 million
fund_shares = 10000000 # 10 million shares

my_private_credit_fund = PrivateCreditFund("My Credit Fund", fund_assets, fund_liabilities, fund_shares)

nav = my_private_credit_fund.calculate_nav()
nav_per_share = my_private_credit_fund.calculate_nav_per_share()

print(f"Fund Name: {my_private_credit_fund.name}")
print(f"Total Assets: ${fund_assets:,}")
print(f"Total Liabilities: ${fund_liabilities:,}")
print(f"Outstanding Shares: {fund_shares:,}")
print(f"NAV: ${nav:,}")
print(f"NAV per Share: ${nav_per_share: .2f}")    
    
