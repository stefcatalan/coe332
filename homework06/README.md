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

In order to use the Flask API, the user must operate in a container on the k8s network. The `python debug deployment` allows the user to access the Flask server after launching a shell inside the container: 

First, the user must get the `Flask service` IP address by doing the following:
```ruby
[stefcat@kube-2 hw06]$ kubectl get services
NAME                     TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)    AGE
stefcat-test-flask-ser   ClusterIP   10.97.99.157     <none>        5000/TCP   3d
```
The user must also get the name of the `python debug deployment` pod:
```ruby
[stefcat@kube-2 hw06]$ kubectl get pods
NAME                                       READY   STATUS    RESTARTS   AGE
py-debug-deployment-5dfcf7bdd9-qjbch       1/1     Running   0          3d15h
```
To launch the debug shell inside the container, `exec` into the gathered pod:
```ruby
[stefcat@kube-2 hw06]$ kubectl exec -it py-debug-deployment-5dfcf7bdd9-qjbch -- /bin/bash
```
Now, the user can access the Flask API!
```ruby
root@py-debug-deployment-5dfcf7bdd9-qjbch:/# curl <flask service IP>:5000/<route>
{
      "GeoLocation": "(-60.7340, 54.3187)", 
      "id": "10297", 
      "mass (g)": "8670", 
      "name": "Thomas", 
       ...
```

