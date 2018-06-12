from tornado import httpserver
from tornado import gen
from tornado.ioloop import IOLoop
import tornado.web
from src.storage.SQL import SQLiteStorage

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('Hello, world')

class DataHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('GET - Welcome to the DataHandler!')

    def post(self):
        self.write('POST - Welcome to the DataHandler!')

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/?", MainHandler),
            (r"/api/v1/data/?", DataHandler),
            (r"/api/v1/data/[0-9][0-9][0-9][0-9]/?", DataHandler)
        ]
        tornado.web.Application.__init__(self, handlers)

def main():
    #db = SQLiteStorage.SQLLiteStorage()

    # Verify the database exists and has the correct layout
    #db.verifyDatabase()

    app = Application()
    app.listen(9999)
    IOLoop.instance().start()

if __name__ == '__main__':
    main()