from random import randint
from characters.abstract.strategy import Strategy
from characters.classes.types import Classes
from characters.abilities.types import Abilities
from characters.skills.types import Skills
from characters.builder.proficiency_types import Proficiencies
from characters.equipment.armor.categories import ArmorCategory
from characters.equipment.weapons.categories import WeaponsCategory
from characters.saving_throws.types import SavingThrows


class Inventor(Strategy):
    """
    Any tinkerer can follow a diagram to make a device, but you invent
    the impossible! Every strange contraption you dream up is a unique
    experiment pushing the edge of possibility, a mysterious machine that
    seems to work for only you. You’re always on the verge of the next great
    breakthrough, and every trial and tribulation is another opportunity to test and tune. If
    you can dream it, you can build it.
    """

    def configure(self, character):
        character.set_class_type(Classes.INVENTOR)

        # Update hit points to be Ancestry HP + 8 + Const Modifier
        current_hp = character.hit_points
        current_const_mod = character.abilities["constitution"]["modifier"]
        character.set_hit_points(current_hp + 8 + current_const_mod)

        # set ability boosts
        character.set_ability_modifier(Abilities.INTELLIGENCE, 1)

        # set initial proficiency level
        character.set_perception_proficiency(Proficiencies.TRAINED)
        character.set_skill_proficiency(Skills.CRAFTING, Proficiencies.TRAINED)

        # saving throws
        character.set_saving_throws_proficiency(SavingThrows.FORTITUDE, Proficiencies.EXPERT)
        character.set_saving_throws_proficiency(SavingThrows.REFLEX, Proficiencies.TRAINED)
        character.set_saving_throws_proficiency(SavingThrows.WILL, Proficiencies.EXPERT)

        # trained in random skills (count of skills = 3 + Intelligence Modifier)
        skill_count = 3 + character.abilities['intelligence']['modifier']
        skills_list = list(Skills)

        # attacks
        character.set_weapon_proficiency(WeaponsCategory.UNARMED, Proficiencies.TRAINED)
        character.set_weapon_proficiency(WeaponsCategory.SIMPLE, Proficiencies.TRAINED)
        character.set_weapon_proficiency(WeaponsCategory.MARTIAL, Proficiencies.TRAINED)

        # defenses
        character.set_armor_class_proficiency(ArmorCategory.LIGHT, Proficiencies.TRAINED)
        character.set_armor_class_proficiency(ArmorCategory.MEDIUM, Proficiencies.TRAINED)
        character.set_armor_class_proficiency(ArmorCategory.UNARMORED, Proficiencies.TRAINED)

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
