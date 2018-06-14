from .TornadoApp import TornadoApp
from .TornadoHandler import TornadoHandler

class WebHandler():
    handlers = None
    port = None

    # Define web engine.
    handler = TornadoHandler
    app = TornadoApp

    def __init__(self, handlers, port):
        self.handlers, self.port = handlers, port
        self.app = self.app(handlers)