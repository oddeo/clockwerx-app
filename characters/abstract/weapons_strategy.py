from abc import abstractmethod
from characters.abstract.strategy import Strategy


class WeaponsStrategy(Strategy):

    @property
    @abstractmethod
    def weapon_type(self):
        pass

    @property
    @abstractmethod
    def category(self):
        pass

    @property
    @abstractmethod
    def damage(self):
        pass

    @property
    @abstractmethod
    def damage_type(self):
        pass

    @property
    @abstractmethod
    def bulk(self):
        pass

    @property
    @abstractmethod
    def hands(self):
        pass

    @property
    @abstractmethod
    def group(self):
        pass

    @property
    @abstractmethod
    def weapon_traits(self):
        pass

    @abstractmethod
    def configure(self, character):
        pass
