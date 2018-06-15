""" Import modules. """
from .Account import Account
from src.handlers.web.WebHandler import WebHandler

"""
" Defines Account web handler.
"""
class AccountHandler(WebHandler.request):
    db = {}

    def head(self, id=None):
        """
        " Quick response without body, but headers.
        """
        try:
            if id:
                self.db[id]
            else:
                self.db
        except KeyError:
            self.set_status(404)
        except Exception:
            self.set_status(500)

    def get(self, id=None):
        """
        " Gets the list of existing accounts.
        " If id is specified, return the specific one.
        """
        try:
            if id:
                result = self.db[id]
            else:
                result = self.db
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
        " Adds a new account.
        """
        try:
            body = self.json_decode(self.request.body)
            key = id or len(self.db)
            self.db[key] = body
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
        " Updates the existing account.
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
        " Deletes the existing account.
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