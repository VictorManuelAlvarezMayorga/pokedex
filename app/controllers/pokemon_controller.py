from flask import Blueprint, request, jsonify
from marshmallow import ValidationError
from app.models.factory import modelFactory
from bson import ObjectId
from app.tools.response_manager import responseManager

RM = responseManager()
bp = Blueprint("pokemon", __name__, url_prefix="/pokemons")
pokemon_model = modelFactory.get_model("pokemon")

@bp.route("/<string: _id>", method=["GET"])
def get_pokemon(_id): 
    try:
        pokemon = pokemon_model.find_by_id(ObjectId(_id))
        if not pokemon: 
            return RM.error("No se encontró el Pokémon que buscas")
        else: 
            return RM.success(pokemon)
    except:
        return RM.error("Hubo un error")
    
@bp.route("/all-pokemons", method=["GET"])
def all_pokemons (): 
    data = pokemon_model.find_all()
    return RM.success()