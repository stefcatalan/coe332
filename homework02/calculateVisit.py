# reads meteorite json file & calculates time of the trip in order

import json
from numpy import sin, cos, arccos, arcsin, sqrt, radians

# great circle function
def greatCircle(lat1, lon1, lat2, lon2):
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])

    return 3389.5 * (arccos(sin(lat1) * sin(lat2) + cos(lat1) * cos(lat2) * cos(lon1 - lon2)))

def main():
   
    # read data from part 1 and store as dictionary
    with open('jsonData.json') as jsonFile:
        data = json.load(jsonFile)

    # assume robot starts at latitude / longitude
    startingLat = 16.0
    startingLon = 82.0

    # assume robot visits sites in order of list index
    sitesList = data["sites"]

    totalTravel = 0

    # site visit for loop
    for visit in sitesList:
        distance = greatCircle(startingLat, startingLon, visit["latitude"], visit["longitude"])
    
        timeTravel = distance / 10 # robot max speed is 10 km/h

        if visit["composition"] == "stony":
            timeSample = 1
        elif visit["composition"] == "iron":
            timeSample = 2
        elif visit["composition"] == "stony-iron":
            timeSample = 3

        print("leg =", visit["site_id"], ",", "travel time =", timeTravel, ",", "sample time =", timeSample)

        totalTravel += timeTravel

    print("total legs =", visit["site_id"], ",", "total time elapsed =", totalTravel)


    return

if __name__ == '__main__':
    main()

