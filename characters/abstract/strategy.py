from abc import ABC, abstractmethod


class Strategy(ABC):

    @abstractmethod
    def configure(self, character):
        pass
