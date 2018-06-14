class Symbol():

    # Name of the symbol pair.
    name = ''

    # Other variables.
    digits = 0
    trade_contract_size = 0
    min_lot, max_lot = 0, 0

    # Latest ask and bid price.
    ask, bid = 0, 0

    # Datetime of the price last update.
    datetime = 0

    # Value of pip size.
    pip_size = 1/100
    tick_size = None

    def __init__(self, name):
        self.name = name
        pass

    # Get ask price (best buy offer).
    def get_ask(self):
        # @todo
        pass

    # Get bid price (best sell offer).
    def get_bid(self):
        # @todo
        pass

    # Get the point size in the quote currency.
    # The smallest digit of price quote.
    def get_point_size(self):
        # @todo
        pass

    # Get count of digits after decimal point for the symbol price.
    def get_digits(self):
        # @todo
        pass

    # Get a pip size.
    def get_pip_size(self):
        # @todo
        pass

    # Get a contract lot size in the base currency.
    def get_trade_contract_size(self):
        # @todo
        pass

    # Get a minimum permitted amount of a lot/volume for a deal.
    def get_min_lot(self):
        # @todo
        pass

    # Get a maximum permitted amount of a lot/volume for a deal.
    def get_max_lot(self):
        # @todo
        pass

    # Get a lot/volume step for a deal.
    def get_lot_step(self):
        # @todo
        pass

    # Get an order freeze level in points.
    def get_freeze_level(self):
        # Freeze level is a value that determines the price band,
        # within which the order is considered as 'frozen' (prohibited to change).
        #
        # If the execution price lies within the range defined by the freeze level,
        # the order cannot be modified, cancelled or closed.
        # The possibility of deleting a pending order is regulated by the FreezeLevel.
        # @todo
        pass

    # Get a tick size in points.
    # It is a minial price change in points.
    def get_tick_size(self):
        # @todo
        pass

    # Get the current real spread.
    def get_spread(self):
        return (self.ask - self.bid) * pow(10, self.digits)

    # Get summary volume of current session deals.
    def get_session_volume(self):
        # @todo
        pass

    # Updates the latest price.
    def update_price(self):
        # @todo
        #self.ask =
        #self.bid =
        pass