""" Import modules. """
from .ProviderHandler import ProviderHandler
from src.handlers.web.WebHandler import WebHandler

"""
" Defines ProviderList web handler.
"""
class ProviderListHandler(ProviderHandler):

    def get(self, field):
        """
        " Gets the list of available providers.
        """
        result = {
            'type': [*self.providers],
        }.get(field)
        self.write({field: result})