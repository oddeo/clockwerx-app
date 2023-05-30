from characters.abstract.strategy import Strategy
from characters.builder.proficiency_types import Proficiencies


class DefaultPerception(Strategy):

    def __init__(self):
        self.score = 0
        self.proficiency = 0
        self.item = ""
        self.senses = []

    def configure(self, character):
        character.set_perception(DefaultPerception())
        character.set_perception_proficiency(Proficiencies.TRAINED)
        character.set_perception_score(character.abilities['wisdom']['modifier'] + self.proficiency)

        return character
