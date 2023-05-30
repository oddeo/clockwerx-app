from characters.builder.player_character_builder import PlayerCharacterBuilder
from characters.abilities.default import DefaultAbilities
from characters.skills.default import DefaultSkills
from characters.armor_class.default import DefaultArmorClass
from characters.perception.default import DefaultPerception
from characters.saving_throws.default import DefaultSavingThrows
from characters.bulk_limits.default import DefaultBulkLimit
from characters.weapon_proficiencies.default import DefaultWeaponProficiencies
from characters.equipment.coins.default import DefaultCoins
from characters.equipment.armor.no_armor import NoArmor
from characters.equipment.weapons.fist import Fist
from characters.ancestries.gnome import Gnome
from characters.backgrounds.magical_experiment import MagicalExperiment
from characters.heritages.gnome_wellspring import WellspringGnome
from characters.classes.summoner_demon import SummonerDemon
from characters.skills.apply_skills import ApplySkillScores


class Xazar:
    """
    4) Think of this like filling out your character sheet.
    These are the values found on Merisiel's character sheet.
    Now copy this file and make your own character!

    Hint: If the attribute value is 0, you don't have to set it here.
    Just ignore those attributes.  The "builder" handles them
    for you.
    """

    @staticmethod
    def build():
        return PlayerCharacterBuilder() \
            .set_character_name("Xazar") \
            .set_abilities(DefaultAbilities()) \
            .set_skills(DefaultSkills()) \
            .set_armor_class(DefaultArmorClass()) \
            .set_weapon_proficiencies(DefaultWeaponProficiencies()) \
            .set_ancestry(Gnome()) \
            .set_background(MagicalExperiment()) \
            .set_heritage(WellspringGnome()) \
            .set_class(SummonerDemon()) \
            .set_skills(ApplySkillScores()) \
            .set_perception(DefaultPerception()) \
            .set_saving_throws(DefaultSavingThrows()) \
            .set_bulk(DefaultBulkLimit()) \
            .set_armor(NoArmor()) \
            .set_weapons(Fist()) \
            .set_coins(DefaultCoins()) \
            .get_result()

