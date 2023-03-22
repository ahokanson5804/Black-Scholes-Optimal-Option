import yfinance as yf
import pandas as pd
import numpy as np
import scipy.stats as si

def black_scholes(S, K, T, r, sigma, option_type='call'):
    d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = (np.log(S / K) + (r - 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    
    if option_type == 'call':
        price = (S * si.norm.cdf(d1, 0.0, 1.0) - K * np.exp(-r * T) * si.norm.cdf(d2, 0.0, 1.0))
    elif option_type == 'put':
        price = (K * np.exp(-r * T) * si.norm.cdf(-d2, 0.0, 1.0) - S * si.norm.cdf(-d1, 0.0, 1.0))
        
    return price

def get_options_data(ticker, exp_date):
    stock = yf.Ticker(ticker)
    option_chain = stock.option_chain(exp_date)
    return option_chain.calls, option_chain.puts

def find_best_option(ticker, exp_dates, risk_free_rate=0.02, option_type='call'):
    S = yf.download(ticker, progress=False)['Close'][-1]
    
    best_option = {
        'strike': 0,
        'expiration': '',
        'gain': 0
    }
    
    for exp_date in exp_dates:
        calls, puts = get_options_data(ticker, exp_date)
        
        for index, row in calls.iterrows():
            K = row['strike']
            T = (pd.to_datetime(exp_date) - pd.to_datetime('today')).days / 365
            sigma = row['impliedVolatility']
            option_price = black_scholes(S, K, T, risk_free_rate, sigma, option_type)
            
            gain = option_price - row['lastPrice']
            
            if gain > best_option['gain']:
                best_option['strike'] = K
                best_option['expiration'] = exp_date
                best_option['gain'] = gain
    
    return best_option

ticker = 'BBBY'
exp_dates = ['2023-04-21', '2023-04-28', '2023-05-19', '2023-06-16']
best_call_option = find_best_option(ticker, exp_dates)

print(f"Best call option for {ticker}:")
print(f"Strike price: {best_call_option['strike']}")
print(f"Expiration date: {best_call_option['expiration']}")
print(f"Expected gain: {best_call_option['gain']}")
