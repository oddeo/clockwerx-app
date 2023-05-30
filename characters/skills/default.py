from characters.abstract.strategy import Strategy


class DefaultSkills(Strategy):

    def __init__(self):
        self.acrobatics = {"score": 0, "proficiency": 0}
        self.arcana = {"score": 0, "proficiency": 0}
        self.athletics = {"score": 0, "proficiency": 0}
        self.crafting = {"score": 0, "proficiency": 0}
        self.deception = {"score": 0, "proficiency": 0}
        self.diplomacy = {"score": 0, "proficiency": 0}
        self.intimidation = {"score": 0, "proficiency": 0}
        self.lore = {"score": 0, "proficiency": 0, "subcategory": ""}
        self.medicine = {"score": 0, "proficiency": 0}
        self.nature = {"score": 0, "proficiency": 0}
        self.occultism = {"score": 0, "proficiency": 0}
        self.performance = {"score": 0, "proficiency": 0}
        self.religion = {"score": 0, "proficiency": 0}
        self.society = {"score": 0, "proficiency": 0}
        self.stealth = {"score": 0, "proficiency": 0}
        self.survival = {"score": 0, "proficiency": 0}
        self.thievery = {"score": 0, "proficiency": 0}

    def configure(self, character):
        character.set_skills(DefaultSkills())

        return character
