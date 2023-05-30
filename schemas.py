from marshmallow import Schema, fields


class RollSchema(Schema):
    roll_type = fields.Str(required=True)
    attribute = fields.Str(required=True)
    character_id = fields.Str(required=True)
    result = fields.Dict(dump_only=True)


class AuthSchema(Schema):
    character_id = fields.Str(required=True)
