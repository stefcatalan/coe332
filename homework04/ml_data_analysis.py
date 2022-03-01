#!/usr/bin/env python3
import json
from typing import List
import logging
import socket
import sys


format_str=f'[%(asctime)s {socket.gethostname()}] %(filename)s:%(funcName)s:%(lineno)s - %(levelname)s: %(message)s'
logging.basicConfig(level=logging.WARNING, format=format_str)


def compute_average_mass(a_list_of_dicts: List[dict], a_key_string: str) -> float:
    """
    Iterates through a list of dictionaries, pulling out values associated with
    a given key. Returns the average of those values.

    Args:
        a_list_of_dicts (list): A list of dictionaries, each dict should have the
                                same set of keys.
        a_key_string (string): A key that appears in each dictionary associated
                               with the desired value (will enforce float type).

    Returns:
        result (float): Average value.
    """
    if (len(a_list_of_dicts) == 0):
        logging.error('a list of dicts is empty')
    total_mass = 0.
    for item in a_list_of_dicts:
        total_mass += float(item[a_key_string])
    return(total_mass / len(a_list_of_dicts) )


def check_hemisphere(latitude: float, longitude: float) -> str:
    """
    Given latitude and longitude in decimal notation, returns which hemispheres
    those coordinates land in.

    Args:
        latitude (float): Latitude in decimal notation.
        longitude (float): Longitude in decimal notation.

    Returns:
        location (string): Short string listing two hemispheres.
    """
    if latitude == 0 or longitude == 0:
        #logging.error('youre not really in a hemisphere')
        raise(ValueError)
    location = 'Northern' if (latitude > 0) else 'Southern'
    location = f'{location} & Eastern' if (longitude > 0) else f'{location} & Western'
    return(location)


def count_classes(a_list_of_dicts: List[dict], a_key_string: str) -> dict:
    """
    Iterates through a list of dictionaries, and pulls out the value associated
    with a given key. Counts the number of times each value occurs in the list of
    dictionaries and returns the result.

    Args:
        a_list_of_dicts (list): A list of dictionaries, each dict should have the
                                same set of keys.
        a_key_string (string): A key that appears in each dictionary associated
                               with the desired value.

    Returns:
        classes_observed (dict): Dictionary of class counts.

    """
    classes_observed = {}
    for item in a_list_of_dicts:
        if item[a_key_string] in classes_observed:
            classes_observed[item[a_key_string]] += 1
        else:
            classes_observed[item[a_key_string]] = 1
    return(classes_observed)


def main():
    inputfile = sys.argv[1]

    print('Summary of meteorite data: \n')

    logging.debug('entering main loop')

    with open(inputfile, 'r') as f:
        ml_data = json.load(f)

    logging.debug(f'the type of ml_data is {type(ml_data)}')

    print('Average mass of', len(ml_data['meteorite_landings']), 'meteors:')
    print(compute_average_mass(ml_data['meteorite_landings'], 'mass (g)'), 'grams \n')

    print('Hemisphere data:')

    northeast = 0
    northwest = 0
    southeast = 0
    southwest = 0

    for row in ml_data['meteorite_landings']:
        if check_hemisphere(float(row['reclat']), float(row['reclong'])) == 'Northern & Eastern':
            northeast += 1
        elif check_hemisphere(float(row['reclat']), float(row['reclong'])) == 'Northern & Western':
            northwest += 1
        elif check_hemisphere(float(row['reclat']), float(row['reclong'])) == 'Southern & Eastern':
            southeast += 1
        elif check_hemisphere(float(row['reclat']), float(row['reclong'])) == 'Southern & Western':
            southwest += 1
    print('There were', northeast, 'meteors found in the Northern & Eastern quadrant')
    print('There were', northwest, 'meteors found in the Northern & Western quadrant')
    print('There were', southeast, 'meteors found in the Southern & Eastern quadrant')
    print('There were', southwest, 'meteors found in the Southern & Western quadrant \n')

    print('Class data:')
    keys = list(count_classes(ml_data['meteorite_landings'], 'recclass'))
    for key in keys:
        print('The', key,'class was found', count_classes(ml_data['meteorite_landings'], 'recclass')[key], 'times')



if __name__ == '__main__':
    main()


