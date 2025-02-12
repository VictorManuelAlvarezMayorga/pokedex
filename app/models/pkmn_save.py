from app import mongo 

class Pokemon_Save: 
    collection = mongo.db.pokemons_save
    
    @staticmethod
    def find_all():
        pokemon = Pokemon_Save.collection.find()
        return list(pokemon)
    
    @staticmethod
    def find_by_id (pokemon_id): 
        pokemon = Pokemon_Save.collection.find_one({
            "_id": pokemon_id
        })
        return pokemon
    
    @staticmethod
    def create(data):
        pokemon = Pokemon_Save.collection.insert_one(data)
        return pokemon.inserted_id
    
    @staticmethod
    def update(pokemon_id, data):
        pokemon = Pokemon_Save.collection.update_one({
            "_id": pokemon_id
        }, {
            "$set": data
        })
        return pokemon
    
    @staticmethod
    def delete(pokemon_id):
        return Pokemon_Save.collection.delete_one({"_id": pokemon_id})