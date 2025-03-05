from app import mongo
from app.models.superClass import SuperClass

class User(SuperClass):
     def __init__(self):
        super().__init__("users")

     def find_all(self):
         raise NotImplementedError("No es necesario obtnener todos los usuarios")
     
     def get_by_email_password(self, email, password):
         user = self.collection.find_one({"email": email, "password":password})
         user["_id"] = str(user["_id"])
         return user