from characters.abstract.strategy import Strategy
from characters.skills.types import Skills


class ApplySkillScores(Strategy):

    def configure(self, character):
        cab = character.abilities
        csk = character.skills

        character.set_skill_score(Skills.ACROBATICS,
                                  cab['dexterity']['modifier'] + csk['acrobatics']['proficiency'])
        character.set_skill_score(Skills.ARCANA,
                                  cab['intelligence']['modifier'] + csk['arcana']['proficiency'])
        character.set_skill_score(Skills.ATHLETICS,
                                  cab['strength']['modifier'] + csk['athletics']['proficiency'])
        character.set_skill_score(Skills.CRAFTING,
                                  cab['intelligence']['modifier'] + csk['crafting']['proficiency'])
        character.set_skill_score(Skills.DECEPTION,
                                  cab['charisma']['modifier'] + csk['deception']['proficiency'])
        character.set_skill_score(Skills.DIPLOMACY,
                                  cab['charisma']['modifier'] + csk['diplomacy']['proficiency'])
        character.set_skill_score(Skills.INTIMIDATION,
                                  cab['charisma']['modifier'] + csk['intimidation']['proficiency'])
        character.set_skill_score(Skills.LORE,
                                  cab['intelligence']['modifier'] + csk['lore']['proficiency'])
        character.set_skill_score(Skills.MEDICINE,
                                  cab['wisdom']['modifier'] + csk['medicine']['proficiency'])
        character.set_skill_score(Skills.NATURE,
                                  cab['wisdom']['modifier'] + csk['nature']['proficiency'])
        character.set_skill_score(Skills.OCCULTISM,
                                  cab['intelligence']['modifier'] + csk['occultism']['proficiency'])
        character.set_skill_score(Skills.PERFORMANCE,
                                  cab['charisma']['modifier'] + csk['performance']['proficiency'])
        character.set_skill_score(Skills.RELIGION,
                                  cab['wisdom']['modifier'] + csk['religion']['proficiency'])
        character.set_skill_score(Skills.SOCIETY,
                                  cab['wisdom']['modifier'] + csk['society']['proficiency'])
        character.set_skill_score(Skills.STEALTH,
                                  cab['dexterity']['modifier'] + csk['stealth']['proficiency'])
        character.set_skill_score(Skills.SURVIVAL,
                                  cab['wisdom']['modifier'] + csk['survival']['proficiency'])
        character.set_skill_score(Skills.THIEVERY,
                                  cab['dexterity']['modifier'] + csk['thievery']['proficiency'])

        return character
