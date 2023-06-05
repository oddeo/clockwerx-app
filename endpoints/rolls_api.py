from flask_jwt_extended import jwt_required, get_jwt
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from schemas import RollSchema
from dice.rolls import ability_roll, skill_roll, initiative_roll, perception_roll
from characters.character import Character


blp = Blueprint("rolls", __name__, description="Dice roll operations")


@blp.route("/roll/<string:roll_type>/<string:attribute>/<string:character_id>")
class Dice(MethodView):

    @jwt_required()
    @blp.response(200, RollSchema)
    def get(self, roll_type, attribute, character_id):
        try:
            jwt = get_jwt()
            if jwt.get("is_admin"):
                # example for future functions that require admin rights
                print("user is an admin")

            roll_map = {
                "ability": ability_roll,
                "skill": skill_roll,
                "initiative": initiative_roll,
                "perception": perception_roll
            }

            player = Character.retrieve(character_id)

            if not player:
                raise KeyError()

            result = roll_map[roll_type](player, attribute)

            return {"roll_type": roll_type, "attribute": attribute, "character_id": character_id, "result": result}

        except KeyError:
            abort(401, message=f"Character id {character_id} is not authorized")
