from src.api.symbol import Symbol

class Market(Symbol.Symbol):
    # Pointer to symbol instance.
    symbol = None

    # Pip precision
    pip_digits = 0

    def __init__(self, symbol):
        self.symbol = symbol

    # Get a pip digit precision.
    def get_pip_digits(self):
        return 2 if self.get_digits < 4 else 4

    # Get a pip value.
    def get_pip_value(self):
        return 10 >> self.get_pip_digits
