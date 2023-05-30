from characters.abstract.feats_strategy import FeatsStrategy
from characters.builder.proficiency_types import Proficiencies


class QuickRepair(FeatsStrategy):

    """
    You take 1 minute to Repair an item. If you’re a master in
    Crafting, it takes 3 actions. If you’re legendary, it takes 1 action.
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
        if character.skills["crafting"]["proficiency"] == Proficiencies.TRAINED.value:
            conditions_met = True

        return conditions_met

    def configure(self, character):
        if self.minimum_level(character) and self.minimum_prerequisites(character):
            pass

        else:
            raise ValueError("Your character does not meet the minimum requirements")

        return character
