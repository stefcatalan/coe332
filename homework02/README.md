# Return of the JSON

Homework 02 consists the operation of a robotic vehicle on Mars that investigates five meteorite landing sites in Syrtis Major. We are simulating this mission in two parts, while also implementing aspects of JSON to further improve on our skills using the JSON library.

## Part 1: Generating Coordinates

This script generates five random pairs of latitude and longitude coordinates in the Northern and Eastern hemispheres and also assigns a meteorite composition to each site. All of this data is then gathered in a nested dictionary and saved into a JSON file.

To run the code, the command would be "python3 generateCoordinates.py", which makes the JSON file along with it.

## Part 2: Calculating the Visit

This script reads the JSON file from part 1 and stores the data. The robot then visits the five sites in order and gathers a sample from the site, returning a value of time travelled and time to sample in each iteration.

To run this script, the command is "python3 calculateVisit.py", which will print out the statements for the data mentioned above.
