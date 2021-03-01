import os
import arrow
import acp_times
import re
from bson.json_util import dumps
from flask import Flask, redirect, url_for, request, render_template, jsonify
from flask_restful import Resource, Api
from pymongo import MongoClient

import logging

app = Flask(__name__)
api = Api(app)

client = MongoClient(os.environ['DB_PORT_27017_TCP_ADDR'], 27017)
db = client.tododb

class Brevets(Resource):
    def get(self):
        _allTimes = db.tododb.find()
        details = []
        for x in _allTimes:
            details.append(x['start'])
            details.append(x['stop'])
        return {'dict' : details }
        
class BrevetsOpenOnly(Resource):
    def get(self):
        k = request.args.get('top', type = int) 
        if k:
            app.logger.warning(k)
            _allTimes = db.tododb.find()
            onion = []
            core=[]
            for x in _allTimes:
                onion.append(x['start'])
                app.logger.info(onion)
            for j in onion:
                app.logger.warning("loop")
                app.logger.warning(j)
                stillonion = j
            for x in range(k):
                core.append(stillonion[x])    
               
            return {'dict' : core }
        
        else:
            _allTimes = db.tododb.find()
            details = []
            for x in _allTimes:
                details.append(x['start'])
            return {'dict' : details }
  

class BrevetsClosedOnly(Resource):
    def get(self):
        k = request.args.get('top', type = int) 
        if k:
            app.logger.warning(k)
            _allTimes = db.tododb.find()
            onion = []
            core=[]
            for x in _allTimes:
                onion.append(x['stop'])
                app.logger.info(onion)
            for j in onion:
                app.logger.warning("loop")
                app.logger.warning(j)
                stillonion = j
            for x in range(k):
                core.append(stillonion[x])    
               
            return {'dict' : core }
        
        else:
            _allTimes = db.tododb.find()
            details = []
            for x in _allTimes:
                details.append(x['stop'])
            return {'dict' : details }

class BrevetsJson(Resource):
    def get(self):
        _allTimes = db.tododb.find()
        details = []
        for x in _allTimes:
            details.append(x['start'])
            details.append(x['stop'])
        return {'dict' : details }
        
class BrevetsOpenOnlyJson(Resource):
    def get(self):
        k = request.args.get('top', type = int) 
        if k:
            app.logger.warning(k)
            _allTimes = db.tododb.find()
            onion = []
            core=[]
            for x in _allTimes:
                onion.append(x['start'])
                app.logger.info(onion)
            for j in onion:
                app.logger.warning("loop")
                app.logger.warning(j)
                stillonion = j
            for x in range(k):
                core.append(stillonion[x])    
               
            return {'dict' : core }
        
        else:
            _allTimes = db.tododb.find()
            details = []
            for x in _allTimes:
                details.append(x['start'])
            return {'dict' : details }

class BrevetsClosedOnlyJson(Resource):
    def get(self):
        k = request.args.get('top', type = int) 
        if k:
            app.logger.warning(k)
            _allTimes = db.tododb.find()
            onion = []
            core=[]
            for x in _allTimes:
                onion.append(x['stop'])
                app.logger.info(onion)
            for j in onion:
                app.logger.warning("loop")
                app.logger.warning(j)
                stillonion = j
            for x in range(k):
                core.append(stillonion[x])    
               
            return {'dict' : core }
        
        else:
            _allTimes = db.tododb.find()
            details = []
            for x in _allTimes:
                details.append(x['stop'])
            return {'dict' : details }

class BrevetsCSV(Resource):
    def get(self):
        _allTimes = db.tododb.find()
        details = []
        string = ""
        for x in _allTimes:
            details.append(x['start'])
            details.append(x['stop'])
        for i in details:
            for j in i:
                string = string + j
                string = string + ","
        app.logger.info(string)
        string = string[:-1]
        return string
        
class BrevetsOpenOnlyCSV(Resource):
    def get(self):
        k = request.args.get('top', type = int) 
        if k:
            _allTimes = db.tododb.find()
            details = []
            string = ""
            for x in _allTimes:
                details.append(x['start'])
            for i in details:
                app.logger.info(i)
                trythis = i
            for j in range(k):
                #app.logger.info(trythis[j])
                string = string + trythis[j]
                string = string + ","

        else:
            _allTimes = db.tododb.find()
            details = []
            string = ""
            for x in _allTimes:
                details.append(x['start'])
            for i in details:
                for j in i:
                    string = string + j
                    string = string + ","       
        string = string[:-1]
        return string

class BrevetsClosedOnlyCSV(Resource):
    def get(self):
        k = request.args.get('top', type = int) 
        if k:
            _allTimes = db.tododb.find()
            details = []
            string = ""
            for x in _allTimes:
                details.append(x['stop'])
            for i in details:
                app.logger.info(i)
                trythis = i
            for j in range(k):
                #app.logger.info(trythis[j])
                string = string + trythis[j]
                string = string + ","

        else:
            _allTimes = db.tododb.find()
            details = []
            string = ""
            for x in _allTimes:
                details.append(x['stop'])
            for i in details:
                for j in i:
                    string = string + j
                    string = string + ","       
        string = string[:-1]
        return string


