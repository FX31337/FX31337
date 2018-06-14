from src.api.account import Account
from src.api.market import Market

class Trade():
    account = None
    market = None
    orders = []

    def __init__(self, account, market):
        self.account = account
        self.market = market