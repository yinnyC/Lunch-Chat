# Dalys-team-project | Lunch Chat for recruiters and job seekers


Lunch Chat is a video conferencing networking tool that will change the way computer engineers connect with tech recruiters. This project is a platform that allows students to schedule quick and informal meetings on recruiters' calendars. Break down barriers, make connections and finally, get recomendations to job opportunities that really fit!

# Built by: Andrea Graziosi, Daniel Duque, Liz Stangle, Shahir Ali, Yin Chang

## Technologies:

- Flask -  A python based server-side architecture used for url routing.
- Jinja2 - A front-end templating library compatible with flask.
- Firebase - A Backend-as-a-Service used for user authentication and realtime database.
- Pyrebase - A python wrapper for the Firebase API.

## Use:

Project Set- Up:

Run these on your terminal

```
   $ pip3 install virtualenv
   $ python3 -m venv env
   $ source env/bin/activate
   $ pip3 install -r requirement
```
### Project Structure:

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

# Click [here]() to visit the website

## Roadmap:

| Skateboard (1 feature) | Bike (2nd feature)     | Car (Extras)           |
| :--------------------- | :--------------------- | :--------------------- |
| Build a login system and allow users to create a profile, and to request meeting dates| Users and recruiters to browse user profiles |  Allow users to select time slots on calendars, and  automatically set up meeting appointments.


