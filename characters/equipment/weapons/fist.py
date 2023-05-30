from characters.abstract.weapons_strategy import WeaponsStrategy
from characters.equipment.weapons.categories import WeaponsCategory
from characters.equipment.weapons.damage import DamageTypes
from characters.equipment.weapons.types import Weapons


class Fist(WeaponsStrategy):

    @property
    def weapon_type(self):
        weapon_type = Weapons.FIST
        return weapon_type

    @property
    def category(self):
        category = WeaponsCategory.UNARMED
        return category

    @property
    def damage(self):
        damage = "1d4"
        return damage

    @property
    def damage_type(self):
        damage_type = DamageTypes.BLUNT
        return damage_type

    @property
    def bulk(self):
        bulk = None
        return bulk

    @property
    def hands(self):
        hands = 1
        return hands

    @property
    def group(self):
        group = "brawling"
        return group

    @property
    def weapon_traits(self):
        weapon_traits = ["agile", "finesse", "nonlethal", "unarmed"]
        return weapon_traits

    def __init__(self):
        self.weapon = {
            "weapon_type": self.weapon_type.value,
            "category": self.category.value,
            "damage": self.damage,
            "damage_type": self.damage_type.value,
            "bulk": self.bulk,
            "hands": self.hands,
            "group": self.group,
            "weapon_traits": self.weapon_traits
        }

    def configure(self, character):
        character.set_weapons(Fist())
        # TODO: Setup payment system for other weapons - "fist" is free

        return character
