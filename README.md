# Black-Scholes-Optimal-Option

This repository provides a Python script that uses the Black-Scholes Model to find the option with the highest likelihood of positive gains for a specified stock ticker and expiration dates. The script retrieves options chain data for the specified ticker and calculates the expected gains using the Black-Scholes formula for each option. It then returns the strike price and expiration date of the option with the highest expected gain.

Installation - copy git command bellow

git clone https://github.com/ahokanson5804/Black-Scholes-Optimal-Option.git

Install these packages: 

    pip install yfinance pandas numpy scipy

Usage:

Open the <black_scholes_optimal_option.py> file and modify the 'ticker' and 'exp_dates' variables as needed. Only analyses one ticker at a time.

    ticker = 'AAPL'
    exp_dates = ['2023-04-21', '2023-05-19', '2023-06-16']
    
The script will output the best call option, including the strike price, expiration date, and expected gain.


    Best call option for AAPL:
    Strike price: 150.0
    Expiration date: 2023-04-21
    Expected gain: 3.4823537159835047



Notes:

The script currently only considers call options. You can modify the option_type argument in the find_best_option function to analyze put options as well.
The risk-free rate is set to 0.02 (2%) by default. You can adjust it as needed.
The script calculates the time to expiration (T) as the number of days divided by 365. This is a simplification, and you may want to adjust this calculation for more accurate results.

License:

This project is licensed under the MIT License. See the [LICENSE](https://chat.openai.com/LICENSE) file for details.
