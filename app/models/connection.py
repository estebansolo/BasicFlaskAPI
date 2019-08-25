import os
from mysql.connector import connect, Error as mysql_error

class DBConnection(object):
    _instance = None
    class Singleton:
        def __init__(self):
            self.connection = connect(
                host=os.environ['MYSQL_HOST'],
                user=os.environ['MYSQL_USER'],
                password=os.environ['MYSQL_PASSWORD'],
                database=os.environ['MYSQL_DATABASE']
            )

            self.cursor = self.connection.cursor()

    def __init__(self):
        if DBConnection._instance is None:
            DBConnection._instance = DBConnection.Singleton()

    def __getattr__(self, attr):
        return getattr(self._instance, attr)

    def __setattr__(self, attr, value):
        return setattr(self._instance, attr, value)


class Manager:
    @property
    def table(self):
        return self._table


    @table.setter
    def table(self, value):
        self._table = value


    def get_connection(self):
        return DBConnection().cursor


    def select(self, fields=[]):
        return ', '.join(fields)


    def execute(self, query=''):
        if query == '':
            return {'error': {'message': 'Query string not defined'}}

        cursor = self.get_connection()

        cursor.execute(query)
        rows = cursor.fetchall()
        keys = cursor.column_names
        return [{key: value for key, value in zip(keys, row)} for row in rows]
