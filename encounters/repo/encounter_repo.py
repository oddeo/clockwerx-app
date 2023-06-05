from db.encounter import Db
from db.exception import DatabaseException


def save(encounter):
    encounter_db_id = Db.save(encounter)
    if encounter_db_id is None:
        raise DatabaseException("Nothing returned from db on save.")

    return encounter


def retrieve(encounter_id=None):
    encounter = Db.retrieve(encounter_id)
    return encounter


def retrieve_all():
    encounter = Db.retrieve_all()
    return encounter


def remove(encounter_id):
    encounter = Db.remove(encounter_id)
    return encounter
