from flask import jsonify
from flask_jwt_extended import jwt_required
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from schemas import EncounterSchema
from encounters.encounter import Encounter


blp = Blueprint("encounters", __name__, description="Encounter collections")


@blp.route("/encounter")
class EncounterList(MethodView):

    @jwt_required()
    @blp.response(200)
    def get(self):
        try:
            encounters = Encounter.retrieve_all()

            results = []
            for enc in encounters:
                results.append({"encounter_id": enc['encounter_id'],
                               "participants": enc['participants']})

            if not encounters:
                raise KeyError()

            return jsonify(results)

        except KeyError:
            abort(401, message=f"Not authorized")


@blp.route("/encounter/<string:encounter_id>")
class EncounterSingle(MethodView):

    @jwt_required()
    @blp.response(200, EncounterSchema)
    def get(self, encounter_id):
        try:

            encounter = Encounter.retrieve(encounter_id)

            result = {"encounter_id": encounter['encounter_id'],
                      "participants": encounter['participants']}

            if not encounter_id:
                raise KeyError()

            return jsonify(result)

        except KeyError:
            abort(404, message=f"Encounter id: {encounter_id} not found")


@blp.route("/encounter")
class SaveEncounter(MethodView):
    @jwt_required()
    @blp.arguments(EncounterSchema)
    def post(self, encounter_data):

        try:
            if encounter_data['encounter_id'] == "":
                encounter = Encounter()
                encounter.set_participants(encounter_data['participants'])

            else:
                encounter_dict = Encounter.retrieve(encounter_data['encounter_id'])
                if encounter_dict:
                    encounter = Encounter.cast(encounter_dict['encounter_id'], encounter_dict['participants'])
                    encounter.set_participants(encounter_data['participants'])
                else:
                    raise KeyError(encounter_data['encounter_id'])

            result = Encounter.save(encounter)

            return {"encounter": result.__dict__}

        except KeyError as ke:
            print(f"bad encounter_id given: {ke}")
            abort(401, message="please provide a valid encounter_id")


@blp.route("/encounter/<string:encounter_id>")
class RemoveEncounter(MethodView):
    @jwt_required()
    @blp.response(204, EncounterSchema)
    def delete(self, encounter_id):

        Encounter.remove(encounter_id)
