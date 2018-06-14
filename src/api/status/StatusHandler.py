from src.handlers.web.WebHandler import WebHandler

class StatusHandler(WebHandler.handler):

    def get(self):
        data = self.status()
        self.write(data)

    def post(self):
        data = self.status()
        self.write(data)

    def put(self):
        data = {}
        self.write(data)

    def delete(self):
        data = {}
        self.write(data)

    def status(self):
        return {'status': 'active'}