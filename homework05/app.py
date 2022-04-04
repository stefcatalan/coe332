import redis
import json
import requests
from flask import Flask

app = Flask(__name__)

# getting data from file to analyze from    
def getData():

    return json.load(open('ML_Data_Sample.json', 'r'))

# generating the redis client object
def loadRedis():
    
    return redis.Redis(host = '172.17.0.3', port = 6379, db = 0)

@app.route('/read', methods=['GET'])
def readData():
    file = requests.get(url = "https://raw.githubusercontent.com/wjallen/coe332-sample-data/main/ML_Data_Sample.json")
    return file.json()


if __name__ == "__main__":
    d = getData()
    loadRedis(d['meteorite_landings'])
    app.run(debug = True, host = '0.0.0.0')
