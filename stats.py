
def calculate(value: int, gain: float, tax: float = 0.25):
    initial_value = value // gain
    gain_value = value - initial_value
    gain_after_tax = gain_value * (1-tax)
    tax_value = gain_value * tax 
    breakeven_after_sell = 1-((value-tax_value)/value)

    print(f'initial value ($): {initial_value}')
    print(f'current value ($): {value}')
    print(f'gain (%): {gain}')
    print('-'*30)
    print(f'gain ($): {gain_value}')
    print(f'gain after tax ($): {gain_after_tax}')
    print(f'tax ($): {tax_value}')
    print('-'*30)
    print(f'breakeven after sell (%): {round(breakeven_after_sell,3)}')


gain = 50 # percentage
value = 150
tax = 0.25

calculate(value, 1+gain/100, tax)

