from flask import *
import pymongo
import os

app = Flask(__name__)
app.debug = True
app.secret_key = "Test"

from server.routes import *
