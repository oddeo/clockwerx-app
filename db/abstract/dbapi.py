from abc import ABC, abstractmethod
from db.abstract.dbconnect import DbConnection


class DbApi(ABC):
    # uses the Bridge Design Pattern to inject database connection using interface

    @classmethod
    @abstractmethod
    def save_character(cls, character, connection: DbConnection) -> str:
        """
        Save changes to character or create new if one does not exist w same id
        return str: character_id
        """
        pass

    @classmethod
    @abstractmethod
    def retrieve_character(cls, character_id: str, connection: DbConnection) -> dict:
        """
        Retrieve a dictionary repr of character by str character_id
        return dict: character | {"character_id": character_id,"database_result": "record_not_found"}
        """
        pass

    @classmethod
    @abstractmethod
    def remove_character(cls, character_id: str, connection: DbConnection) -> int:
        """
        Delete a character by str character_id
        return int: deleted count
        """
        pass

