import time
from utils.helpers import get_price, simulate_trade, log_opportunity, RateLimitError

class SimpleArbitrageBot:
    def __init__(self):
        self.symbols_to_watch = ['BTC-USD', 'ETH-USD', 'LTC-USD']
        self.scan_interval = 5  # seconds
        self.successful_calls = 0
        self.minimum_profit_threshold = 0.3  # percent
        self.trading_fee_percent = 0.1  # per trade
        self.estimated_slippage_percent = 0.05  # estimate

    def run(self):
        while True:
            for symbol in self.symbols_to_watch:
                try:
                    buy_price = get_price('exchange_a', symbol)
                    sell_price = get_price('exchange_b', symbol)

                    if buy_price is None or sell_price is None:
                        continue

                    spread = sell_price - buy_price
                    percent_gain = (spread / buy_price) * 100

                    total_cost_percent = (self.trading_fee_percent * 2) + self.estimated_slippage_percent

                    if percent_gain >= (total_cost_percent + self.minimum_profit_threshold):
                        simulate_trade(symbol, buy_price, sell_price, percent_gain)
                    else:
                        log_opportunity(symbol, buy_price, sell_price, percent_gain)

                    self.successful_calls += 1
                    if self.successful_calls >= 3 and self.scan_interval > 5:
                        self.scan_interval -= 1
                        self.successful_calls = 0

                except RateLimitError:
                    print(f"[WARNING] 429 Rate Limit detected. Slowing down to 30 seconds.")
                    self.scan_interval = 30
                    self.successful_calls = 0
                except Exception as e:
                    print(f"[ERROR] Unexpected error for {symbol}: {str(e)}")

                time.sleep(self.scan_interval)
