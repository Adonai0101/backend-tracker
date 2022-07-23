import flask
from flask import Flask
from flask_cors import CORS

from router.user import user
from router.dinero import dinero
from router.terminar import terminar
from router.historial import historial

#Database
from db import mongo
#leer variables de entorno
from decouple import config


app = Flask(__name__)
app.secret_key = "SUpersecretoalvalvPutoelqueloleaporqessecreto"
CORS(app)

#Mongo db
app.config['MONGO_URI'] = config('URL_DB')
mongo.init_app(app)


app.register_blueprint(user,url_prefix='/user')
app.register_blueprint(dinero,url_prefix='/dinero')
app.register_blueprint(terminar,url_prefix='/terminar')
app.register_blueprint(historial,url_prefix='/historial')

@app.route('/')
def index():
    return "works desde una short"

if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0")