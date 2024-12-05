from flask import Flask

# __name__ > propia de python que sirve para indicar si el archivo en el cual nos encontramos es el archivo principal (el que se esta ejecutando por la terminal). si es el archivo principal su valor sera '__main__', caso contrario tendra otro valor la variable
app = Flask(__name__)
# Flask solamente puede tener una instancia en todo el proyecto y esa instancia debe de estar en el archivo principal, sino no podra ejecutarse la instancia de la clase

# decorador: reusar el metodo de una clase sin necesidad de editarlo como tal, solo modifica el comportamiento, para este caso, la ruta configurada
@app.route('/')
def inicio():
    return 'Hola mundo desde flask'

if __name__ == '__main__':
    app.run(debug=True)