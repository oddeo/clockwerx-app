from characters.ancestries.types import Ancestries
from characters.abstract.strategy import Strategy
from characters.ancestries.languages import Languages
from characters.ancestries.sizes import Sizes
from characters.abilities.types import Abilities
from characters.feats.features import Features
from characters.feats.sources import FeatureSources
from characters.feats.types import FeatureTypes
from characters.ancestries.traits import Traits


class Dwarf(Strategy):
    """
    Dwarves have a well-earned reputation as a stoic and stern people, ensconced within citadels
    and cities carved from solid rock. While some see them as dour and humorless crafters of
    stone and metal, dwarves and those who have spent time among them understand their
    unbridled zeal for their work, caring far more about quality than quantity. To a stranger,
    they can seem untrusting and clannish, but to their friends and family, they are warm and
    caring, their halls filled with the sounds of laughter and hammers hitting anvils.
    """

    def configure(self, character):
        character.set_ancestry(Ancestries.DWARF)
        character.set_language(Languages.COMMON)
        character.set_language(Languages.DWARVEN)
        character.set_size(Sizes.MEDIUM)
        character.set_speed(20)
        character.set_hit_points(10)

        # Ancestry special ability
        character.set_feature(Features.DARK_VISION, FeatureTypes.ANCESTRY, FeatureSources.SPECIAL, 1)

        # Ancestry traits
        character.set_trait(Traits.DWARF)
        character.set_trait(Traits.HUMANOID)

        # set ability boosts
        character.set_ability_modifier(Abilities.CONSTITUTION, 1)
        character.set_ability_modifier(Abilities.INTELLIGENCE, 1)
        character.set_ability_modifier(Abilities.WISDOM, 1)

        # set ability flaws
        character.set_ability_modifier(Abilities.CHARISMA, -1)

        return character
