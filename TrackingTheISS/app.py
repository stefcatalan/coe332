from flask import Flask
import requests
import xmltodict
import json

app = Flask(__name__)

@app.route('/data', methods=['POST'])
def getData():
    """
    This function loads the positional and sighting data from the XML files into JSON files that contain a dictionary of the data.

    Returns:
        A message declaring the process was successful.
    """

    # making the dictionaries able to be scoped globally
    global positionData
    global sightingData

    # opening the xml file for positional data
    with open("ISS.OEM_J2K_EPH.xml", "r") as xmlfile:

        # converting xml data as dictionary
        dictData = xmltodict.parse(xmlfile.read())
        xmlfile.close()

        # converting data into json file
        positionData = json.dumps(dictData)
        with open("positionData.json", "w") as jsonfile:
            jsonfile.write(positionData)
            jsonfile.close()

    # opening the xml file for sighting data
    with open("XMLsightingData_citiesUSA01.xml", "r") as xmlfile:

        # converting xml data as dictionary
        dictData = xmltodict.parse(xmlfile.read())
        xmlfile.close()

        # converting data into json file
        sightingData = json.dumps(dictData)
        with open("sightingData.json", "w") as jsonfile:
            jsonfile.write(sightingData)
            jsonfile.close()

    return f'data has successfully been read from files\n'

@app.route('/epochs', methods=['GET'])
def epochs():
    """
    This function gathers the epoch data from the positional file.
    
    Returns:
        A list of all epochs.
    """
    data = getData()
    
    


if __name__ == '__main__':
    app.run(debug = True, host = '0.0.0.0')

