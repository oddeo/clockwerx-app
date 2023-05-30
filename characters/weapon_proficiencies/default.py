from characters.abstract.strategy import Strategy


class DefaultWeaponProficiencies(Strategy):

    def __init__(self):
        self.unarmed = 0
        self.simple = 0
        self.martial = 0
        self.advanced = 0

    def configure(self, character):
        character.set_weapon_proficiencies(DefaultWeaponProficiencies())

        return character
