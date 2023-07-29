from marshmallow import Schema, fields


class RollSchema(Schema):
    roll_type = fields.Str(required=True)
    attribute = fields.Str(required=False)
    character_id = fields.Str(required=True)
    result = fields.Dict(dump_only=True)


class EncounterSchema(Schema):
    encounter_id = fields.Str(required=True)
    participants = fields.List(fields.Dict())
    result = fields.Dict(dump_only=True)


class AuthSchema(Schema):
    character_id = fields.Str(required=True)
