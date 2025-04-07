#tarea
from marshmallow import Schema, fields, ValidationError

class pokefav_Schema(Schema):
     pokemon_id = fields.Str(
        required = True,
        validate = lambda x: len(x) >0,
        error_messages = {
            "required" : "El id del pokemon es requerido"
            }
        )