from flask import Blueprint, request, jsonify
from marshmallow import ValidationError
from app.models.factory import modelFactory
from bson import ObjectId
from app.tools.response_manager import responseManager
from flask_jwt_extended import jwt_required

RM = responseManager()
bp = Blueprint("pokemons", __name__, url_prefix="/pokemons")
pokemon_model = modelFactory.get_model("pokemons")

@bp.route("/<string:_id>", methods=["GET"])
@jwt_required()
def get_pokemon(_id): 
    try:
        pokemon = pokemon_model.find_by_id(ObjectId(_id))
        if not pokemon: 
            return RM.error("No se encontró el Pokémon que buscas")
        else: 
            return RM.success(pokemon)
    except:
        return RM.error("Hubo un error")
    
@bp.route("/all-pokemons", methods=["GET"])
@jwt_required()
def all_pokemons (): 
    data = pokemon_model.find_all()
    return RM.success(data)