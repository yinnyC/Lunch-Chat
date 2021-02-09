"""Import packages and modules."""
import os
from flask import Blueprint, request, render_template, redirect, url_for,session

# Import app and db from events_app package so that we can run app
from events_app import app,auth,firebase
print(os.environ.get('DATABASE_URL'))
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

@main.route('/signup')
def signup():
    """Return signup template."""
    try:
        user = auth.create_user_with_email_and_password("Parasmani300@gmail.com","1234567")

    except:
        print("could not sign up")
    return render_template('signup.html')


@main.route('/login')
def login():
    """Return login template."""
    try:
        # To sign in user using email and password
        sign_user = auth.sign_in_with_email_and_password("Parasmani300@gmail.com", "1234567")

        # before the 1 hour expiry:
        sign_user = auth.refresh(sign_user['refreshToken'])
        # now we have a fresh token
        print(sign_user['idToken'])
        session['user'] = sign_user['idToken']
        print("sign In Successfull")

        #Sending the account confirmation mail to the user email on successfull sign in
        # auth.send_email_verification(sign_user['idToken'])
    except:
        print("Some thing happend!! could not sign in")

    return render_template('signup.html')

@main.route('/reset_password')
def reset():
    token = session['user']
    # Sending Password reset email
    reset_email = auth.send_password_reset_email("Parasmani300@gmail.com")
    return render_template("index.html")

@main.route('/add_sth')
def addSth():
    data = {"name": "Mortimer 'Morty' Smith"}
    firebase.database().child("users").push(data)
    print('data inserted')
    return render_template('/index.html')