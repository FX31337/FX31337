import tornado.web
from tornado import gen, httpserver
from tornado.escape import json_encode, json_decode

class TornadoHandler(tornado.web.RequestHandler):
    handlers = []

    def get(self):
        self.write('Hello, world')

    def post(self):
        self.write('POST - Welcome to the DataHandler!')

    def json_encode(self, obj):
        return json_encode(obj)

    def json_decode(self, value):
        return json_decode(value)