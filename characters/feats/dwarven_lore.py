from characters.abstract.feats_strategy import FeatsStrategy
from characters.feats.features import Features
from characters.ancestries.types import Ancestries
from characters.feats.sources import FeatureSources
from characters.feats.types import FeatureTypes
from characters.skills.types import Skills
from characters.skills.lores import Lores
from characters.builder.proficiency_types import Proficiencies


class DwarvenLore(FeatsStrategy):

    """
    You eagerly absorbed the old stories and traditions of your
    ancestors, your gods, and your people, studying in subjects
    and techniques passed down for generation upon generation.
    You gain the trained proficiency rank in Crafting and
    Religion. If you would automatically become trained in one
    of those skills (from your background or class, for example),
    you instead become trained in a skill of your choice. You also
    become trained in Dwarven Lore.
    """

    @property
    def feat_level(self):
        # set feat level
        feat_level = 1
        return feat_level

    def minimum_level(self, character):
        condition_met = False
        if character.level >= self.feat_level:
            condition_met = True

        return condition_met

    def minimum_prerequisites(self, character):
        conditions_met = False
        if character.ancestry == Ancestries.DWARF.value:
            conditions_met = True

        return conditions_met

    def configure(self, character):
        if self.minimum_level(character) and self.minimum_prerequisites(character):
            character.set_feature(Features.DWARVEN_LORE, FeatureTypes.ANCESTRY, FeatureSources.LEVEL, self.feat_level)
            character.set_lore_subcategory(Lores.DWARVEN)

            character.set_skill_proficiency(Skills.CRAFTING, Proficiencies.TRAINED)
            character.set_skill_proficiency(Skills.RELIGION, Proficiencies.TRAINED)

        else:
            raise ValueError("Your character does not meet the minimum requirements")

        return character
