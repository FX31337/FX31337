""" Import modules. """
from src.api.provider.Provider import Provider
from binance.client import Client
from binance.exceptions import BinanceAPIException, BinanceWithdrawException
from binance.websockets import BinanceSocketManager

"""
" Implements Binance Exchange API service.
" @see: https://github.com/sammchardy/python-binance
"""
class BinanceProvider(Client, Provider):
    # API Key and Secret.
    api_key, api_secret = None, None

    # Get current account information.
    account = {}

    order_type_buy = Client.SIDE_BUY
    order_type_sell = Client.SIDE_SELL
    order_type_market = Client.ORDER_TYPE_MARKET

    _intervals = {
        'M1': Client.KLINE_INTERVAL_1MINUTE,
        'M2': Client.KLINE_INTERVAL_3MINUTE,
        'M3': Client.KLINE_INTERVAL_3MINUTE,
        'M5': Client.KLINE_INTERVAL_5MINUTE,
        'M15': Client.KLINE_INTERVAL_15MINUTE,
        'M30': Client.KLINE_INTERVAL_30MINUTE,
        'H1': Client.KLINE_INTERVAL_1HOUR,
        'H2': Client.KLINE_INTERVAL_2HOUR,
        'H4': Client.KLINE_INTERVAL_4HOUR,
        'H6': Client.KLINE_INTERVAL_6HOUR,
        'H8': Client.KLINE_INTERVAL_8HOUR,
        'H12': Client.KLINE_INTERVAL_12HOUR,
        'D1': Client.KLINE_INTERVAL_1DAY,
        'D3': Client.KLINE_INTERVAL_3DAY,
        'W1': Client.KLINE_INTERVAL_1WEEK,
        'MN1': Client.KLINE_INTERVAL_1MONTH,
    }

    def __init__(self, data):
        """
        " Initialize Binance's Client API.
        """
        try:
            self.api_key = data["api_key"]
            self.api_secret = data["api_secret"]
        except Exception as e:
            raise e
        else:
            super().__init__(self.api_key, self.api_secret)
            self.update_account()

    def update_account(self):
        """
        " Retrieves and updates the current account information.
        """
        self.account = self.get_account()

    def getMarketDepth(self, symbol):
        return client.get_order_book(symbol)

    # Place a test market buy order.
    def createOrderTest(self, symbol, side, type, quantity):
        return client.create_test_order(symbol, side, type, quantity)

    # Place an actual order.
    def createOrder(self, symbol, side, type, quantity):
        return client.create_order(symbol, side, type, quantity)

    # Place a withdrawal.
    def placeWithdrawal(self, asset, address, amount):
        try:
            result = client.withdraw(asset, address, amount)
        except BinanceAPIException as e:
            print(e)
        except BinanceWithdrawException as e:
            print(e)
        else:
            print("Success")

    # Get list of withdrawals.
    def getWithdrawalHistory(self, asset=None):
        if asset:
            # Fetch list of asset withdrawals.
            return client.get_withdraw_history(asset)
        else:
            # Fetch list of withdrawals.
            return client.get_withdraw_history()

    # Start aggregated trade websocket.
    def start_aggtrade_socket(self, symbol):
        bm = BinanceSocketManager(client)
        bm.start_aggtrade_socket(symbol, process_message)
        bm.start()

    # Get historical kline data from any date range.
    def getKlines(self, symbol, interval, date_range):
        # Fetch klines.
        klines = client.get_historical_klines(symbol, interval, date_range)