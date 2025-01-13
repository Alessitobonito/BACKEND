from instancias import conexion
from sqlalchemy import Column, types
from datetime import datetime

class categoriaModel(conexion.Model):
    __tablename__ = 'categorias'
    id = Column(types.Integer, autoincrement=True, primary_key=True, nullable=False)
    nombre = Column(types.Text, nullable=False)
    fechaCreacion = Column(name= 'fecha_creacion', type_=types.TIMESTAMP, nullable=False, default=datetime.now)
    disponibilidad = Column(types.Boolean, nullable=False, default=True)