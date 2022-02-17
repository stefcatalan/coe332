# reads in data, prints info to screen

import json
import logging
import numpy as np

def calculateTurbidity(qualityList: list):
    """
    Given a list containing turbidiity data, this function will calculate the turbidity of the water and determine whether it is below a safe threshold through a log message. Returns the average value of turbidity and its water quality from intervals of five dicts in the list.

    Args:
        qualittyList (list): A list of dictionaries comtaining water quality data.

    Returns:
        T (float): Average turbidity value from each five dictionaries.
    """
    currentT = 0

    # getting values from the list
    for i in range(len(qualityList)):

        a0 = qualityList[i]['calibration_constant']
        I90 = qualityList[i]['detector_current']

        # calculating T for each iteration
        currentT += (a0 * I90)

    # average T from the five measurments
    T = currentT / 5
    print('Average turbidity from last 5 measurments = ', T, 'NTU')

    # set lower log level
    logging.basicConfig(level = logging.DEBUG)

    b = 0    

    # if statement determining if the water is safe or not
    if(T < 1.0):
        isSafe = logging.info('Water quality is safe')
        print('Minimum time required to return below safe threshold = 0 hours\n')
    elif(T > 1.0):
        isSafe = logging.warning('Turbidity is above safe threshold')
        # if it is unsafe, run minTime to calculate time required for T to be < 1.0
        b = minTime(T)
        print('Minimum time required to return below safe threshold =', b, 'hours \n')

    return T

def minTime(T: float):
    """
    Derived from a standart exponential decay function, this function calculates the minimum time required for turbidity to return below a safe threshold. Returns the time calulated in hours.

    Args:
        T (float): The value of turbidity calculated in the previous function.

    Returns:
        b (float): The amount of time elapsed for the turbidity to return to a safe level.
    """
    T0 = T
    Ts = 1.0 # turbidity threshold for safe water
    d = 0.02 # decay factor per hour

    # equation to solve for minimum time required for T to be at a safe turbidity
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
