import jsonpickle
from encounters.repo.encounter_repo import save, retrieve, remove, retrieve_all
from utils.ids import generate_id


class Encounter:

    @classmethod
    def save(cls, encounter):
        result = save(encounter)
        return result

    @classmethod
    def retrieve(cls, encounter_id):
        result = retrieve(encounter_id)
        return result

    @classmethod
    def retrieve_all(cls):
        result = retrieve_all()
        return result

    @classmethod
    def remove(cls, encounter_id):
        result = remove(encounter_id)
        return result

    @classmethod
    def cast(cls, encounter_id: str, encounter_participants: list):
        result = Encounter(encounter_id=encounter_id, participants=encounter_participants)
        return result

    def __init__(self, encounter_id=None, participants=None):
        self.encounter_id = generate_id() if encounter_id is None else encounter_id
        self.participants = [] if participants is None else participants

    def __str__(self):
        json_view = jsonpickle.encode(self)
        return json_view

    def set_encounter_id(self, encounter_id: str):
        self.encounter_id = encounter_id

    def set_participants(self, participants: list):
        for p in participants:
            self.participants.append(p)
