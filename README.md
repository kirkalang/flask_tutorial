# Flask Tutorial
Based on the linkedin learning class - [Building RESTful APIs with Flask](https://www.linkedin.com/learning/building-restful-apis-with-flask).

Below are modification made to course examples to facilitate testing with pytest as opposed to relying entirely on postman.

## Use of Flask Blueprints
Using Blueprints enables adding specific routes for each course chapter. Each chapter has it's own python file in the controllers directory, and adds its own base route.
For example, the Hello World example is in app/controllers/chapter1.py and adds a Blueprint with name 'chap1' and base route '/chap1'.

## Running the Flask app
Currently using python dotenv files, specifically the .flaskenv file to configure the FLASK_APP and other environment configuration settings. 
To run then just requires creating a python virtual environment, running pip install -r requirements.txt and then running flask run.

## Running the pytest tests
The tests are located in the tests directory. 
The conftest.py file defines pytest fixtures used to initialize the app and an associated Flask test_client. 
The app fixture relies of the app.create_app() function that is defined in the app/__init__.py file. 
The app fixture yields an instance of the app that is used to instantiate a new test_client and can be used by the tests to access the app directly.
