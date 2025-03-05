from flask import Blueprint, request, jsonify
from app.schemas.pokemon_fav_schema import pokefav_Schema
from marshmallow import ValidationError
from app.models.factory import modelFactory
from bson import ObjectId
from app.tools.response_manager import responseManager
from flask_jwt_extended import jwt_required, get_jwt_identity  

RM = responseManager()
bp = Blueprint("pokemon_fav", __name__, url_prefix="/my-favorite-pokemons")
pokefav_Schema = pokefav_Schema ()
pokefav_model = modelFactory.get_model("pokemon_favorites")


#Crea
@bp.route("/create", methods=["POST"])
@jwt_required()
def create():
    user_id= get_jwt_identity()
    try:
        data = request.json
        data = pokefav_Schema.load(data)
        data["user_id"]= user_id
        pf = pokefav_model.create (data)
        return RM.success({"_id": pf})
    except ValidationError as err:
        print(err)
        return RM.error("Es necesario enviar los parametros")
#Elimina
@bp.route("/delete", methods=["DELETE"])
@jwt_required()
def delete(id):
    pokefav_model.delete(ObjectId(id))
    return RM.success("Pokemon eleiminado con exito")
#Get All
@bp.route("/", methods=["GET"])
@jwt_required()
def get_all():
    user_id = get_jwt_identity()
    data = pokefav_model.find_all(user_id)
    return RM.success(data)
#Modificar la clase del modelo y evitar que se usen metodos indebidos