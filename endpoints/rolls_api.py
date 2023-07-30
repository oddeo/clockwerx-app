from flask_jwt_extended import jwt_required, get_jwt
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from schemas import RollSchema
from dice.open import OpenRoll
from dice.initiative import InitiativeRoll
from dice.ability import AbilityCheckRoll
from dice.skill import SkillCheckRoll
from dice.perception import PerceptionRoll
from dice.fortitude import FortitudeSaveRoll
from dice.will import WillSaveRoll
from dice.reflex import ReflexSaveRoll
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
                pass

            roll_map = {
                "ability": AbilityCheckRoll,
                "skill": SkillCheckRoll,
                "initiative": InitiativeRoll,
                "perception": PerceptionRoll,
                "open": OpenRoll
            }

            player = Character.retrieve(character_id)

            if not player:
                raise KeyError()

            result = roll_map[roll_type](player, attribute=attribute).start()

            return {"roll_type": roll_type, "character_id": character_id, "result": result}

        except KeyError:
            abort(401, message=f"Character id {character_id} is not authorized")


@blp.route("/roll/<string:roll_type>/<string:character_id>")
class DiceNoAttributes(MethodView):

    @jwt_required()
    @blp.response(200, RollSchema)
    def get(self, roll_type, character_id):
        try:
            jwt = get_jwt()
            if jwt.get("is_admin"):
                # example for future functions that require admin rights
                pass

            roll_map = {
                "perception": PerceptionRoll,
                "initiative": InitiativeRoll,
                "fortitude": FortitudeSaveRoll,
                "will": WillSaveRoll,
                "reflex": ReflexSaveRoll,
            }

            player = Character.retrieve(character_id)

            if not player:
                raise KeyError()

            result = roll_map[roll_type](player).start()

            return {"roll_type": roll_type, "character_id": character_id, "result": result}

        except KeyError:
            abort(401, message=f"Character id {character_id} is not authorized")
