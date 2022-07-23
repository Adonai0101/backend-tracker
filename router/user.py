from flask import Blueprint,request
from db import mongo

user = Blueprint('user',__name__)

@user.route('/')
def get_user():
    return 'user'

@user.route('/',methods=['POST'])
def post_user():
    data = request.json
    uid = request.json['uid']

    user = mongo.db.user.find_one({'uid':uid})
    if not user:
        print('no existe --s')
        mongo.db.user.insert_one(data)
    return 'post user'