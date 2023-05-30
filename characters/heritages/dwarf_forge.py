from characters.abstract.strategy import Strategy
from characters.heritages.types import Heritages


class ForgeDwarf(Strategy):
    def configure(self, character):
        character.set_heritage(Heritages.DWARF_FORGE)

        """
        You have a remarkable adaptation to hot environments from ancestors who inhabited
        blazing deserts or volcanic chambers beneath the earth. This grants you fire resistance
        equal to half your level (minimum 1), and you treat environmental heat effects as
        if they were one step less extreme (incredible heat becomes extreme, extreme heat
        becomes severe, and so on).
        """

        return character
