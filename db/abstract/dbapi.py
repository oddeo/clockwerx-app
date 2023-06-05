from abc import ABC, abstractmethod
from db.abstract.dbconnect import DbConnection


class DbApi(ABC):
    # uses the Bridge Design Pattern to inject database connection using interface

    @classmethod
    @abstractmethod
    def save(cls, item, connection: DbConnection) -> str:
        pass

    @classmethod
    @abstractmethod
    def retrieve(cls, item_id: str, connection: DbConnection) -> dict:
        pass

    @classmethod
    @abstractmethod
    def remove(cls, item_id: str, connection: DbConnection) -> int:
        pass

