# randomly generate latitude, longitude, compositions for landing sites

import numpy as np
import random
import json

# list of meteorite compositions
meteorComp = ["stony","iron","stony-iron"]

# list of sites
sitesList = []

# randomly generate 5 coordinates
for x in range(5):
    lat = np.random.uniform(16.0, 18.0)
    lon = np.random.uniform(82.0, 84.0)
    
    # randomly choose a meteorite comp from the list
    composition = random.choice(meteorComp)

    # assemble data into a dictionary
    info = {}

    info["site_id"] = x
    info["latitude"] = lat
    info["longitude"] = lon
    info["composition"] = composition

    sitesList.append(info)

# "sites" dictionary
sitesDict = {"sites": sitesList}

# save data into a JSON file
jsonCoordinates = json.dumps(sitesDict, indent = 4)

with open('jsonData.json', 'w') as outfile:
    outfile.write(jsonCoordinates)

