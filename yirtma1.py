from flask import Flask, jsonify, json
from flask_restful import Resource, Api

from pymongo import MongoClient
from bson import json_util

import json

app = Flask(__name__)
api = Api(app)


client = MongoClient('mongodb://localhost:27017')

class Deneme(Resource):
    def get(self):
        db = client.pymongo_test
        posts = db.posts
        post_data = {
            'title': 'Python and MongoDB',
            'content': 'PyMongo is fun, you guys',
            'author': 'Scott'
        }
        result = posts.insert_one(post_data)
        return('One post: {0}'.format(result.inserted_id))


class Post(Resource):
    def get(self):
        db = client.pymongo_test
        posts = db.bnbbtc
        scotts_posts = posts.find()
        data = [json.dumps(item, default=json_util.default) for item in scotts_posts ]
        return jsonify(data = data)


api.add_resource(Deneme,'/')
api.add_resource(Post,'/posts')

app.run(port=5000)
