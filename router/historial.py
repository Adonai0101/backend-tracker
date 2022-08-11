from crypt import methods
import json
from flask import Blueprint, jsonify,request
from db import get_historial
from bson import json_util
from bson.objectid import ObjectId
from db import mongo,cantidades

historial = Blueprint('historial',__name__)

@historial.route('/<uid>')
def index_historial(uid):

    data = get_historial(uid)
    return jsonify({'data':data})

@historial.route('/<uid>',methods = ['DELETE'])
def delete_historial(uid):
    data = request.json
    mongo.db.historial.delete_one({
        "$and" : [
            {
                'uid' : uid
            },
            {
                '_id':ObjectId(data['itemId'])
            }
        ]
    })
    
    data = get_historial(uid)
    return jsonify({'data':data})


@historial.route('/item/<id>')
def get_itemHistorial(id):
    resp = mongo.db.historial.find_one({'_id':ObjectId(id)})
    print(resp)
    return jsonify({
        'total':resp['total'],
        'ingresoTotal':resp['ingreso_total'],
        'gastoTotal':resp['gasto_total'],
        'gastos':resp['gastos'],
        'ingresos':resp['ingresos'],
        'fecha':resp['nombre'],
    })