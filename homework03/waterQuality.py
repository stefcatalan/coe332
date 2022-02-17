# reads in data, prints info to screen

import json
import logging
#import datetime
from datetime import datetime
from datetime import *
from datetime import timedelta
import numpy as np

def calculateTurbidity(qualityList: list):

    currentT = 0

    # getting values from the list
    for i in range(len(qualityList)):

        a0 = qualityList[i]['calibration_constant']
        I90 = qualityList[i]['detector_current']

        currentT += (a0 * I90)

    # calculates turbidity wanted
    T = currentT / 5
    print('Average turbidity from last 5 measurments = ', T, 'NTU')

    logging.basicConfig(level = logging.DEBUG)
    b = 0    

    # if statement determining if the water is safe or not
    if(T < 1.0):
        isSafe = logging.info('Water quality is safe')
        print('Minimum time required to return below safe threshold = 0 hours\n')
    elif(T > 1.0):
        isSafe = logging.warning('Turbidity is above safe threshold')
        b = minTime(T)
        print('Minimum time required to return below safe threshold =', b, 'hours \n')

    return T

def minTime(T: float):
    T0 = T
    Ts = 1.0
    d = 0.02

    b = np.log((Ts/T0)) / np.log((1-d))
    return b


def main():
    
    # read data from json file
    with open('turbidity_data.json') as jsonFile:
        waterData = json.load(jsonFile)

    # making data into a list
    waterData = list(waterData['turbidity_data'])
 
    # iterating over every 5 data sets
    for i in range(0, len(waterData), 5):
        data = waterData[i: i+5]
        T = calculateTurbidity(data)
        #b = minTime(T)


if __name__ == '__main__':
    main()
