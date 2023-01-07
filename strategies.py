"""
Compare different market strategies
"""

DEPOT_VALUE = 50000
APY = 1.07
YEARS_HOLDING = 30

def after_tax(amount, tax=0.25):
    return amount*(1-tax)

def buy_and_hold(amount,apy,years):
    return amount*apy**years

def buy_and_hold_after_tax(depot_initial,apy,years,buy_in=None):
    if buy_in==None: buy_in=depot_initial
    total_value = buy_and_hold(depot_initial,apy,years)
    profit_after_tax = after_tax(total_value-buy_in)
    return buy_in + profit_after_tax

def sell_per_year(depot_initial,apy,years,sell_per_year):
    buy_in = depot_initial
    total_value = depot_initial
    for i in range(years-1):
        total_value = buy_and_hold(total_value,apy,1)
        profit_after_tax = after_tax(sell_per_year)
        buy_in += profit_after_tax
        total_value = (total_value-sell_per_year) + profit_after_tax
    return buy_and_hold_after_tax(total_value,apy,1,buy_in)

# Option 1: Buy and hold
final_value1 = buy_and_hold_after_tax(DEPOT_VALUE,APY,YEARS_HOLDING)
print('Buy and hold: {:.2f}'.format(final_value1))

# Option 2: Increase buy_in every year
# Sell SELL_PER_YEAR $ per year, tax it and rebuy shares
SELL_PER_YEAR = 1000
final_value2 = sell_per_year(DEPOT_VALUE,APY,YEARS_HOLDING,SELL_PER_YEAR)
print('Sell {}$ per year: {:.2f}'.format(SELL_PER_YEAR,final_value2))


