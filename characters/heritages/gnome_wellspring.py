from characters.abstract.strategy import Strategy
from characters.heritages.types import Heritages


class WellspringGnome(Strategy):
    def configure(self, character):
        character.set_heritage(Heritages.GNOME_WELLSPRING)

        # TODO: Need to have spell types
        # TODO: Spells have their own levels
        # TODO: Cantrip is a special type of spell that does not use spell slots
        """
        Choose Arcane, Divine, or Occult (spell types)
        A Cantrip is heightened to a spell level = 1/2 your level (rounded up)
        Whenever you gain a primal innate spell from a known ancestry feat
        change its tradition from primal to your chosen tradition
        """

        return character
