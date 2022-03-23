NAME ?= stefcatalan

all: build run

 images:
	docker images | grep ${NAME}

 ps:
	docker ps -a | grep ${NAME}

 build:
	docker build -t ${NAME}/midterm:1.0 .

 run:
	docker run --name "iss-tracker" -d -p 5006:5000 ${NAME}/midterm:1.0
