from abc import abstractmethod
from characters.abstract.strategy import Strategy


class ArmorStrategy(Strategy):

    @property
    @abstractmethod
    def armor_type(self):
        pass

    @property
    @abstractmethod
    def category(self):
        pass

    @property
    @abstractmethod
    def ac_bonus(self):
        pass

    @property
    @abstractmethod
    def dex_cap(self):
        pass

    @property
    @abstractmethod
    def check_penalty(self):
        pass

    @property
    @abstractmethod
    def speed_penalty(self):
        pass

    @property
    @abstractmethod
    def strength(self):
        pass

    @property
    @abstractmethod
    def bulk(self):
        pass

    @property
    @abstractmethod
    def group(self):
        pass

    @property
    @abstractmethod
    def armor_traits(self):
        pass

    @abstractmethod
    def configure(self, character):
        pass
