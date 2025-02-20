from app import mongo 
from app.models.superClass import SuperClass
from bson import ObjectId

class PokemonFavorites(SuperClass): 
    def __init__(self):
        super().__init__('pokemon_favorites')

    def create(self, data):
        raise NotImplementedError('Los pokemones no se pueden crear')
    
    def delete(self, object_id):
        raise NotImplementedError('Los pokemones no se pueden eliminar')
    
    def update(self, object_id, data):
        raise NotImplementedError('Los pokemones no se pueden actualizar')
    
    def find_by_id(self, object_id):
        return NotImplementedError("Los pokemones no se pueden encontrar")

    def find_all(self, user_id):
        data = self.collection.find({"user_id": ObjectId(user_id)})
        return data