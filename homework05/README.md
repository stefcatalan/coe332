# Database and Apps

Database servers have the ability to encapsulate data that can be analyzed. In this assignment, we launch a containerized Redis server and Flask app routes to retreive and load data to the database.

## Launching a Containerized Redis Server

A user is able to launch a containerized instance of a Redis database server with:
```ruby
docker run -d -p 6406:6379 -v $(pwd)/data:/data --name=stefcat-redis redis:6 --save 1 1
```
This command comprises of several parts. `-d` lets the container run in the background, which is connected to my assigned Redis port on ISP `6406` to the default Redis port inside the container `6379`. `$(pwd)/data` mounts a local folder to the `/data` folder inside the container. To save 1 backup file every 1 second, the `--save 1 1` is added.

## Analyzing Data with Flask Apps

In order to analyze the data in the database, we have built a small Flask app with routes that perform tasks for the Redis server.

To pull a pre-ontainerized copy of the Flask application I have made:
```ruby
docker pull stefcatalan/redisflask:hw05
```
The user now has access to the copy of the app.

Building the image again if changes were made can be performed as follows:
```ruby
docker build -t stefcatalan/redisflask:hw05 .
```
To run the application and name the container:
```ruby
docker run --name "<name>" -d -p 5006:5000 stefcatalan/redisflask:hw05
```
This connects the Flask routes to my port on the ISP `5006` to the defauly Flak port `5000`

Now that the application is running, the user can now access the routes:
```ruby
curl localhost:5006/<route>
```
The `/read` route reads the ML sample data out of Redis and returns it as a JSON list of dictionaries. The `/load` route loads the ML data into a JSON file in the Redis database instance.


