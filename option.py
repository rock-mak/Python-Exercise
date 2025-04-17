import numpy as np
from scipy.stats import norm

def bsc(S,X,T,r,sigma):
    d1 = (np.log(S/X)+(r+0.5*sigma**2)*T)/(sigma*np.sqrt(T))
    d2 = d1 - sigma*np.sqrt(T)
    
    call_price = (S*norm.cdf(d1)-X*np.exp(-r*T)*norm.cdf(d2))
    return call_price

S = 306.24
X = 307
T = 0.083 #in year
r = 0.05
sigma = 0.2 #asset 20%

call_option_price = bsc(S,X,T,r,sigma)

print(f"the price of the call option is: ${call_option_price:.2f}")


def is_option_profitable(strike_price, current_price, premium_paid, delta, theta, days_to_expiration):
    
    intrinsic_value = max(0, current_price - strike_price)
    profit = intrinsic_value - premium_paid
    time_decay = theta * days_to_expiration
    adjusted_profit = profit - time_decay
    
    if adjusted_profit > 0:
        return True, adjusted_profit
    else:
        return False, adjusted_profit
        
strike_price = float(input("Strike price: "))
current_price = float(input("Current price: "))
premium_paid = 3.0
delta = float(input("Delta: "))
theta = float(input("Theta: "))
days_to_expiration = int(input("Days to expiration: "))
profitable, profit_amount = is_option_profitable(strike_price, current_price, premium_paid, delta, theta,days_to_expiration)
print()
if profitable:
    print(f"Profit of the option is ${profit_amount:.2f}")
else:
    print(f"Not profitable with loss ${-profit_amount:.2f}")
