from pymongo.collection import ReturnDocument
from db.abstract.dbapi import DbApi
from db.connectors.mongoconnect import MongoDb


class Db(DbApi):

    @classmethod
    def save(cls, encounter, connection=MongoDb):
        db = connection.connect()
        encounters = db.encounters
        # replace this with an upsert to handle create and update
        # this will require a find to see if the encounter exists then update with upsert flag
        saved_encounter = encounters.find_one_and_replace({'encounter_id': encounter.encounter_id},
                                                          encounter.__dict__, upsert=True,
                                                          return_document=ReturnDocument.AFTER)
        return saved_encounter

    @classmethod
    def retrieve(cls, encounter_id, connection=MongoDb) -> dict:
        db = connection.connect()
        encounters = db.encounters

        result = encounters.find_one({"encounter_id": encounter_id})

        return result

    @classmethod
    def retrieve_all(cls, connection=MongoDb) -> dict:
        db = connection.connect()
        encounters = db.encounters
        result = encounters.find()

        return result

    @classmethod
    def remove(cls, encounter_id, connection=MongoDb):
        db = connection.connect()
        encounters = db.encounters
        result = encounters.delete_one({"encounter_id": encounter_id})

        return result.deleted_count

