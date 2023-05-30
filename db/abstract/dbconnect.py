from abc import ABC, abstractmethod


class DbConnection(ABC):

    @staticmethod
    @abstractmethod
    def connect():
        """
        Pull db connection string from env variable
        Create a connection to the database client
        Connect to the database for characters
        Return the connection to the database
        Implement connection-pooling & thread-safety for db connection
        """
        pass
