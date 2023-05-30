from random import randint
from characters.abstract.strategy import Strategy
from characters.classes.types import Classes
from characters.skills.types import Skills
from characters.builder.proficiency_types import Proficiencies
from characters.equipment.armor.categories import ArmorCategory
from characters.equipment.weapons.categories import WeaponsCategory
from characters.saving_throws.types import SavingThrows


class Prototype(Strategy):
    """
    A prototype construct companion is the first construct companion most
    characters get. A companion has the same level you do.
    As you gain levels, you might make further adjustments
    as your companion grows more powerful. Construct
    companions calculate their modifiers and DCs just as you
    do, with one difference: the only item bonuses they can
    benefit from are to Speed.
    Immunities:
    - Bleed
    - Death effects
    - Disease
    - Doomed
    - Drained
    - Fatigued
    - Healing
    - Necromancy
    - Non-lethal attacks
    - Paralyzed
    - Poisoned
    - Sickened
    - Unconscious
    Use Repair action to restore HP - Heal does not work
    """

    def configure(self, character):
        character.set_class_type(Classes.PROTOTYPE)

        # Update hit points to be Ancestry HP + 8 + Const Modifier
        current_hp = character.hit_points
        current_const_mod = character.abilities["constitution"]["modifier"]
        character.set_hit_points(current_hp + 6 + current_const_mod)

        # set initial proficiency level
        character.set_perception_proficiency(Proficiencies.TRAINED)
        character.set_skill_proficiency(Skills.ACROBATICS, Proficiencies.TRAINED)
        character.set_skill_proficiency(Skills.ATHLETICS, Proficiencies.TRAINED)

        # saving throws
        character.set_saving_throws_proficiency(SavingThrows.FORTITUDE, Proficiencies.TRAINED)
        character.set_saving_throws_proficiency(SavingThrows.REFLEX, Proficiencies.TRAINED)
        character.set_saving_throws_proficiency(SavingThrows.WILL, Proficiencies.TRAINED)

        # attacks
        character.set_weapon_proficiency(WeaponsCategory.UNARMED, Proficiencies.TRAINED)

        # defenses
        character.set_armor_class_proficiency(ArmorCategory.UNARMORED, Proficiencies.TRAINED)

        return character
