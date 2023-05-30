from characters.abstract.strategy import Strategy
from characters.saving_throws.types import SavingThrows


class DefaultSavingThrows(Strategy):

    def __init__(self):
        self.fortitude = {"score": 0, "proficiency": 0}
        self.reflex = {"score": 0, "proficiency": 0}
        self.will = {"score": 0, "proficiency": 0}

    def configure(self, character):
        character.set_saving_throws(DefaultSavingThrows())
        character.set_saving_throws_score(SavingThrows.FORTITUDE, character.abilities['constitution']['modifier'])
        character.set_saving_throws_score(SavingThrows.REFLEX, character.abilities['dexterity']['modifier'])
        character.set_saving_throws_score(SavingThrows.WILL, character.abilities['wisdom']['modifier'])

        return character
