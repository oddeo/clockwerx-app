from random import randint
from characters.abstract.strategy import Strategy
from characters.classes.types import Classes
from characters.abilities.types import Abilities
from characters.skills.types import Skills
from characters.builder.proficiency_types import Proficiencies
from characters.equipment.armor.categories import ArmorCategory
from characters.equipment.weapons.categories import WeaponsCategory


class RogueThief(Strategy):

    def configure(self, character):
        character.set_class_type(Classes.ROGUE_THIEF)
        # "Thief" is the Rogue Racket

        # Update hit points to be Ancestry HP + 8 + Const Modifier
        current_hp = character.hit_points
        current_const_mod = character.abilities["constitution"]["modifier"]
        character.set_hit_points(current_hp + 8 + current_const_mod)

        # set ability boosts
        character.set_ability_modifier(Abilities.DEXTERITY, 1)

        # set initial proficiency level
        character.set_skill_proficiency(Skills.STEALTH, Proficiencies.TRAINED)
        character.set_skill_proficiency(Skills.THIEVERY, Proficiencies.TRAINED)

        # trained in random skills (count of skills = 7 + Intelligence Modifier)
        skill_count = 7 + character.abilities['intelligence']['modifier']
        skills_list = list(Skills)

        # attacks
        character.set_weapon_proficiency(WeaponsCategory.UNARMED, Proficiencies.TRAINED)
        character.set_weapon_proficiency(WeaponsCategory.SIMPLE, Proficiencies.TRAINED)

        # defenses
        character.set_armor_class_proficiency(ArmorCategory.UNARMORED, Proficiencies.TRAINED)
        character.set_armor_class_proficiency(ArmorCategory.LIGHT, Proficiencies.TRAINED)

        count = 0
        while count < skill_count:
            index = randint(0,len(skills_list)) - 1
            random_skill = skills_list[index]
            current_skill = character.skills[random_skill.value]

            if current_skill['proficiency'] > 0:
                # Ensures we don't double up on proficiencies that were already set
                continue
            else:
                character.set_skill_proficiency(random_skill, Proficiencies.TRAINED)
                skills_list.remove(skills_list[index])
                count += 1

        return character
