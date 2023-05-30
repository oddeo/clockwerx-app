from characters.ancestries.types import Ancestries
from characters.abstract.strategy import Strategy
from characters.ancestries.languages import Languages
from characters.ancestries.sizes import Sizes
from characters.abilities.types import Abilities
from characters.feats.features import Features
from characters.feats.sources import FeatureSources
from characters.feats.types import FeatureTypes
from characters.ancestries.traits import Traits


class Construct(Strategy):
    """
    A construct companion is a loyal semi-sentient
    construct who follows your orders obediently and is
    roughly as intelligent as an animal. Your construct
    companion has the minion trait, and it gains 2 actions
    during your turn if you use the Command a Minion
    action to command it.
    If your companion is destroyed, you can spend 1
    day of downtime and attempt a Crafting check with
    a high DC for your level. On a success, you rebuild
    your companion. You can have only one construct
    companion at a time, and you can have either a
    construct companion or an animal companion, but not
    both.
    Senses:
    - Precise vision
    - Imprecise hearing
    - Vague touch
    - No smell or taste
    """

    def configure(self, character):
        character.set_ancestry(Ancestries.CONSTRUCT)
        character.set_language(Languages.COMMON)
        character.set_size(Sizes.MEDIUM)
        character.set_speed(25)
        character.set_hit_points(10)

        # Ancestry special ability
        character.set_feature(Features.PRECISE_VISION, FeatureTypes.ANCESTRY, FeatureSources.SPECIAL, 1)

        # Ancestry traits
        character.set_trait(Traits.CONSTRUCT)
        character.set_trait(Traits.MINION)

        # set ability boosts
        character.set_ability_modifier(Abilities.STRENGTH, 3)
        character.set_ability_modifier(Abilities.DEXTERITY, 3)
        character.set_ability_modifier(Abilities.CONSTITUTION, 2)
        character.set_ability_modifier(Abilities.WISDOM, 1)

        # set ability flaws
        character.set_ability_modifier(Abilities.INTELLIGENCE, -4)

        return character
