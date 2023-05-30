from characters.abstract.armor_strategy import ArmorStrategy
from characters.equipment.armor.categories import ArmorCategory
from characters.equipment.armor.types import Armor
from characters.equipment.armor.utils import calculate_ac


class NoArmor(ArmorStrategy):

    @property
    def armor_type(self):
        armor_type = Armor.NO_ARMOR
        return armor_type

    @property
    def category(self):
        category = ArmorCategory.UNARMORED
        return category

    @property
    def ac_bonus(self):
        ac_bonus = 0
        return ac_bonus

    @property
    def dex_cap(self):
        dex_cap = 99
        return dex_cap

    @property
    def check_penalty(self):
        check_penalty = 0
        return check_penalty

    @property
    def speed_penalty(self):
        speed_penalty = 0
        return speed_penalty

    @property
    def strength(self):
        strength = 0
        return strength

    @property
    def bulk(self):
        bulk = 0
        return bulk

    @property
    def group(self):
        group = None
        return group

    @property
    def armor_traits(self):
        armor_traits = None
        return armor_traits

    def __init__(self):
        self.item = {
            "armor_type": self.armor_type.value,
            "category": self.category.value,
            "ac_bonus": self.ac_bonus,
            "dex_cap": self.dex_cap,
            "check_penalty": self.check_penalty,
            "speed_penalty": self.speed_penalty,
            "strength": self.strength,
            "bulk": self.bulk,
            "group": self.group,
            "armor_traits": self.armor_traits
        }

    def configure(self, character):
        character.set_armor(NoArmor())
        character.set_armor_class_score(calculate_ac(character, self.dex_cap))
        # TODO: Setup payment system for other armor - "no armor" is free

        return character
