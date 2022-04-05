import redis
import json
from flask import Flask, jsonify, request

app = Flask(__name__)

def getData():
    """    
    This route grabs data from the json file in the image container to be analyzed.

    Returns:
        A list of dictionaries on an ML Data Sample.
    """
    return json.load(open('ML_Data_Sample.json', 'r'))

def loadRedis():
    """    
    This route generates the redis client object for the user.

    Returns:
        A running redis database server.
    """
    return redis.Redis(host = '172.17.0.3', port = 6379, db = 0)

@app.route('/read', methods=['GET'])
def readData():
    """
    This route reads the data out of the json file.

    Returns:
        The data as a json list of dictionaries.
    """
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
    """
    This route loads the Meteorite Landing data into a new file.

    Returns:
        A message declaring the process was successul.
    """
    with open('data.json', 'w') as datafile:
        json.dump('ML_Data_Sample.json', datafile)
        datafile.close()

    return f'data has sucessfully been read from the file!\n'

if __name__ == "__main__":
    app.run(debug = True, host = '0.0.0.0')
    d = getData()
    loadRedis(d['meteorite_landings'])
