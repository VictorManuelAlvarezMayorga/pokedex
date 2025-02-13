from app import mongo
from app.models.superClass import Super_Class

class User(Super_Class):
    def __init__(self):
        super().__init__('users')
    
    def find_all(self):
        raise NotImplementedError('No es necesario obtener todos los usuarios')