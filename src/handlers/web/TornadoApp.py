import tornado.web
from tornado.ioloop import IOLoop

class TornadoApp(tornado.web.Application):

    def __init__(self, handlers):
        tornado.web.Application.__init__(self, handlers)

    def start(self):
        IOLoop.instance().start()

    def listen(self, port):
        super().listen(port)
        return self