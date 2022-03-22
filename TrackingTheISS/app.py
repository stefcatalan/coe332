from flask import Flask, jsonify
import xmltodict
import json
import logging

app = Flask(__name__)

logging.basicConfig(level = logging.DEBUG)

@app.route('/reset', methods=['POST'])
def getData():
    """
    This route loads the positional and sighting data from the XML files into global variables that contain a list of dictionaries of data.

    Returns:
        A message declaring the process was successful.
    """
    try:
        # making the dictionaries able to be scoped globally
        global positionData
        global sightingData

        # opening the xml file for positional data
        with open("ISS.OEM_J2K_EPH.xml", "r") as xmlfile:

            # converting xml data as dictionary
            positionData = xmltodict.parse(xmlfile.read())
            xmlfile.close()

            # converting data into json file
            positionData = positionData['ndm']['oem']['body']['segment']['data']['stateVector']
            with open("positionData.json", "w") as jsonfile:
            #    jsonfile.write(positionData)
                json.dump(positionData, jsonfile)
                jsonfile.close()

    except FileNotFoundError as e:
        logging.error(e)
        return 'The file was not found\n'

    try:
        # opening the xml file for sighting data
        with open("XMLsightingData_citiesUSA01.xml", "r") as xmlfile:

            # converting xml data as dictionary
            sightingData = xmltodict.parse(xmlfile.read())
            xmlfile.close()

            # converting data into json file
            sightingData = sightingData['visible_passes']['visible_pass']
            with open("sightingData.json", "w") as jsonfile:
                json.dump(sightingData, jsonfile)
                jsonfile.close()

    except FileNotFoundError as e:
        logging.error(e)
        return 'The file was not found\n'

    return f'Data has successfully been read from files!\n'

@app.route('/epochs', methods=['GET'])
def epochs():
    """
    This route gathers all epochs from the positional data.
    
    Returns:
        A list of epochs.
    """
    data = getData()
    global epochList

    epochList = []
    # iterating through the length of the list
    for i in range(len(positionData)):
        currentDict = positionData[i]

        # collecting each value of the key 'epoch'
        if 'EPOCH' in currentDict.keys():
            epochList.append(currentDict['EPOCH'])

    return jsonify(epochList)

@app.route('/epochs/<epoch>', methods=['GET'])
def specificEpoch(epoch: str):
    """
    This route reads in a user input and finds the information on the specific epoch requested.
    
    Args:
        A specified epoch (str value).

    Returns:
        A list of dictionaries with the imformation of the requested epoch.
    """
    data = epochs()

    requestedEpochList = []
    # iterating through the length of the list
    for i in range(len(epochList)):

        # finding dictionaries with the key requested
        if epoch in epochList[i]:
            requestedEpochList.append(positionData[i])

    return jsonify(requestedEpochList)

@app.route('/countries', methods=['GET'])
def countries():
    """
    This route gathers all countries from the sighting data.
    
    Returns:
        A list of all countries.
    """
    data = getData()
    global countryList

    countryList = []
    for i in range(len(sightingData)):
        currentDict = sightingData[i]

        # finding the values for the key 'country'
        if 'country' in currentDict.keys():
            countryList.append(currentDict['country'])

    return jsonify(countryList)


@app.route('/countries/<country>', methods=['GET'])
def specificCountry(country: str):
    """
    This route reads in a user input and finds the information on the specific country requested.

    Args:
        A specified country (str value).

    Reutrns:
        A list of dictionaries with information on the specified country.
    """
    data = countries()
    global requestedCountryList    

    requestedCountryList = []
    for i in range(len(countryList)):

        #finding dictionaries with the key requested
        if country in countryList[i]:
            requestedCountryList.append(sightingData[i])

    return jsonify(requestedCountryList)


@app.route('/countries/<country>/regions', methods=['GET'])
def regions(country: str):
    """
    This route gathers all regions within the given country.
    
    Args:
        The specified country queried from the previous route. (str value)

    Returns:
        A list of the regions.
    """
    data = specificCountry(country)
    global regionsList

    regionsList = []
    for i in range(len(requestedCountryList)):
        currentDict = requestedCountryList[i]
        regionsList.append(currentDict['region'])
    
    return jsonify(regionsList)


@app.route('/countries/<country>/regions/<region>', methods=['GET'])
def specificRegion(country: str, region: str):
    """
    This route reads in a user input and finds the information on the specific region requested.

    Args:
        The specified country queried from a previous route (str value).
        A specified region (str values).

    Reutrns:
        A list of dictionaries with information on the specified region.
    """
    data = regions(country)
    global requestedRegion

    requestedRegion = []
    for i in range(len(regionsList)):
        if region in regionsList[i]:
            requestedRegion.append(requestedCountryList[i])

    return jsonify(requestedRegion)


@app.route('/countries/<country>/regions/<region>/cities', methods=['GET'])
def cities(country: str, region: str):
    """
    This route gathers all cities within the given region.

    Args:
        The specified country queried from a previous route (str value).
        The specified region queried from the previous route (str value).

    Returns:
        A list of the cities.
    """
    data = specificRegion(country, region)
    global citiesList

    citiesList = []
    for i in range(len(requestedRegion)):
        currentDict = requestedRegion[i]
        citiesList.append(currentDict['city'])
    
    return jsonify(citiesList)


@app.route('/countries/<country>/regions/<region>/cities/<city>', methods=['GET'])
def specificCity(country: str, region: str, city: str):
    """
    This route reads in a user input and finds the information on the specific city requested.

    Args:
        The specified country queried from a previous route (str value).
        The specified region queried from a previous route (str value).
        A specified city (str value).
    
    Returns:
        A list of dictionaries with information on the specified region.
    """
    data = cities(country, region)
    
    requestedCity = []
    for i in range(len(citiesList)):
        if city in citiesList[i]:
            requestedCity.append(requestedRegion[i])

    return jsonify(requestedCity)


if  __name__ == '__main__':
    app.run(debug = True, host = '0.0.0.0')

