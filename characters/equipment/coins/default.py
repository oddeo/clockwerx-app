from characters.abstract.strategy import Strategy


class DefaultCoins(Strategy):

    def __init__(self):
        self.copper = 0
        self.silver = 0
        self.gold = 15
        self.platinum = 0

    def configure(self, character):
        character.set_coins(DefaultCoins())

        return character
