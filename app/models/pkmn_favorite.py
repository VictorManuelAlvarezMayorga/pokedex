from app import mongo 
from app.models.superClass import Super_Class


class PokemonFavorites(Super_Class): 
    def __init__(self):
        super().__init__('pokemon_favorites')

    def create(self, data):
        raise NotImplementedError('Los pokemones no se pueden crear')
    
    def delete(self, object_id):
        raise NotImplementedError('Los pokemones no se pueden eliminar')
    
    def update(self, object_id, data):
        raise NotImplementedError('Los pokemones no se pueden actualizar')