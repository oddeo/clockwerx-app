from characters.ancestries.types import Ancestries
from characters.abstract.strategy import Strategy
from characters.ancestries.languages import Languages
from characters.ancestries.sizes import Sizes
from characters.abilities.types import Abilities
from characters.feats.features import Features
from characters.feats.sources import FeatureSources
from characters.feats.types import FeatureTypes
from characters.ancestries.traits import Traits


class Elf(Strategy):

    def configure(self, character):
        character.set_ancestry(Ancestries.ELF)
        character.set_language(Languages.COMMON)
        character.set_language(Languages.ELVEN)
        character.set_language(Languages.CELESTIAL)
        character.set_size(Sizes.MEDIUM)
        character.set_speed(30)
        character.set_hit_points(6)

        # Ancestry special ability
        character.set_feature(Features.DARK_VISION, FeatureTypes.ANCESTRY, FeatureSources.SPECIAL, 1)

        # Ancestry traits
        character.set_trait(Traits.ELF)
        character.set_trait(Traits.HUMANOID)

        # set ability boosts
        character.set_ability_modifier(Abilities.DEXTERITY, 1)
        character.set_ability_modifier(Abilities.INTELLIGENCE, 1)

        # set ability flaws
        character.set_ability_modifier(Abilities.CONSTITUTION, -1)

        return character
