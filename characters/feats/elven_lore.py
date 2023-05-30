from characters.abstract.feats_strategy import FeatsStrategy
from characters.feats.features import Features
from characters.ancestries.types import Ancestries
from characters.feats.sources import FeatureSources
from characters.feats.types import FeatureTypes
from characters.skills.types import Skills
from characters.skills.lores import Lores
from characters.builder.proficiency_types import Proficiencies


class ElvenLore(FeatsStrategy):

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
        if character.ancestry == Ancestries.ELF.value:
            conditions_met = True

        return conditions_met

    def configure(self, character):
        if self.minimum_level(character) and self.minimum_prerequisites(character):
            character.set_feature(Features.ELVEN_LORE, FeatureTypes.ANCESTRY, FeatureSources.LEVEL, self.feat_level)
            character.set_lore_subcategory(Lores.ELVEN)

            character.set_skill_proficiency(Skills.ARCANA, Proficiencies.TRAINED)
            character.set_skill_proficiency(Skills.NATURE, Proficiencies.TRAINED)

        else:
            raise ValueError("Your character does not meet the minimum requirements")

        return character



