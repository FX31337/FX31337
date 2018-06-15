""" Import modules. """
from .Provider import Provider
from src.handlers.web.WebHandler import WebHandler

""" Import supported providers. """
from src.providers.exchange.Binance.BinanceProvider import BinanceProvider

"""
" Defines Provider web handler.
"""
class ProviderHandler(WebHandler.request):
    db = {}
    providers = {
        'Binance': BinanceProvider,
    }

    def head(self, id=None):
        """
        " Quick response without body, but headers.
        """
        try:
            self.db[id] if id else self.db
        except KeyError:
            self.set_status(404)
        except Exception:
            self.set_status(500)

    def get(self, id=None):
        """
        " Gets the list of existing providers.
        " If id is specified, return the specific one.
        """
        try:
            result = self.db[id] if id else self.db
        except KeyError as e:
            self.set_status(404)
            result = {
                'error': {
                    'type': e.__class__.__name__,
                    'message': 'Cannot find: ' + str(e),
                }
            }
        except Exception as e:
            self.set_status(500)
            result = {
                'error': {
                    'type': e.__class__.__name__,
                    'message': str(e),
                }
            }
        self.write(result)

    def post(self, id=None):
        """
        " Adds a new provider.
        """
        try:
            body = self.json_decode(self.request.body)
            provider = self.providers.get(body["type"])
            key = id or len(self.db)
            if provider:
                self.db[key] = provider(body)
            else:
                raise ValueError(
                    "Unknown provider '{}'! Supported: {}".format(
                        body["type"],
                        ",".join(self.providers)
                    )
                )
        except KeyError as e:
            self.set_status(404)
            result = {
                'error': {
                    'type': e.__class__.__name__,
                    'message': 'Missing ' + str(e),
                }
            }
        except Exception as e:
            self.set_status(500)
            result = {
                'error': {
                    'type': e.__class__.__name__,
                    'message': str(e),
                }
            }
        else:
            result = {'success': True}
        self.write(result)

    def put(self, id=None):
        """
        " Updates the existing provider.
        """
        try:
            result = self.db[id]
            body = self.json_decode(self.request.body)
            self.db[id] = body
        except KeyError as e:
            self.set_status(404)
            result = {
                'error': {
                    'type': 'NotFound',
                    'message': 'Cannot find: ' + str(e),
                }
            }
        except Exception as e:
            self.set_status(500)
            result = {
                'error': {
                    'type': e.__class__.__name__,
                    'message': str(e),
                }
            }
        else:
            result = {'success': True}
        self.write(result)

    def delete(self, id):
        """
        " Deletes the existing provider.
        """
        try:
            del self.db[id]
        except KeyError as e:
            self.set_status(404)
            result = {
                'error': {
                    'type': 'NotFound',
                    'message': 'Cannot find: ' + str(e),
                }
            }
        except Exception as e:
            self.set_status(500)
            result = {
                'error': {
                    'type': e.__class__.__name__,
                    'message': str(e),
                }
            }
        else:
            result = {'success': True}
        self.write(result)