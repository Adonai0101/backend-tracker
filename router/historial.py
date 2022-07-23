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