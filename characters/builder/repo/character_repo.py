from db.data import Db, DatabaseException


def save_character(character):
    character_db_id = Db.save_character(character)
    if character_db_id is None:
        raise DatabaseException("Nothing returned from db on save.")

    return character.character_id


def retrieve_character(character_id):
    character = Db.retrieve_character(character_id)
    return character


def retrieve_by_discord_display_name(discord_display_name):
    character = Db.retrieve_by_discord_display_name(discord_display_name)
    return character


def remove_character(character_id):
    character = Db.remove_character(character_id)
    return character
