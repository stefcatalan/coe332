# Tracking the ISS

The International Space Station continuously revolves round us in a low Eart orbit. Given information on the ISS's positional data and when it can be seen around the world, it would be very interesting to sift through. The data set in `ISS.OEM_J2K_EPH.xml` contains information on the position of the ISS during respective epochs. The data set in `XMLsightingData_citiesUSA01.xml` contains information on when the ISS can be seen over various cities. Building a containerized Flask application allows the user to easily query and return the information from the data sets.

### Source Code

The `app.py` script contains the routes needed to go through the positional and sighting data. The routes read what the user wishes to query, then gathers the information from the files.

### Tests

The `test_app.py` script performs a series of pytests for when routes are queried. The command `pytest` executes the code and lets the user know if there has been a problem encountered.

### Makefile

The `Makefile` contains targets to build and run the containerized Flask application. In the repository, the command `make all` executes both targets. `make build` builds the image, and `make run` runs the applicaion. After completing these commands, the user can now interact with the Flask application.

### Dockerfile

The `Dockerfile` contains the containerized Flask application and the files needed in the Docker Image.

## Gathering Information

If the user wishes to download and build the containerized app themself, run these commands to obtain the data first:
```ruby
[isp02]$ wget https://nasa-public-data.s3.amazonaws.com/iss-coords/2022-02-13/ISS_OEM/ISS.OEM_J2K_EPH.xml
[isp02]$ wget https://nasa-public-data.s3.amazonaws.com/iss-coords/2022-02-13/ISS_sightings/XMLsightingData_citiesUSA01.xml
```
In order to build the Docker image, update a `Dockerfile` with the necessary source code and data:
```ruby
...
COPY ISS.OEM_J2K_EPH.xml /app/ISS.OEM_J2K_EPH.xml
COPY XMLsightingData_citiesUSA01.xml /app/XMLsightingData_citiesUSA01.xml
...
ENTRYPOINT ["python"]
CMD ["app.py"]
```
Execute the following command to build your image:
```ruby
[isp02]$ docker build -t <username>/<image_name>:<tag> .
```

The command to pull a pre-containerized copy of the Flask application I have made as follows:
```ruby
[isp02]$ docker pull stefcatalan/midterm:1.0
```

## Running the Containerized App

In order to run the Flask application and name the container:
```ruby
[isp02]$ docker run --name "iss-tracker" -d -p 5006:5000 stefcatalan/midterm:1.0
```
The user is now able to interact with the application. The `'/'` route displays information on how to execute all of the Flask routes.
```ruby
[isp02]$ curl localhost:5006/

    *** Tracking the ISS ***
```
The expected outputs are either a list of the queried input,
```ruby
...
  "2022-057T11:48:56.869Z", 
  "2022-057T11:52:56.869Z", 
  "2022-057T11:56:56.869Z", 
  "2022-057T12:00:00.000Z"
]
```
or a list of dictionaries of a queried key.
```ruby
    "sighting_date": "Thu Feb 24/05:01 AM", 
    "spacecraft": "ISS", 
    "utc_date": "Feb 24, 2022", 
    "utc_offset": "-8.0", 
    "utc_time": "13:01"
  }, 
  {
    "city": "Le_Grand", 
    "country": "United_States", 
    "duration_minutes": "< 1", 
    "enters": "9 above NNE", 
    "exits": "10 above NNE", 
    "max_elevation": "9", 
    "region": "California", 
...
```

## Cleaning Up

After the user is finished analyzing the Flask application, it is necessary to stop and remove the container.
```ruby
[isp02]$ docker ps -a | grep stefcatalan
aba38304ee2     stefcatalan/midterm:1.0       ...
[isp02]$ docker stop aba38304ee2
aba38304ee2
[isp02]$ docker rm aba38304ee2
aba38304ee2
```
### Citations

Goodwin, Scott. 'ISS-COORDS-2022-02-13.' NASA, TOPO, 13 Feb. 2022, [https://data.nasa.gov/Space-Science/ISS-COORDS-2022-02-13/r6u8-bhhq](https://data.nasa.gov/Space-Science/ISS_COORDS_2022-02-13/r6u8-bhhq) 
