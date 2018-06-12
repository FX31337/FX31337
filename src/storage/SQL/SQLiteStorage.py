from . import SQLBase as base
import sqlite3 as sqlite

class SQLLiteStorage(base.SQLBase):

    def __init__(self):
        super()

    def verifyDatabase(self):
        conn = sqlite.connect('data.db')
        c = conn.cursor()
        try:
            c.execute('SELECT * FROM data')
            print('Table already exists')
        except:
            print('Creating table \'data\'')
            c.execute('CREATE TABLE data (\
                id text,\
                datetime text)')
            print('Successfully created table \'data\'')
        conn.commit()
        conn.close()