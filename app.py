from dotenv import dotenv_values
from flask import Flask, jsonify
from flask import render_template
from flask_smorest import Api
from flask_jwt_extended import JWTManager
from endpoints.rolls_api import blp as roll_blueprint
from endpoints.auth_api import blp as auth_blueprint
from endpoints.encounters_api import blp as encounters_blueprint
from characters.character import Character
from blocklist import BLOCKLIST

app = Flask(__name__)


app.config["PROPAGATE_EXCEPTIONS"] = True
app.config["API_TITLE"] = "Rolls REST API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.0.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

flask_api = Api(app)

flask_api.register_blueprint(roll_blueprint)
flask_api.register_blueprint(auth_blueprint)
flask_api.register_blueprint(encounters_blueprint)

config = dotenv_values(".env")
app.config["JWT_SECRET_KEY"] = config['FLASK_SECRET']
jwt = JWTManager(app)


@jwt.token_in_blocklist_loader
def check_if_token_in_blocklist(jwt_header, jwt_payload):
    return jwt_payload["jti"] in BLOCKLIST


@jwt.revoked_token_loader
def revoked_token_callback(jwt_header, jwt_payload):
    return (
        jsonify({"description": "the token was revoked", "error": "token_revoked"}),
        401,
    )


@jwt.needs_fresh_token_loader
def token_not_fresh_callback(jwt_header, jwt_payload):
    return (
        jsonify({"description": "token is not fresh", "error": "token_revoked"}),
        401,
    )


@jwt.additional_claims_loader
def add_claims_to_jwt(identity):
    given_character_id = identity
    player = Character.retrieve(given_character_id)

    if 'is_admin' in player:
        return {"is_admin": True}
    return {"is_admin": False}


@jwt.expired_token_loader
def expired_token_callback(jwt_header, jwt_payload):
    return (
        jsonify({"message": "the token has expired", "error": "token_expired"}),
        401,
    )


@jwt.invalid_token_loader
def invalid_token_callback(error):
    return (
        jsonify({"message": "signature verification failed", "error": "invalid_token"}),
        401,
    )


@jwt.unauthorized_loader
def missing_token_callback(error):
    return (
        jsonify({"message": "request does not contain an access token", "error": "authorization_required"}),
        401,
    )


@app.route("/")
def hello_world():
    return render_template("index.html")
