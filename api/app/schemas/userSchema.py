from marshmallow import Schema, fields, ValidationError

class user_Schema(Schema):
    name = fields.Str(
        required=True,
        validate=lambda x: len(x) >0,
        error_messages={
            'required': 'El nombre de usuario es requerido'
        
        }
    )

    password = fields.Str(
        required=True,
        validate=lambda x: len(x) >0,
        error_messages={
            'required': 'La contraseña es requerida'
        
        }
    )

    email = fields.Email(
        required=True,
        validate=lambda x: '@utma.edu.mx' in x,
        error_messages={
            'required': 'El correo es requerido'
        
        }
    )

