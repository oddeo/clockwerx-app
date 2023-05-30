from pymongo import MongoClient
from db.abstract.dbconnect import DbConnection
from dotenv import dotenv_values


class MongoDb(DbConnection):
    """
    pymongo client object is thread-safe and has connection-pooling built in.
    If an operation fails because of a network error, ConnectionFailure is raised
    and the client reconnects in the background.
    """

    @staticmethod
    def connect():
        try:
            config = dotenv_values(".env")
            conn_str = config['DB_CONF']
            client = MongoClient(conn_str)
            database = client['pathfinder_characters']

            return database

        except Exception as error:
            raise ConnectionError(error)
