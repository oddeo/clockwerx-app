from characters.character import Character
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from schemas import AuthSchema
from flask_jwt_extended import create_access_token, jwt_required, get_jwt, create_refresh_token, get_jwt_identity
from blocklist import BLOCKLIST

blp = Blueprint("auth", __name__, description="Dice roll auth operations")


@blp.route("/auth")
class DiceAuth(MethodView):
    @blp.arguments(AuthSchema)
    def post(self, auth_data):
        try:
            given_character_id = auth_data['character_id']
            player = Character.retrieve(given_character_id)

            if 'database_result' in player:
                raise KeyError(given_character_id)

            access_token = create_access_token(identity=player['character_id'], fresh=True)
            refresh_token = create_refresh_token(identity=player['character_id'])

            return {"access_token": access_token, "refresh_token": refresh_token}

        except KeyError as ke:
            print(f"bad character_id given: {ke}")
            abort(401, message="please provide a valid character_id")

        except Exception as e:
            print(e)
            abort(500, message="something went wrong on our side")


@blp.route("/logout")
class DiceLogout(MethodView):
    @jwt_required()
    def post(self):
        jti = get_jwt()["jti"]
        BLOCKLIST.add(jti)
        return {"message": "logout successful"}


@blp.route("/refresh")
class DiceRefresh(MethodView):
    @jwt_required(refresh=True)
    def post(self):
        current_user = get_jwt_identity()
        new_token = create_access_token(identity=current_user, fresh=False)
        return {"access_token": new_token}
