from builder.player_character_builder import PlayerCharacterBuilder
from abilities.default import DefaultAbilities
from skills.default import DefaultSkills
from armor_class.default import DefaultArmorClass
from skills.apply_skills import ApplySkillScores
from perception.default import DefaultPerception
from saving_throws.default import DefaultSavingThrows
from bulk_limits.default import DefaultBulkLimit
from weapon_proficiencies.default import DefaultWeaponProficiencies
from equipment.coins.default import DefaultCoins
from equipment.armor.no_armor import NoArmor
from equipment.weapons.fist import Fist
from equipment.weapons.hand import Hand
from ancestries.dwarf import Dwarf
from heritages.dwarf_forge import ForgeDwarf
from backgrounds.mechanic import Mechanic
from classes.inventor import Inventor
from feats.dwarven_lore import DwarvenLore


class Lemmy:

    @staticmethod
    def build():
        return PlayerCharacterBuilder() \
            .set_character_name("Lemmy Sparks") \
            .set_abilities(DefaultAbilities()) \
            .set_skills(DefaultSkills()) \
            .set_armor_class(DefaultArmorClass()) \
            .set_weapon_proficiencies(DefaultWeaponProficiencies()) \
            .set_ancestry(Dwarf()) \
            .set_background(Mechanic()) \
            .set_heritage(ForgeDwarf()) \
            .set_perception(DefaultPerception()) \
            .set_skills(ApplySkillScores()) \
            .set_saving_throws(DefaultSavingThrows()) \
            .set_class(Inventor()) \
            .set_features(DwarvenLore()) \
            .set_bulk(DefaultBulkLimit()) \
            .set_armor(NoArmor()) \
            .set_weapons(Fist()) \
            .set_weapons(Hand()) \
            .set_coins(DefaultCoins()) \
            .get_result()

