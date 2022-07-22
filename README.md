# Flask Tutorial
Based on the linkedin learning class - [Building RESTful APIs with Flask](https://www.linkedin.com/learning/building-restful-apis-with-flask).

Below are modification made to course examples to facilitate testing with pytest as opposed to relying entirely on postman.

## Use of Flask Blueprints
Using Blueprints enables adding specific routes for each course chapter. Each chapter has it's own python file in the controllers directory, and adds its own base route.
For example, the Hello World example is in app/controllers/chapter1.py and adds a Blueprint with name 'chap1' and base route '/chap1'.

## Running the Flask app
Currently using python dotenv files, specifically the .flaskenv file to configure the FLASK_APP and other environment configuration settings. 
To run then just requires creating a python virtual environment, running *pip install -r requirements.txt* and then running *flask run*.

## Running the pytest tests
The tests are located in the tests directory. 
The conftest.py file defines pytest fixtures used to initialize the app and an associated Flask test_client. 
The app fixture relies of the app.create_app() function that is defined in the app/__init__.py file. 
The app fixture yields an instance of the app that is used to instantiate a new test_client and can be used by the tests to access the app directly.

# Docker & AWS
Used the instructions at https://aws.amazon.com/getting-started/hands-on/serve-a-flask-app/ to build a container image and deploy the container using aws lightsail.

* *Dockerfile* - configures environment using pip & requirements.txt, copies project directory structure and runs app using flask run. Currently listening on all IP addresses to ensure the host can access the app running in the container. Future improvement is to specify a specific address instead of using host=0.0.0.0

* Using the above built the docker container image, ran the image and tested locally

* Created a container service using aws lightsail create-container-service and then pushed the container to Lightsail with the aws push-container-image command.

* *containers.json* - specifies the container to deploy and the ports to open on the container

* *public-endpoint.json* - describes the settings of the public endpoint for the container service. Indicates the flask container will expose port 5000. Public endpoint settings are only required for services that require public access

* Deploy the container to the container service using the aws create-container-service-deployment command

* Use the get-container-services command to monitor the state of the container. When it changes to ACTIVE it is up and running.

## Specific commands used to deploy the container

* docker build -t flask-container .

* aws lightsail create-container-service --service-name flask-service --power small --scale 1

* aws lightsail push-container-image --service-name flask-service --label flask-container --image flask-container

* aws lightsail create-container-service-deployment --service-name flask-service --containers file://containers.json --public-endpoint file://public-endpoint.json

* aws lightsail get-container-services --service-name flask-service