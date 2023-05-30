from characters.abstract.strategy import Strategy
from characters.heritages.types import Heritages


class NoHeritage(Strategy):
    def configure(self, character):
        character.set_heritage(Heritages.NONE)

        """
        This character does not have a heritage.
        """

        return character
