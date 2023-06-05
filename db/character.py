from pymongo.collection import ReturnDocument
from db.abstract.dbapi import DbApi
from db.connectors.mongoconnect import MongoDb


class Db(DbApi):

    @classmethod
    def save(cls, character, connection=MongoDb):
        db = connection.connect()
        characters = db.characters
        # replace this with an upsert to handle create and update
        # this will require a find to see if the character exists then update with upsert flag
        saved_character = characters.find_one_and_replace({'character_id': character.character_id},
                                                          character.__dict__, upsert=True,
                                                          return_document=ReturnDocument.AFTER)
        return saved_character['character_id']

    @classmethod
    def retrieve(cls, character_id, connection=MongoDb):
        db = connection.connect()
        characters = db.characters
        character = characters.find_one({"character_id": character_id})
        result = character \
            if character \
            else {"character_id": character_id, "database_result": "record_not_found"}

        return result

    @classmethod
    def retrieve_by_discord_display_name(cls, discord_display_name, connection=MongoDb):
        pipeline = [
                      {
                        "$search": {
                          "index": "discord_display_name",
                          "text": {
                            "query": discord_display_name,
                            "path": {
                              "wildcard": "*"
                            }
                          }
                        }
                      }
                    ]

        db = connection.connect()
        characters = db.characters
        character = list(characters.aggregate(pipeline))
        result = character[0] \
            if character \
            else {"discord_display_name": discord_display_name, "database_result": "record_not_found"}

        return result

    @classmethod
    def remove(cls, character_id, connection=MongoDb):
        db = connection.connect()
        characters = db.characters
        result = characters.delete_one({"character_id": character_id})

        return result.deleted_count

