import redis
import json
#import requests
from flask import Flask, jsonify, request

app = Flask(__name__)

# getting data from file to analyze from    
def getData():

    return json.load(open('ML_Data_Sample.json', 'r'))

# generating the redis client object
def loadRedis():
    
    rd = redis.Redis(host = '172.17.0.3', port = 6379, db = 0)
    for f in data:
        rd.set(d['id'], mapping = d)

@app.route('/read', methods=['GET'])
def readData():
    """
    g = getData()
    start = request.args.get('start', 0)
    try:
        start = int(start)
    except ValueError:
        return 'invalid start input value'
    start = int(start)

    return jsonify(g[start:])
    """
    return getData()

@app.route('/load', methods=['POST'])
def loadData():

    

if __name__ == "__main__":
    app.run(debug = True, host = '0.0.0.0')
    d = getData()
    loadRedis(d['meteorite_landings'])
