import random

class RateLimitError(Exception):
    pass

def get_price(exchange, symbol):
    # Mock function for getting prices
    mock_prices = {
        'BTC-USD': 30000 + random.uniform(-50, 50),
        'ETH-USD': 2000 + random.uniform(-10, 10),
        'LTC-USD': 100 + random.uniform(-5, 5)
    }
    if random.randint(0, 50) == 0:
        raise RateLimitError()
    return mock_prices.get(symbol)

def simulate_trade(symbol, buy_price, sell_price, percent_gain):
    print(f"[TRADE] Simulating {symbol} arbitrage: Buy at {buy_price:.2f}, Sell at {sell_price:.2f}, Gain: {percent_gain:.2f}%")

def log_opportunity(symbol, buy_price, sell_price, percent_gain):
    print(f"[INFO] {symbol}: Buy {buy_price:.2f} / Sell {sell_price:.2f} --> Spread: {percent_gain:.2f}%")
