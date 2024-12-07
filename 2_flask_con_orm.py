from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, types

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg://postgres:Valdivia123@localhost:5432/bd_flask'
app.config['DEBUG'] = True
conexion = SQLAlchemy(app)

# Cada clase que se cree será como una tabla en la base de datos
class ProductoModel(conexion.Model):
    # Herencia: Semana 1 Programacion Orientada a Objetos
    # ahora declaramos las columnas de la tabla como si fueran atributos de la clase

    # id ....serial primary key  > SQL
    id = Column(type_=types.Integer, primary_key=True, autoincrement=True)
    # nombre ... not null, > SQL
    nombre = Column(type_=types.Text, nullable=False)
    # precio ... not null > SQL
    precio = Column(type_=types.Float(precision=2), nullable=False)
    # serie ... not null unique > SQL
    serie = Column(type_=types.Text, nullable=False, unique=True)
    disponible = Column(type_=types.Boolean, nullable=True)
    # name > si queremos manejar un nombre en el backend y otro nombre en la bd con la propiedad name indicamos como se llamara en la bd
    fechaVencimiento = Column(
        type_=types.Date, nullable=True, name='fecha_vencimiento')

    # para indicar como queremos que se llame la tabla sin modificar el nombre de la clase
    __tablename__ = 'productos'

    @app.route('/crear-tablas')
    def crear_tablas():
        conexion.create_all()
        return {
            'message': 'Tablas creadas exitosamente'
        }
app.run(debug=True)
