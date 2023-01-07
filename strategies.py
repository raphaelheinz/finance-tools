"""
Compare different market strategies
"""

BUYIN = 50000
APY = 1.07
YEARS_HOLDING = 10

def after_tax(amount, tax=0.25):
    return amount*(1-tax)

def buy_and_hold(amount,apy,years):
    return amount*apy**years

def calculate_final_value(buyin,apy,years):
    total_value = buy_and_hold(buyin,apy,years)
    profit_after_tax = after_tax(total_value-buyin)
    return buyin + profit_after_tax

# Option1: Buy and hold
final_value1 = calculate_final_value(BUYIN,APY,YEARS_HOLDING)
print(final_value1)



