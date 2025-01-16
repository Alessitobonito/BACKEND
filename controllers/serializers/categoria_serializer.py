from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from models import CategoriaModel

class CategoriaSerializer(SQLAlchemyAutoSchema):
    class Meta:
        model = CategoriaModel
    