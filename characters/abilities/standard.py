from random import randint
from characters.abstract.strategy import Strategy


class StandardAbilities(Strategy):

    def __init__(self):
        self.strength = {"score": Assign.roll_4d6(), "modifier": 0}
        self.dexterity = {"score": Assign.roll_4d6(), "modifier": 0}
        self.constitution = {"score": Assign.roll_4d6(), "modifier": 0}
        self.intelligence = {"score": Assign.roll_4d6(), "modifier": 0}
        self.wisdom = {"score": Assign.roll_4d6(), "modifier": 0}
        self.charisma = {"score": Assign.roll_4d6(), "modifier": 0}

    def configure(self, character):
        character.set_abilities(StandardAbilities())

        return character


class Assign:
    """
    For standard assignment, you roll a 6 sided die 4 times
    You then drop the lowest roll
    And then sum up the remaining values to determine your score
    """

    @staticmethod
    def roll_4d6():
        r1 = randint(1, 6)
        r2 = randint(1, 6)
        r3 = randint(1, 6)
        r4 = randint(1, 6)

        rolls = [r1, r2, r3, r4]
        rolls.remove(min(rolls))

        return sum(rolls)
