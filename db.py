import json
from flask import jsonify
from flask_pymongo import PyMongo

mongo = PyMongo()


def cantidades(uid,cuenta):
    
    ingresos = []
    gastos = []
    ingreso_total = 0
    gasto_total = 0
    total = 0

    #hacemos la consulta para retornar alguna shit
    resp = mongo.db.tracker.find({
        "$and" : [
                    {
                        'uid' : uid
                    },
                    {
                        'cuenta':cuenta
                    }
                ]
    })

    for i in resp:

        temp = {
            'id':str(i['_id']),
            'tipo':i['tipo'],
            'categoria':i['categoria'],
            'comentario':i['comentario'],
            'dinero':i['dinero'],
            'cuenta':i['cuenta'],
            'uid':i['uid']
        }

        if i['tipo'] == 'ingresos':
            ingreso_total = ingreso_total + float(temp['dinero'])
            ingresos.append(temp)
        else:
            gasto_total = gasto_total + float(temp['dinero'])
            gastos.append(temp)

    total = ingreso_total - gasto_total

    
    salida ={
        'total':total,
        'ingreso_total':ingreso_total,
        'gasto_total':gasto_total,
        'ingresos':ingresos,
        'gastos':gastos
    }

    return salida

def get_item(uid,id_item):

    resp = mongo.db.tracker.find_one({
    "$and" : [
                {
                    'uid' : uid
                },
                {
                    'cuenta':id_item
                }
            ]
    })

    return resp


def get_historial(uid):
    data = []

    resp = mongo.db.historial.find({'uid' : uid})

    for i in resp:
        temp = {
            'id':str(i['_id']),
            'total':i['total'],
            'ingresoTotal':i['ingreso_total'],
            'gastoTotal':i['gasto_total'],
            'ingresos':i['ingresos'],
            'gastos':i['gastos'],
            'uid':i['uid'],
            'nombre':i['nombre'],
        }
        data.append(temp)
    return data