from characters.ancestries.types import Ancestries
from characters.abstract.strategy import Strategy
from characters.ancestries.languages import Languages
from characters.ancestries.sizes import Sizes
from characters.abilities.types import Abilities
from characters.feats.features import Features
from characters.feats.types import FeatureTypes
from characters.feats.sources import FeatureSources


class Gnome(Strategy):

    def configure(self, character):
        character.set_ancestry(Ancestries.GNOME)
        character.set_language(Languages.COMMON)
        character.set_language(Languages.GNOMISH)
        character.set_language(Languages.SYLVAN)
        character.set_language(Languages.GOBLIN) # this should have been a free choice based on int mod

        character.set_size(Sizes.SMALL)
        character.set_speed(25)
        character.set_hit_points(8)

        character.set_feature(Features.LOW_LIGHT_VISION, FeatureTypes.ANCESTRY, FeatureSources.SPECIAL, 1)

        # set ability boosts
        character.set_ability_modifier(Abilities.CONSTITUTION, 1)
        character.set_ability_modifier(Abilities.CHARISMA, 1)
        character.set_ability_modifier(Abilities.INTELLIGENCE, 1) # this should have been a free choice

        # set ability flaws
        character.set_ability_modifier(Abilities.STRENGTH, -1)

        return character
