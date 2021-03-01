#Brevet-Service

import os
import arrow
import re
from flask import Flask, redirect, url_for, request, render_template, jsonify
from pymongo import MongoClient
from flask_restful import Resource, Api

import logging

# Instantiate the app
app = Flask(__name__)
api = Api(app)

client = MongoClient(os.environ['DB_PORT_27017_TCP_ADDR'], 27017)

class Brevets(Resource):
    def get(self):
       return "I am here!" 

# Create routes
# Another way, without decorators
api.add_resource(Brevets, '/listAll')

# Run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
