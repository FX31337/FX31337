from .TornadoApp import TornadoApp
from .TornadoHandler import TornadoHandler

"""
" Defines a web handler.
"""
class WebHandler(TornadoApp):
    handlers = None

    # Define web engine.
    request = TornadoHandler

    def __init__(self, handlers=[]):
        super().__init__(self.handlers + handlers)