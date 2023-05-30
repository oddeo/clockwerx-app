from characters.abstract.strategy import Strategy


class DefaultAbilities(Strategy):

    def __init__(self):
        self.strength = {"score": 10, "modifier": 0}
        self.dexterity = {"score": 10, "modifier": 0}
        self.constitution = {"score": 10, "modifier": 0}
        self.intelligence = {"score": 10, "modifier": 0}
        self.wisdom = {"score": 10, "modifier": 0}
        self.charisma = {"score": 10, "modifier": 0}

    def configure(self, character):
        character.set_abilities(DefaultAbilities())

        return character
