# Updating and Containerizing a Python Script

After successfully writing scripts with functions and unit tests, we are now satisfied with our application on meteorite data. Now, we have learned how to make the code available to others with the option of using outsourced data.

## Part 1: Optimizing Data Analysis

In order for others to use their own data in our scripts, I had to modify the code to take the name of the JSON file as a command line argument:
```ruby
import sys
...

inputfile = sys.argv[1]

with open(inputfile, 'r') as f:
    ml_data = json.load(f)
```
In this section, we created unit tests for all three functions to assert their accuracy. It is also important to edit the print statements to make the summary of the meteorite data informative and easy to analyze.

## Part 2: Containerizing and Sharing Docker Image

To make the scripts available to others, I containerized, tagged, and shared my image into Docker Hub. To pull and use my existing image, the command is:
```
docker pull stefcatalan/ml_data_analysis:hw04
```
with `stefcatalan` as my username, `ml_data_analysis` as the script name, and `hw04` as the tag.

Using my Dockerfile, building a Docker image would take the form of:
```
docker build -t <dockerhubusername>/<code>:<tag> .
```
To ensure you have secured a copy of the image, simply use `docker images` and look for your information.

Now that the image is built, a user can run the containerized code again the sample data inside the container:
```ruby
[isp02]$ docker run --rm -v $PWD:/data stefcatalan/ml_data_analysis:hw04 ml_data_analysis.py /data/Meteorite_Landings.json
Summary of meteorite data:
... etc 
```
To run the containerized code against user-provided data, ensure that the data is in `/data`, and rewrite the command:
```ruby
[isp02]$ docker run --rm -v $PWD:/data stefcatalan/ml_data_analysis:hw04 ml_data_analysis.py /data/<filename>
```
Ensure that the functions are working cohesively with the command `pytest`, which will output errors (if any).

## Expected Input Data

In order for user-provided data to work with the Docker Image, the file must have the same formatting as `Meteorite_Landings.json`. This file contains a list of dictionaries in a dictionary titled `"meteorite_landings"`.
```ruby
{
    "meteorite_landings":[
        {
            "name": "Ruiz",
            "id": "10001",
            "recclass": "L5",
            "mass (g)": "21",
            "reclat": "50.775",
            "reclong": "6.08333",
            "Geolocation": "(50.775, 6.08333)"
        },
        ... etc
```
The same keys should be used as the example shows above. Using [this link](https://raw.githubusercontent.com/wjallen/coe332-sample-data/main/ML_Data_Sample.json), you can view additional Meteorite Landing data with the `wget <url>` command. Ensure that the file is downloaded in the same directory of the Docker Image to run the containerized scripts:
```ruby
docker run --rm -v $PWD:/data stefcatalan/ml_data_analysis:hw04 ml_data_analysis.py /data/<filename>
```













