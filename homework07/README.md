# Software Design Diagrams

While software programs increase in complexity, diagrams are able to describe components of a system in a way that text cannot do. There are two types of diagrams that convey different information. Behaviral diagrams describe dynamic information; how pieces of a system react with one another. Structural diagrams describe the static relationships within a system. These diagrams allow the reader to visualize the software system holisticly in a more convenient manner.

## User Interaction with API

This [project repository](https://github.com/stefcatalan/coe332/tree/main/TrackingTheISS) consists of a Flask application that was containerized in a Docker image. When the user runs the image, they can now interact with the API.

The diagram below is a behavioral diagram that depicts how the user interacts with the API system. The oval shapes indicate start/end points, the paralellograms indicate where the application takes in user input, the rhombus indicates where the application has several options for the user, and the rectangles describe the output data from the Flask app. This flowchart has the capability of conveying the information in a consise, structured way as a guide for any users.

![interactAPI](https://user-images.githubusercontent.com/89610590/165777581-7615ead0-1e42-4a9a-af4e-57379b638003.png)
 
