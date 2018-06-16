""" Import modules. """
import tornado.web
from tornado.ioloop import IOLoop
from tornado.log import gen_log as logger

"""
" Defines Tornado's app.
"""
class TornadoApp(tornado.web.Application):

    def __init__(self, handlers):
        tornado.web.Application.__init__(self, handlers)

    def start(self):
        IOLoop.instance().start()

    def listen(self, port):
        super().listen(port)
        return self

    def log(self, severity, *args):
        return {
            'info': logger.info,
            'warning': logger.warning,
            'error': logger.error,
        }.get(severity)(*args)