#tarea
from marshmallow import Schema, fields, ValidationError

class pokefav_Schema(Schema):
    PokemonName = fields.Str(
        required=True,
        validate=lambda x: len(x) >0,
        error_messages={
            'required': 'El nombre del Pokemon es requerido'
        
        }
    )
    PokeId = fields.Str(
        required=True,
        validate=lambda x: len(x) >0,
        error_messages={
            'required': 'El ID del Pokemon es requerido'
        
        }
    )
    name = fields.Str(
        required=True,
        validate=lambda x: len(x) >0,
        error_messages={
            'required': 'El nombre de usuario es requerido'
        
        }
    )