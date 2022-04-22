# API Deployment into the Kubernetes-Verse

Kubernetes is an open-source system that operates containerized services for applications. This assignment centers on the deployment of our Flask APIs into k8s, which would make the application available to other users. 

### Redis Containerization

In order to ensure that data stored in Redis is consistent and independent of the Redis pods, a persistent volume claim is needed. The `Redis PVC` yml file provides block storage over the network.

Deployments in k8s allows for a continuous long-running application. The `Redis deployment` yml file ensures that the Redis pods are always being recreated after being deleted or if the application crashes.

Creating a `Redis service` permits the network to communicate with other k8s pods (i.e. Flask APIs) for the user to interact with the applications.

### Flask API Deployment

The `Flask deployment` yml file pulls a containerized Flask application from Docker Hub for the user to interact with. There are 2 replicas of the Flask API pod, so that one can take in user input, and the other can be used to call a desired output.

Services in k8s exposes the Flask API to different components in Kubernetes and the outside world. The `Flask service` makes the Flask application available to outside users and conveniently creates a persistent IP address that can be used to talk to the API, which is independent from the application's pods. 

### A Debug Deployment

In order to use the Flask API, the user must operate in a container on the k8s network. The `python debug deployment` 

(describe and explain how to use it):
1. kubectl get services
    get flask service IP
2. kubectl get pods
    get pod id of python debug deployment
3. kubectl exec -it '< python debug dep id >'
4. curl '< flask service IP >':5000/route  

