import jsonpickle
from characters.repo.character_repo import save_character, retrieve_character, remove_character, \
    retrieve_by_discord_display_name
from characters.builder.character_types import Characters
from characters.builder.proficiency_types import Proficiencies
from characters.ancestries.types import Ancestries
from characters.ancestries.traits import Traits
from characters.equipment.coins.types import Coins
from characters.feats.features import Features
from characters.feats.sources import FeatureSources
from characters.feats.types import FeatureTypes
from characters.ancestries.sizes import Sizes
from characters.ancestries.languages import Languages
from characters.heritages.types import Heritages
from characters.backgrounds.types import Backgrounds
from characters.classes.types import Classes
from characters.abstract.strategy import Strategy
from characters.abilities.types import Abilities
from characters.skills.types import Skills
from characters.skills.lores import Lores
from characters.equipment.armor.categories import ArmorCategory
from characters.equipment.weapons.categories import WeaponsCategory
from characters.equipment.weapons.types import Weapons
from characters.saving_throws.types import SavingThrows
from utils.ids import generate_id


class Character:
    """
    3) Think of this like a blank character sheet
    that has not been filled out yet
    """

    # TODO: STEP 6 - Spell Attack Roll,
    #                Spell DCs,
    #                Spell Types,
    #                Focus Points
    # TODO: STEP 8 - Equipment
    # TODO: Command line utility for optional parameters

    @classmethod
    def save(cls, character):
        if character.character_id is None:
            new_id = generate_id()
            character.set_character_id(new_id)

        result = save_character(character)
        return result

    @classmethod
    def retrieve(cls, character_id):
        result = retrieve_character(character_id)
        return result

    @classmethod
    def retrieve_by_discord_display_name(cls, discord_display_name):
        result = retrieve_by_discord_display_name(discord_display_name)
        return result

    @classmethod
    def remove(cls, character):
        result = remove_character(character.character_id)
        return result

    @classmethod
    def cast(cls, character_dict: dict):
        result = Character(
            character_id=character_dict['character_id'],
            character_type=Characters(character_dict['character_type']),
            character_name=character_dict['character_name'],
            level=character_dict['level'],
            hero_points=character_dict['hero_points'],
            hit_points=character_dict['hit_points'],
            ancestry=character_dict['ancestry'],
            features=character_dict['features'],
            traits=character_dict['traits'],
            heritage=character_dict['heritage'],
            background=character_dict['background'],
            languages=character_dict['languages'],
            size=character_dict['size'],
            speed=character_dict['speed'],
            class_type=character_dict['class_type'],
            abilities=character_dict['abilities'],
            skills=character_dict['skills'],
            armor_class=character_dict['armor_class'],
            perception=character_dict['perception'],
            saving_throws=character_dict['saving_throws'],
            bulk=character_dict['bulk'],
            armor=character_dict['armor'],
            weapon_proficiencies=character_dict['weapon_proficiencies'],
            weapons=character_dict['weapons'],
            coins=character_dict['coins'],
            discord_display_name=character_dict['discord_display_name'])
        return result

    def __init__(self,
                 character_id=None,
                 character_type=Characters,
                 character_name="",
                 level=1,
                 hero_points=1,
                 hit_points=0,
                 ancestry=Ancestries,
                 features=None,
                 traits=None,
                 heritage=Heritages,
                 background=Backgrounds,
                 languages=None,
                 size=Sizes,
                 speed=0,
                 class_type=Classes,
                 abilities=Strategy,
                 skills=Strategy,
                 armor_class=Strategy,
                 perception=Strategy,
                 saving_throws=Strategy,
                 bulk=Strategy,
                 armor=Strategy,
                 weapon_proficiencies=Strategy,
                 weapons=None,
                 coins=Strategy,
                 discord_display_name=""
                 ):
        self.character_id = character_id
        self.character_type = character_type.value
        self.character_name = character_name
        self.ancestry = ancestry
        self.traits = [] if traits is None else traits
        self.features = [] if features is None else features
        self.heritage = heritage
        self.background = background
        self.languages = [] if languages is None else languages
        self.size = size
        self.speed = speed
        self.class_type = class_type
        self.armor_class = armor_class
        self.level = level
        self.hero_points = hero_points
        self.hit_points = hit_points
        self.abilities = abilities
        self.skills = skills
        self.perception = perception
        self.saving_throws = saving_throws
        self.bulk = bulk
        self.armor = armor
        self.weapon_proficiencies = weapon_proficiencies
        self.weapons = [] if weapons is None else weapons
        self.coins = coins
        self.discord_display_name = discord_display_name

    def __str__(self):
        json_view = jsonpickle.encode(self)
        return json_view

    def set_character_id(self, character_id: str):
        self.character_id = character_id

    def set_character_type(self, character_type: Characters):
        self.character_type = character_type.value

    def set_character_name(self, character_name: str):
        self.character_name = character_name

    def set_ancestry(self, ancestry: Ancestries):
        self.ancestry = ancestry.value

    def set_heritage(self, heritage: Heritages):
        self.heritage = heritage.value

    def set_background(self, background: Backgrounds):
        self.background = background.value

    def set_language(self, language: Languages):
        self.languages.append(language.value["lang_type"])

    def set_trait(self, trait: Traits):
        self.traits.append(trait.value)

    def set_feature(self, feature: Features, f_type: FeatureTypes, source: FeatureSources, level: int):
        self.features.append({"feat": feature.value, "type": f_type.value, "source": source.value, "level": level})

    def set_size(self, size: Sizes):
        self.size = size.value

    def set_speed(self, speed: int):
        self.speed = speed

    def set_class_type(self, class_type: Classes):
        self.class_type = class_type.value

    def set_armor_class(self, armor_class: Strategy):
        self.armor_class = armor_class.__dict__

    def set_armor_class_score(self, score: int):
        current_ac_score = self.armor_class["score"]
        new_score = current_ac_score + score

        self.armor_class["score"] = new_score

    def set_armor_class_proficiency(self, category: ArmorCategory, proficiency: Proficiencies):
        current_prof = self.armor_class[category.value]

        new_proficiency_score = proficiency.value \
            if proficiency.value > current_prof \
            else current_prof

        self.armor_class[category.value] = new_proficiency_score

    def set_armor(self, armor: Strategy):
        self.armor = armor.__dict__

    def set_level(self, level: int):
        self.level = level

    def set_hero_points(self, points: int):
        self.hero_points = points

    def set_hit_points(self, hit_points: int):
        self.hit_points = hit_points

    def set_abilities(self, abilities: Strategy):
        self.abilities = abilities.__dict__

    def set_ability_modifier(self, ability: Abilities, modifier: int):
        current_ability = self.abilities[ability.value]
        current_ability['modifier'] += modifier

        new_score = int(current_ability['score']) + int(modifier * 2)
        current_ability['score'] = new_score if new_score <= 18 else 18

    def set_skills(self, skills: Strategy):
        self.skills = skills.__dict__

    def set_skill_score(self, skill: Skills, score: int):
        self.skills[skill.value]['score'] += score

    def set_skill_proficiency(self, skill: Skills, proficiency: Proficiencies):
        current_prof = self.skills[skill.value]['proficiency']

        new_proficiency_score = proficiency.value \
            if proficiency.value > current_prof \
            else current_prof

        self.skills[skill.value]['proficiency'] = new_proficiency_score

    def set_lore_subcategory(self, lore: Lores):
        self.skills[Skills.LORE.value]['subcategory'] = lore.value

    def set_perception(self, perception: Strategy):
        self.perception = perception.__dict__

    def set_perception_score(self, score: int):
        current_score = self.perception['score']
        new_score = current_score + score

        self.perception['score'] = new_score

    def set_perception_proficiency(self, proficiency: Proficiencies):
        current_proficiency = self.perception['proficiency']

        new_proficiency_score = proficiency.value \
            if proficiency.value > current_proficiency \
            else current_proficiency

        self.perception['proficiency'] = new_proficiency_score

    def set_saving_throws(self, saving_throws: Strategy):
        self.saving_throws = saving_throws.__dict__

    def set_saving_throws_score(self, throw: SavingThrows, score: int):
        current_throw = self.saving_throws[throw.value]
        new_score = current_throw['score'] + score

        self.saving_throws[throw.value]['score'] = new_score

    def set_saving_throws_proficiency(self, throw: SavingThrows, proficiency: Proficiencies):
        current_throw = self.saving_throws[throw.value]

        new_throws_score = proficiency.value \
            if proficiency.value > current_throw['proficiency'] \
            else current_throw['proficiency']
        current_throw['proficiency'] = new_throws_score

        self.saving_throws[throw.value] = current_throw

    def set_bulk(self, bulk: Strategy):
        self.bulk = bulk.__dict__

    def set_bulk_score(self, score: int):
        self.bulk['score'] = score

    def set_bulk_encumbered_base(self, score: int):
        self.bulk['encumbered_base'] = score

    def set_bulk_maximum_base(self, score: int):
        self.bulk['maximum_base'] = score

    def set_weapon_proficiencies(self, weapon_proficiencies: Strategy):
        self.weapon_proficiencies = weapon_proficiencies.__dict__

    def set_weapon_proficiency(self, category: WeaponsCategory, proficiency: Proficiencies):
        current_proficiency = self.weapon_proficiencies[category.value]

        new_proficiency_score = proficiency.value \
            if proficiency.value > current_proficiency \
            else current_proficiency

        self.weapon_proficiencies[category.value] = new_proficiency_score

    def set_weapons(self, weapon: Weapons):
        self.weapons.append(weapon.__dict__)

    def set_coins(self, coins: Strategy):
        self.coins = coins.__dict__

    def set_coin_amount(self, amount: int, coin_type: Coins):
        current_coins = self.coins[coin_type.value]
        new_amount = current_coins + amount
        self.coins[coin_type.value] = new_amount

    def set_discord_display_name(self, discord_display_name: str):
        self.discord_display_name = discord_display_name
