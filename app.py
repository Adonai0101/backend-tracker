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
from dotenv import load_dotenv
from os import getenv

app = Flask(__name__)
app.secret_key = "SUpersecretoalvalvPutoelqueloleaporqessecreto"
load_dotenv()
CORS(app)
#Mongo db
app.config['MONGO_URI'] = "mongodb://local:LocalDB@cluster0-shard-00-00.eqf28.mongodb.net:27017,cluster0-shard-00-01.eqf28.mongodb.net:27017,cluster0-shard-00-02.eqf28.mongodb.net:27017/tracker?ssl=true&replicaSet=atlas-1154or-shard-0&authSource=admin&retryWrites=true&w=majority"
mongo.init_app(app)


app.register_blueprint(user,url_prefix='/user')
app.register_blueprint(dinero,url_prefix='/dinero')
app.register_blueprint(terminar,url_prefix='/terminar')
app.register_blueprint(historial,url_prefix='/historial')

@app.route('/')
def index():
    print('calando las .env')
    return "works desde una short"

if __name__ == '__main__':
    load_dotenv()
    app.run(debug=True,host="0.0.0.0")