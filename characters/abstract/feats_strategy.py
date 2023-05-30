from abc import abstractmethod
from characters.abstract.strategy import Strategy


class FeatsStrategy(Strategy):

    @property
    @abstractmethod
    def feat_level(self):
        pass

    @abstractmethod
    def minimum_level(self, character):
        pass

    @abstractmethod
    def minimum_prerequisites(self, character):
        pass

    @abstractmethod
    def configure(self, character):
        pass
