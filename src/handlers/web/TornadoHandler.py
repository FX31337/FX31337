import tornado.web
from tornado import gen, httpserver
from tornado.escape import json_encode, json_decode
from tornado.log import gen_log as logger

"""
" Defines Tornado's web handler.
"""
class TornadoHandler(tornado.web.RequestHandler):
    handlers = []
    methods = {'HEAD', 'GET', 'POST', 'PUT', 'DELETE', 'OPTIONS'}

    def options(self, id=None):
        """
        " Gets list of communication options available.
        """
        allow = []
        for method in self.methods:
            if method.lower() in dir(self):
                allow.append(method)
        self.set_header('Allow', ",".join(allow))

    def json_encode(self, obj):
        """
        " Encodes JSON value.
        """
        return json_encode(obj)

    def json_decode(self, value):
        """
        " Decodes JSON value.
        """
        return json_decode(value)

    def write_error(self, status_code, **kwargs):
        """
        " Overrides implement custom error pages.
        " @see: RequestHandler.write_error
        """
        print(dir(kwargs))
        err_type = "Unknown"
        reason = "Unknown"

        if "exc_info" in kwargs:
            # Refs: https://stackoverflow.com/a/30029019
            e = kwargs["exc_info"][1]
            err_type = e.__class__.__name__
            if isinstance(e, tornado.web.HTTPError):
                reason = e.reason
            else:
                reason = str(e)
        result = {
            'error': {
                'type': err_type,
                'message': reason,
            }
        }
        self.write(result)

    def log(self, type, *args):
        {
            'info': logger.info
        }.get(type)(*args)