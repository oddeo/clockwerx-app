from random import randint
from characters.abstract.strategy import Strategy
from characters.classes.types import Classes
from characters.abilities.types import Abilities
from characters.skills.types import Skills
from characters.builder.proficiency_types import Proficiencies


class SummonerDemon(Strategy):

    def configure(self, character):
        character.set_class_type(Classes.SUMMONER_DEMON)
        # "Demon" is the Eidolon

        # Update hit points to be Ancestry HP + 10 + Const Modifier
        current_hp = character.hit_points
        current_const_mod = character.abilities['constitution']['modifier']
        character.set_hit_points(current_hp + 10 + current_const_mod)

        # set ability boosts
        character.set_ability_modifier(Abilities.CHARISMA, 1)

        # set initial proficiency level
        # TODO: Need to be able to set proficiency in SIMPLE WEAPONS & UNARMED "attacks"
        # TODO: Need to be able to set proficiency of spells

        # trained in random skills (count of skills = 3 + Intelligence Modifier)
        skill_count = 3 + character.abilities['intelligence']['modifier']
        skills_list = list(Skills)

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
