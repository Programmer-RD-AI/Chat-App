from pymongo import *
from flask import *
from flask_restful import *

mongodb_url = "mongodb://Ranuga:ranuga2008@cluster0-shard-00-00.6n3dg.mongodb.net:27017,cluster0-shard-00-01.6n3dg.mongodb.net:27017,cluster0-shard-00-02.6n3dg.mongodb.net:27017/myFirstDatabase?ssl=true&replicaSet=atlas-uo9rgq-shard-0&authSource=admin&retryWrites=true&w=majority"
app = Flask(__name__)
app.debug = True
app.secret_key = "development"
cluster = MongoClient(mongodb_url)
from server.routes import *
