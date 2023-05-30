from random import randint

from characters.builder.proficiency_types import Proficiencies

from characters.abstract.strategy import Strategy
from characters.backgrounds.types import Backgrounds

from characters.abilities.types import Abilities
from characters.skills.types import Skills


class NoBackground(Strategy):

    def configure(self, character):

        character.set_background(Backgrounds.NONE)

        # skills training
        character.set_skill_proficiency(Skills.STEALTH, Proficiencies.TRAINED)

        # TODO: These two don't seem to fit in the general skill collection... not sure what they are yet
        # character.set_skill_proficiency(Skills.UNDERWORLD_LORE, Proficiencies.TRAINED)
        # character.set_skill_proficiency(Skills.SMUGGLER, Proficiencies.EXPERT) - "Experienced Smuggler" feat

        # ability boost 1: random choice between dexterity or intelligence
        character.set_ability_modifier(Abilities.DEXTERITY, 1) \
            if randint(0, 1) == 0 \
            else character.set_ability_modifier(Abilities.INTELLIGENCE, 1)

        # ability boost 2: random ability
        abilities_list = list(Abilities)
        abilities_count = len(abilities_list) - 1

        index = randint(0,abilities_count)
        random_ability = abilities_list[index]
        current_ability = character.abilities[random_ability.value]
        character.set_ability_modifier(random_ability, current_ability['modifier'] + 1)

        return character
