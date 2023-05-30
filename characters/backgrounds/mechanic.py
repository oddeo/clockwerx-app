from random import randint

from characters.builder.proficiency_types import Proficiencies
from characters.abstract.strategy import Strategy
from characters.backgrounds.types import Backgrounds
from characters.abilities.types import Abilities
from characters.skills.types import Skills
from characters.feats.types import FeatureTypes
from characters.feats.sources import FeatureSources
from characters.feats.features import Features


class Mechanic(Strategy):

    def configure(self, character):
        """
        The intricate inner workings of machines are no stranger
        to you. Whether they are mundane devices or complex
        clockworks, you know what makes them tick and how to
        maintain them. An adventuring group might keep you around
        to repair their equipment, or you might travel around to offer
        your rare services to those in need—for a price, of course!
        Choose two ability boosts. One must be to Strength or
        Intelligence, and one is a free ability boost.
        You’re trained in the Crafting skill and the Engineering
        Lore skill. You gain the Quick Repair skill feat.
        """

        character.set_background(Backgrounds.MECHANIC)

        # skills training
        character.set_skill_proficiency(Skills.CRAFTING, Proficiencies.TRAINED)
        character.set_skill_proficiency(Skills.LORE, Proficiencies.TRAINED)

        # feat
        character.set_feature(Features.QUICK_REPAIR, FeatureTypes.SKILL, FeatureSources.BACKGROUND, 1)

        # ability boost 1: random choice between strength or intelligence
        character.set_ability_modifier(Abilities.STRENGTH, 1) \
            if randint(0, 1) == 0 \
            else character.set_ability_modifier(Abilities.INTELLIGENCE, 1)

        # ability boost 2: random ability
        abilities_list = list(Abilities)
        abilities_count = len(abilities_list) - 1

        index = randint(0,abilities_count)
        random_ability = abilities_list[index]
        current_ability = character.abilities[random_ability.value]
        character.set_ability_modifier(random_ability, current_ability['modifier'] + 1)

        return character
