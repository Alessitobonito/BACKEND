from flask import Flask
from instancias import conexion
from os import environ
from dotenv import load_dotenv
from flask_migrate import Migrate
from models import *


load_dotenv()

app = Flask(__name__)

try:
    import psycopg2
    print("Psycopg2 is installed.")
except ImportError:
    print("Psycopg2 is not installed.")

# Imprime la variable de entorno para verificar que se carga correctamente
print(environ.get('DATABASE_URL'))

# Configura la URI de la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DATABASE_URL')

conexion.init_app(app)
Migrate(app, conexion)

if __name__ == '__main__':
    app.run(debug=True)