from .Market import Market
from .Bar import Bar

class Timeframe(Market):
    # Name of the symbol.
    symbol = None

    # Interval in minutes.
    interval = 1

    # Other variables.
    valid = False

    # Class constructor.
    def __init__(self, symbol, interval):
        self.symbol = symbol
        self.interval = interval
        self.valid = self.valid_tf()

    # Validate timeframe.
    def valid_tf(self):
        pass

    # Get open value of the bar.
    def get_open(self, bar):
        pass

    # Get close value of the bar.
    def get_close(self, bar):
        pass

    # Get highest value of the bar.
    def get_high(self, bar):
        pass

    # Get lowest value of the bar.
    def get_low(self, bar):
        pass

    # Get highest value for the bar range.
    def get_highest(self, bar):
        pass

    # Get lowest value for the bar range.
    def get_lowest(self, bar):
        pass

    # Get volume value of the bar.
    def get_volume(self, bar):
        pass

    # Returns bar's body size in pips.
    def get_body_size(self):
        pass

    # Returns bar's candle size in pips.
    def get_candle_size(self):
        pass

    # Returns bar's range size in pips.
    def get_range_size(self):
        pass

    # Returns bar's tail size in pips.
    def get_tail_size(self):
        pass