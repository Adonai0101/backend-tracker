from crypt import methods
import json
from flask import Blueprint, jsonify,request
from db import mongo,cantidades
from bson import json_util
from bson.objectid import ObjectId

from datetime import datetime


terminar = Blueprint('terminar',__name__)

@terminar.route('/')
def index_terminar():
    return "terminando"

@terminar.route('/',methods = ['POST'])
def terminando():
    uid = request.json['uid']
    cuenta = request.json['cuenta']
    nombre_historial = datetime.today().strftime('%Y-%m-%d')

    resp = cantidades(uid,cuenta)
    resp['uid'] = uid
    resp['nombre'] = nombre_historial

    #guardamos lo registrado en la db
    mongo.db.historial.insert_one(resp)


    #Eliminamos todos los registros
    mongo.db.tracker.delete_many({

        "$and" : [
            {
                'uid' : uid
            },
            {
                'cuenta':cuenta
            }
        ]
    })

    #obteniemdo los valores de la db
    resp = cantidades(uid,cuenta)
    return resp