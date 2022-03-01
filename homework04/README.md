# Updating and Containerizing a Python Script

After successfully writing scripts with functions and unit tests, we are now satisfied with our application on meteorite data. Now, we have learned how to make the code available to others with the option of using outsourced data.

## Part 1: Optimizing Data Analysis

In order for others to use their own data in our scripts, I had to modify the code to take the name of the JSON file as a command line argument.
```
import sys
...
inputfile = sys.argv[1]

with open(inputfile, 'r') as f:
    ml_data = json.load(f)
```
In this section, we created unit tests for all three functions to assert their accuracy. It is also important to edit the print statements to make the summary of the meteorite data informative and easy to analyze.

## Part 2: Containerizing and Sharing Docker Image