api.add_resource(Brevets, '/listAll')
api.add_resource(BrevetsOpenOnly, '/listOpenOnly')
api.add_resource(BrevetsClosedOnly, '/listCloseOnly')

api.add_resource(BrevetsJson, '/listAll/json')
api.add_resource(BrevetsOpenOnlyJson, '/listOpenOnly/json')
api.add_resource(BrevetsClosedOnlyJson, '/listCloseOnly/json')

api.add_resource(BrevetsCSV, '/listAll/csv')
api.add_resource(BrevetsOpenOnlyCSV, '/listOpenOnly/csv')
api.add_resource(BrevetsClosedOnlyCSV, '/listCloseOnly/csv')

@app.route('/')
def todo():
    _items = db.tododb.find()
    items = [item for item in _items]

    return render_template('calc.html', items=items)

@app.route('/new', methods=['POST'])
def new():
    app.logger.info("made it into method")
    
    db.tododb.remove({})
    app.logger.info("database is clean!")
    
    #Case to catch an empty submission here.
    if request.form.get('km'):
        
        dbitem = {
            'distance' : request.form['distance'],
            'control' : [],
            'start' : [],
            'stop' : []
        }
        
        #app.logger.warning(dbitem['distance'])

        #distance = request.form['distance'] 
        km = request.form.getlist('km')
        start = request.form.getlist('open')
        stop = request.form.getlist('close')
    
        """ I know a probably could have done these loops by iterating through a
        list or something, but im running out of time and can't waste it on 
        figuring out syntax.
        """
        #dbitem['distance'] = distance
        #db.tododb.insert_one({'BrevitDistance' : distance})
        
        for i in km:
            try:
                float(i)
                toop = (i,)
                dbitem['control'].append(i)
                #dbitem['control'] = [str(x) for x in dbitem['control']]
                #db.tododb.insert_one({'Control' : i})
            except:
                if i.isnumeric():
                    dbitem["control"].append(i)
                    #db.tododb.insert_one({'Control' : i})
        for j in start:
            app.logger.info(j)
            if j:
                dbitem["start"].append(j)
                #db.tododb.insert_one({'StartTime' : j})

        for k in stop:
            if k:
                dbitem["stop"].append(k)
                #db.tododb.insert_one({'StopTime' : k})

        #this should change the lists from being in unicode to UTF8
        
        """ 
        for key in dbitem.keys():
            if isinstance(dbitem[key], list):
                for x in dbitem[key]:
                    dbitem[key] = [x.encode('UTF8') for x in dbitem[key]]
        for x in dbitem:
            app.logger.warning(dbitem[x])
        """
        db.tododb.insert_one(dbitem)


        return redirect(url_for('todo'))

    else:
        return render_template('404.html')

@app.route('/show', methods=['POST'])
def show():

    #Case to catch an empty submission here.
    if db.tododb.count() == 0:
        return render_template('404.html')
    _items = db.tododb.find()
    items = [item for item in _items]
    #THIS DOES!! AHHHH!!!!
    x=0
    for key in items[x].keys():
        if isinstance(items[x][key], list):
            for y in items[x][key]:
                items[x][key] = [y.encode('UTF8') for y in items[x][key]]
    app.logger.info(items)
    return render_template('results.html', items=items)

@app.route('/clear', methods=['POST'])
def clear():
    #clears the database
    db.tododb.remove({})
    return redirect(url_for('todo'))

@app.route("/_calc_times", methods = ['GET'])
def _calc_times():
    app.logger.info("Got a JSON request")
    km = request.args.get('km', -1, type = float)
    length = request.args.get('length', 0, type = int)
    date = request.args.get('date', type = str)
    time = request.args.get('time', type = str)
    datetime = date + " " + time
    datetime = arrow.get(datetime)

    app.logger.info("km = {}".format(km))
    app.logger.info("brevet length = {}".format(length))
    app.logger.info("starting time = {}".format(datetime))
    app.logger.info("date = {}".format(date))
    app.logger.info("time = {}".format(time))
    app.logger.info("request.args: {}".format(request.args))

    open_time = acp_times.open_time(km, length, datetime)
    close_time = acp_times.close_time(km, length, datetime)

    app.logger.info("Open time = {}".format(open_time))
    app.logger.info("Close time = {}".format(close_time))

    if (open_time == "Bad input" or close_time == "Bad input"):
        return jsonify(result = "404")

    else:
        open_time = arrow.get(open_time).for_json()
        close_time = arrow.get(close_time).for_json()
        result = {"open": open_time, "close": close_time}
        app.logger.warning(result)
    return jsonify(result = result)

@app.route("/404")
def page_not_found():
    return render_template('404.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
