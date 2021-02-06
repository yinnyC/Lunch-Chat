# Project Setup

Hi team, I'm trying to keep files modulized and structured so that we can all just work on our own parts of code without having to read through the whole thing before starting.

##  1. Setup Virtual Environment:

To make sure you all have the required library installed and not messing with our own local pakages. I will suggest you use virtual environment. Navigate to your project folder and run the codes below in your terminal: 

    pip3 install virtualenv
    python3 -m venv env
    source env/bin/activate
    pip3 install -r requirement

## 2. Project Structure

Below is the struture of our project and I'll go on the explain what each folder does.


    |- events_app
      | - main
          | - routes.py
      | - static
          | - css
          | - fonts
          | - img 
      | - templates
          | - base.html
          | - other html files ...
      | __init__.py
      | config.py
    | .env
    | app.py


- events_app : Mostly all the magics are gonna happen here. There are three folders under the events_app and two configuration files

  - main: there's a routes.py file where you handle your routes
  - static: where you put css files and imgs
  - templates: where you create html files
    - base.html: base html is where you create the base components that's gonna appear in every page, such as: html boilerplate, nav bar, footer, etc.
  - __init__.py: we initialize the flask app here and load in the config object here.
  - config.py: where you load in the data from the .env file
- .env: where you put in data that should be uploaded onto github
- app.py: to test out your code, run this file