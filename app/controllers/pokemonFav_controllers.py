from flask import Blueprint, request, jsonify
from app.schemas.pokemon_fav_schema import pokefav_Schema
from marshmallow import ValidationError
from app.models.factory import modelFactory
from bson import ObjectId
from app.tools.response_manager import responseManager

RM = responseManager()
bp = Blueprint("pokemon_fav", __name__, url_prefix="/my-favorite-pokemons")
pokefav_Schema = pokefav_Schema ()
pokefav_model = modelFactory.get_model("pokemon_favorites")


#Crea
@bp.route("/create", methods=["POST"])
def create():
    try:
        data = request.json
        data = pokefav_Schema.validate(data)
        pf = pokefav_model.create (data)
        return RM.success({"_id": pf})
    except ValidationError as err:
        print(err)
        return RM.error("Es necesario enviar los parametros")
#Elimina
@bp.route("/delete", methods=["DELETE"])
def delete(_id):
    pokefav_model.delete(ObjectId(_id))
    return RM.success("Pokemon eleiminado con exito")
#Get All
@bp.route("/<string:user_id>", methods=["GET"])
def get_all(user_id):
    data = pokefav_model.find_all()
    return RM.success(data)
#Modificar la clase del modelo y evitar que se usen metodos indebidos