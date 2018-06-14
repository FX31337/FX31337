from .Account import Account

from src.handlers.web.WebHandler import WebHandler

class AccountHandler(WebHandler.handler):
    account = None

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