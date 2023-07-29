from abc import ABCMeta, abstractmethod
from characters.character import Character


class Roll(metaclass=ABCMeta):

    def __init__(self, player: Character, **kwargs):
        self.player = Character.cast(player)
        self.kwargs = kwargs

    @abstractmethod
    def start(self) -> dict:
        pass
