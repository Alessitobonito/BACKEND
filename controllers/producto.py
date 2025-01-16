from flask_restful import Resource, request
from models import ProductoModel, CategoriaModel
from marshmallow.exceptions import ValidationError
from .serializers import ProductoSerializer
from instancias import conexion


class ProductosController(Resource):
    def post(self):
        data = request.get_json()
        serializador = ProductoSerializer()
        try:
            data_validada = serializador.load(data)

            # Validate that the category exists if categoriaId is provided
            if 'categoriaId' in data_validada:
                categoria_existente = conexion.session.query(CategoriaModel).filter_by(id=data_validada['categoriaId']).first()
                if not categoria_existente:
                    return {
                        'message': 'Error: La categoría especificada no existe.',
                        'content': None
                    }, 400

            nuevo_producto = ProductoModel(**data_validada)

            conexion.session.add(nuevo_producto)
            conexion.session.commit()

            resultado = serializador.dump(nuevo_producto)

            return {
                'content': resultado,
                'message': 'Producto creado exitosamente'
            }
        except ValidationError as error:
            return {
                'message': 'Error al crear el producto',
                'content': error.args
            }
