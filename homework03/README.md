# Analyzing Water Quality

Given information of the turbidity of water samples taken from our Mars mission from before, we will now calculate and analyze the data. This is representative of real world situations where scientists analyze and organize their observations.

## Accessing Data

In order to make calculations to the given data, we must first download the data set. You can do this with the command "curl [url] --output [filename]".

## Calculating Data

After reading the JSON file, this script calculates the average turbidity of the water from every five dicts in the list and determines if the value is within a safe threshold. The script also calculates the time required for the turbidity to be under a safe thresholld if it is initially above 1.0.

To run the code, the command is "python3 waterQuality.py", which gives the information listed above

## Performing Unit Tests

In order to test functions created to calculate the data, this script contains unit tests that work with pytest.

To run the code, the command is "pytest", which will ouput if the tests were successful.

