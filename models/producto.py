from instancias import conexion
from sqlalchemy import Column, types, ForeignKey

class ProductModel(conexion.Model):
    __tablename__ = 'productos'
    id = Column(type_=types.Integer, autoincrement=True, primary_key=True)
    nombre = Column(type_=types.Text, nullable=False)
    descripcion = Column(type_=types.Text)
    precio = Column(type_=types.Float, nullable=False)
    disponibilidad = Column(type_=types.Boolean, default=True)

    categoriaId= Column(ForeignKey(column='categorias.id'), type_=types.Integer, nullable=False)