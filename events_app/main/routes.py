"""Import packages and modules."""
import os
from flask import Blueprint, request, render_template, redirect, url_for, session

# Import app and db from events_app package so that we can run app
from events_app import app, auth, firebase

main = Blueprint("main", __name__)


##########################################
#           Routes                       #
##########################################
@main.route("/")
def homepage():
    """
    Return template for home.
    """
    return render_template('signup.html')


@main.route('/signup', methods=["GET", "POST"])
def signup():
    """Return signup template."""

    # check if it's a post request
    try:
        # request data from front-end
        user = auth.create_user_with_email_and_password(
            "yinnnnnnnn@gmail.com", "1234567")

    except:
        print("could not sign up")
    return render_template('signup.html')


@main.route('/login', methods=["GET", "POST"])
def login():
    """Return login template."""
    if request.method == "GET":
        return '''
               <form action='login' method='POST'>
                <input type='text' name='email' id='email' placeholder='email'/>
                <input type='password' name='password' id='password' placeholder='password'/>
                <input type='submit' name='submit'/>
               </form>
               '''
    elif request.method == "POST":
        try:
            email = request.form.get("email")
            password = request.form.get("password")
            # To sign in user using email and password
            sign_user = auth.sign_in_with_email_and_password(email, password)
            # before the 1 hour expiry:
            sign_user = auth.refresh(sign_user['refreshToken'])
            # now we have a fresh token
            session['user'] = sign_user['idToken']
            print("sign In Successfull")
        except:
            print("Some thing happend!! could not sign in")

        return render_template('signup.html')


@main.route('/reset_password')
def reset():
    token = session['user']
    # Sending Password reset email
    reset_email = auth.send_password_reset_email("Parasmani300@gmail.com")
    print("Please check your email to reset the password")
    return render_template("index.html")


@main.route('/add_sth')
def addSth():
    """ The function can write data into certain collection and user uid"""
    data = {"name": "Mortimer 'Morty' Smith"}
    # To access to the currenr user's uid
    token = session['user']
    user = auth.get_account_info(token)['users'][0]['localId']
    """
    The structure in database should be
    | - project name <lunch chat>
      - | collection
          - | user's uid
              - data you want to safe
    """
    collection = "profile"
    firebase.database().child(collection).child("user").push(data)
    print('data inserted')
    return render_template('/index.html')
