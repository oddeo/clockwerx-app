from characters.abstract.icharacterbuilder import ICharacterBuilder
from characters.character import Character
from characters.builder.character_types import Characters

from characters.abstract.strategy import Strategy


class PlayerCharacterBuilder(ICharacterBuilder):
    """
    2) Think of this like the printing press that prints out
    blank character sheets that get bought by people like us
    """

    def __init__(self):
        self.character = Character(character_type=Characters.PC)

    def set_character_name(self, value: str):
        self.character.set_character_name(value)
        return self

    def set_armor_class(self, strategy: Strategy):
        strategy.configure(self.character)
        return self

    def set_armor(self, strategy: Strategy):
        strategy.configure(self.character)
        return self

    def set_level(self, value: int):
        self.character.set_level(value)
        return self

    def set_hero_points(self, value: int):
        self.character.set_hero_points(value)
        return self

    def set_hit_points(self, value: int):
        self.character.set_hit_points(value)
        return self

    def set_abilities(self, strategy: Strategy):
        strategy.configure(self.character)
        return self

    def set_skills(self, strategy: Strategy):
        strategy.configure(self.character)
        return self

    def set_ancestry(self, strategy: Strategy):
        strategy.configure(self.character)
        return self

    def set_heritage(self, strategy: Strategy):
        strategy.configure(self.character)
        return self

    def set_background(self, strategy: Strategy):
        strategy.configure(self.character)
        return self

    def set_languages(self, languages: list):
        for lang in languages:
            self.character.set_language(lang)

    def set_traits(self, traits: list):
        for trait in traits:
            self.character.set_trait(trait)

    def set_features(self, strategy: Strategy):
        strategy.configure(self.character)
        return self

    def set_class(self, strategy: Strategy):
        strategy.configure(self.character)
        return self

    def set_perception(self, strategy: Strategy):
        strategy.configure(self.character)
        return self

    def set_saving_throws(self, strategy: Strategy):
        strategy.configure(self.character)
        return self

    def set_bulk(self, strategy: Strategy):
        strategy.configure(self.character)
        return self

    def set_weapon_proficiencies(self, strategy: Strategy):
        strategy.configure(self.character)
        return self

    def set_weapons(self, strategy: Strategy):
        strategy.configure(self.character)
        return self

    def set_coins(self, strategy: Strategy):
        strategy.configure(self.character)
        return self

    def set_discord_display_name(self, value: str):
        self.character.set_discord_display_name(value)
        return self

    def get_result(self) -> Character:
        return self.character
