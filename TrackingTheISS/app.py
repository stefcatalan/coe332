from flask import Flask
import requests

app = Flask(__name__)

# reading data and returning into dictionary
@app.route('/data', methods=['POST'])
def readfile():
    file = requests.get(url='https://nasa-public-data.s3.amazonaws.com/iss-coords/2022-02-13/ISS_sightings/XMLsightingData_citiesUSA01.xml')
    return file.json()













if __name__ == '__main__':
    app.run(debug = True, host = '0.0.0.0')



