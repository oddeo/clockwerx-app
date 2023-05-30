from characters.builder.player_character_builder import PlayerCharacterBuilder
from characters.abilities.default import DefaultAbilities
from characters.skills.default import DefaultSkills
from characters.armor_class.default import DefaultArmorClass
from characters.skills.apply_skills import ApplySkillScores
from characters.perception.default import DefaultPerception
from characters.saving_throws.default import DefaultSavingThrows
from characters.bulk_limits.default import DefaultBulkLimit
from characters.weapon_proficiencies.default import DefaultWeaponProficiencies
from characters.equipment.coins.default import DefaultCoins
from characters.equipment.armor.no_armor import NoArmor
from characters.equipment.weapons.fist import Fist
from characters.equipment.weapons.hand import Hand
from characters.ancestries.construct import Construct
from characters.heritages.none import NoHeritage
from characters.backgrounds.none import NoBackground
from characters.classes.prototype import Prototype


class Dekoi:

    @staticmethod
    def build():
        return PlayerCharacterBuilder() \
            .set_character_name("Dekoi") \
            .set_abilities(DefaultAbilities()) \
            .set_skills(DefaultSkills()) \
            .set_armor_class(DefaultArmorClass()) \
            .set_weapon_proficiencies(DefaultWeaponProficiencies()) \
            .set_ancestry(Construct()) \
            .set_background(NoBackground()) \
            .set_heritage(NoHeritage()) \
            .set_perception(DefaultPerception()) \
            .set_skills(ApplySkillScores()) \
            .set_saving_throws(DefaultSavingThrows()) \
            .set_class(Prototype()) \
            .set_bulk(DefaultBulkLimit()) \
            .set_armor(NoArmor()) \
            .set_weapons(Fist()) \
            .set_weapons(Hand()) \
            .set_coins(DefaultCoins()) \
            .get_result()

