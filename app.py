from flask import Flask
from instancias import conexion
from os import environ
from dotenv import load_dotenv


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

if __name__ == '__main__':
    app.run(debug=True)