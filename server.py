#!/usr/bin/env python3

# Import handlers.
from src.handlers.web.WebHandler import WebHandler
from src.api.account.AccountHandler import AccountHandler
from src.api.market.MarketHandler import MarketHandler
from src.api.node.NodeHandler import NodeHandler
from src.api.platform.PlatformHandler import PlatformHandler
from src.api.profile.ProfileHandler import ProfileHandler
from src.api.provider.ProviderHandler import ProviderHandler
from src.api.status.StatusHandler import StatusHandler
from src.api.symbol.SymbolHandler import SymbolHandler
from src.api.trade.TradeHandler import TradeHandler

from tornado import httpserver
from tornado import gen
from tornado.ioloop import IOLoop
import tornado.web

class Application(WebHandler.app):
    handlers = [
        (r"/?", StatusHandler),
        (r"/api/account/?", AccountHandler),
        (r"/api/market/?", MarketHandler),
        (r"/api/node/?", NodeHandler),
        (r"/api/platform/?", PlatformHandler),
        (r"/api/profile/?", ProfileHandler),
        (r"/api/provider/?", ProviderHandler),
        (r"/api/status/?", StatusHandler),
        (r"/api/symbol/?", SymbolHandler),
        (r"/api/trade/?", TradeHandler),
    ]

    def __init__(self, handlers=None):
        super().__init__(handlers or self.handlers)

def main():
    Application().listen(9999).start()

if __name__ == '__main__':
    main()