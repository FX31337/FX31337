from .Market import Market
from .Timeframe import Timeframe
from src.handlers.web.WebHandler import WebHandler

class MarketHandler(WebHandler.request):

    def get(self):
        data = {}
        self.write(data)

    def post(self):
        data = {}
        self.write(data)

    def put(self):
        data = {}
        self.write(data)

    def delete(self):
        data = {}
        self.write(data)