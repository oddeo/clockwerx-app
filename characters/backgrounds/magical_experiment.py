from characters.abstract.strategy import Strategy
from characters.backgrounds.types import Backgrounds

from characters.abilities.types import Abilities


class MagicalExperiment(Strategy):

    def configure(self, character):

        character.set_background(Backgrounds.MAGICAL_EXPERIMENT)

        # ability boost
        character.set_ability_modifier(Abilities.CONSTITUTION, 1)

        # TODO:
        # No way to note special abilities right now, for example, "Touch Telepathy"
        # which allows the character to touch you and understand you for communication
        # as long as you have a language in common with the other character

        return character
