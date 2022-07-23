from crypt import methods
import json
from flask import Blueprint, jsonify,request
from db import mongo,cantidades
from bson import json_util
from bson.objectid import ObjectId

dinero = Blueprint('dinero',__name__)

@dinero.route('/<uid>/<cuenta>')
def get_dinero(uid,cuenta):
    #obteniemdo los valores de la db
    resp = cantidades(uid,cuenta)
    return resp

@dinero.route('/',methods=['POST'])
def post_dinero():
    data = request.json
    cuenta = request.json['cuenta']
    uid = request.json['uid']

    #pequeña validacion a lo shit
    try:
        test = float(data['dinero'])
        #insertando en la db
        mongo.db.tracker.insert_one(data)
    except:
        print('te torci como cheto')

    #obteniemdo los valores de la db
    resp = cantidades(uid,cuenta)
    return resp


#obteniendo todos los items de 

@dinero.route('/items/<uid>/<cuenta>')
def get_items(uid,cuenta):
    #obteniemdo los valores de la db
    resp = cantidades(uid,cuenta)

    return resp

#obteniendo uno de los items
@dinero.route('/item/<uid>/<id_item>/<cuenta>')
def get_item(uid,id_item,cuenta):

    resp = mongo.db.tracker.find_one({
    "$and" : [
                {
                    'uid' : uid
                },
                {
                    '_id':ObjectId(id_item)
                },
                {
                    'cuenta':cuenta
                }
            ]
    })
    
    return jsonify({
        'dinero':resp['dinero'],
        'comentario':resp['comentario']
    })

# eliminar
@dinero.route('/item/<uid>/<id_item>/<cuenta>',methods=['DELETE'])
def delete_item(uid,id_item,cuenta):
    print('eliminando esta shit')
    mongo.db.tracker.delete_one({
        "$and" : [
            {
                'uid' : uid
            },
            {
                '_id':ObjectId(id_item)
            },
            {
                'cuenta':cuenta
            }
        ]
    })

    #obteniemdo los valores de la db
    resp = cantidades(uid,cuenta)
    return resp

@dinero.route('/item/<uid>/<id_item>/<cuenta>',methods=['PUT'])
def edit_item(uid,id_item,cuenta):
    print('estas en edit')
    data = request.json
    print(data)

    #pequeña validacion a lo shit
    try:
        test = float(data['dinero'])



        mongo.db.tracker.update_one({
            
            "$and" : [
                {
                    'uid' : uid
                },
                {
                    '_id':ObjectId(id_item)
                },
                {
                    'cuenta':cuenta
                }
            ]
        },
        {
            '$set':{
                'dinero': request.json['dinero'],
                'comentario':request.json['comentario']
            } 
        })
    except:
        print('te torci como cheto')

    #obteniemdo los valores de la db
    resp = cantidades(uid,cuenta)
    return resp
