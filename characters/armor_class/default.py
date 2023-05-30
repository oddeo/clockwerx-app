from characters.abstract.strategy import Strategy


class DefaultArmorClass(Strategy):

    def __init__(self):
        self.score = 0
        self.unarmored = 0
        self.light = 0
        self.medium = 0
        self.heavy = 0

    def configure(self, character):
        character.set_armor_class(DefaultArmorClass())

        return character
