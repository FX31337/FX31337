#!/usr/bin/env python3

""" Import handlers. """
from src.handlers.web.WebHandler import WebHandler
from src.api.account.AccountHandler import AccountHandler
from src.api.market.MarketHandler import MarketHandler
from src.api.node.NodeHandler import NodeHandler
from src.api.platform.PlatformHandler import PlatformHandler
from src.api.profile.ProfileHandler import ProfileHandler
from src.api.provider.ProviderHandler import ProviderHandler
from src.api.provider.ProviderListHandler import ProviderListHandler
from src.api.status.StatusHandler import StatusHandler
from src.api.strategy.StrategyHandler import StrategyHandler
from src.api.symbol.SymbolHandler import SymbolHandler
from src.api.trade.TradeHandler import TradeHandler

"""
" Defines the main web application class.
"""
class Application(WebHandler):
    handlers = [
        (r"/?", StatusHandler),
        (r"/api/account/?", AccountHandler),
        (r"/api/account/([0-9a-z]+)/?", AccountHandler),
        (r"/api/market/?", MarketHandler),
        (r"/api/market/([0-9a-z]+)/?", MarketHandler),
        (r"/api/node/?", NodeHandler),
        (r"/api/node/([0-9a-z]+)/?", NodeHandler),
        (r"/api/platform/?", PlatformHandler),
        (r"/api/platform/([0-9a-z]+)/?", PlatformHandler),
        (r"/api/profile/?", ProfileHandler),
        (r"/api/profile/([0-9a-z]+)/?", ProfileHandler),
        (r"/api/provider/?", ProviderHandler),
        (r"/api/provider/([0-9a-z]+)/?", ProviderHandler),
        (r"/api/provider/list/(type)/?", ProviderListHandler),
        (r"/api/status/?", StatusHandler),
        (r"/api/status/ping/?", StatusHandler),
        (r"/api/symbol/?", SymbolHandler),
        (r"/api/symbol/([0-9a-zA-Z]+)/?", SymbolHandler),
        (r"/api/trade/?", TradeHandler),
        (r"/api/trade/([0-9]+)/?", TradeHandler),
    ]

def main():
    """
    " Defines the main function.
    """
    Application().listen(9999).start()

"""
" Defines the main entry point of the program.
"""
if __name__ == '__main__':
    main()