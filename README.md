# NLTK_Project
## Overview
Web application, destined to proccess large text inputs and display related stats

## Functionalities
User can write large text and post it on the webstite. Later input is analyzed and related information are extracted. All records are located on the database and can be accessed through 'history'. All records are asigned to a specific user, and can be deleted by him in any time.


## Tools and Frameworks
Visual side of the project is designed in Flask. Most used parts of this framework are flask-login, Jinja2. Database is made through SQLAlchemy. Logic of the program is based on functionalities of the NLTK and TextBlob.

## Authentication
Functionalities of the website are restricted with basic login. User of the service should type his email, password and a first name.

## How to run
You should run a main.py file in a NLTK_Project. The project require connection to the internet during a run, because of NLTK packets.

