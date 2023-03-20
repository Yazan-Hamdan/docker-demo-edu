## Dockerfile

This Dockerfile starts with a base image of Python 3.9 on a slim version of Debian Linux. It sets the working directory
to /app and copies the requirements.txt file into the container. It then installs the required packages with pip. After that, it copies the rest of the application code into the container.

The EXPOSE command exposes port 8080, which is the default port for HTTP traffic. Finally, the CMD command starts the
application using uvicorn and sets the host and port to 0.0.0.0:8080, which will allow the container to receive traffic on port 8080.

To build the Docker image, you can run the following command from the same directory as your Dockerfile:

``docker build -t todo-list .``

This will create a Docker image named todo-list. You can then run the container with the following command:

``docker run -p 8080:8080 todo-list``

This will start the container and map port 8080 on your host machine to port 8080 inside the container. You should be able to
access the application by visiting http://localhost in your web browser.

Note that the ``run`` command creates a new cotainer then start it

if you want to start an existing container:

``docker start <container_name|container ID>``


## docker-compose.yml

In this file, we define a service called todo-list, which is built from the Docker image created using the Dockerfile in
the current directory. We also map port 8080 from the container to port 8080 on the host machine using the ports option.

To run this application with Docker Compose, you can run the following command in the same directory as your
docker-compose.yml file:

``docker-compose up``

make sure to build the image before running it using the following command:

``docker-compose up --build``

This will start the container and map port 8080 on your host machine to port 8080 inside the container, just like the docker
run command above.

You can then access the application by visiting http://localhost:8080 in your web browser.

### Lines explaination

``version: "3.9"``
This line specifies the version of the docker-compose file format being used. In this case, it is version 3.9.

``services:``
This line starts the services section of the docker-compose file, where you define the services that make up your application.


``todo-list:``
This line starts the configuration for a service named "todo-list". This is the name that you will use to refer to the service in other parts of the docker-compose file.


``build .``
This line specifies that the service should be built using the Dockerfile in the current directory (.). This means that the docker-compose file is located in the same directory as the Dockerfile.


``Ports: 8080: 8080``
This line specifies that the service should expose port 8080 and map it to port 8080 on the host machine. This means that any traffic that comes in to port 8080 on the host machine will be forwarded to port 8080 on the container running the service.
