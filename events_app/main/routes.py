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
    if request.method == "GET":
        return '''
               <form action='signup' method='POST'>
                <input type='text' name='email' id='email' placeholder='email'/>
                <input type='password' name='password' id='password' placeholder='7 character minimum'/>
                <input type='submit' name='submit'/>
               </form>
               '''
    elif request.method == "POST":
        try:
            email = request.form.get("email")
            password = request.form.get("password")
            signup_user = auth.create_user_with_email_and_password(
                email, password)
            print("account created!")
        except:
            print("could not sign up")
        return render_template('signup.html')
<<<<<<< HEAD


@main.route('/login', methods=["GET", "POST"])
=======
    
@main.route('/login')
>>>>>>> 22fdc9a5a6980f25e66e0c9ef2e7c92f5a8863dc
def login():
    """ Return login template."""
    if request.method == "GET":
        return render_template('login.html')
    elif request.method == "POST":
        try:
            email = request.form.get("email")
            password = request.form.get("password")
            # To sign in user using email and password
            sign_user = auth.sign_in_with_email_and_password(email, password)
            sign_user = auth.refresh(sign_user['refreshToken'])
            session['user'] = sign_user['idToken']
            print("sign In Successfull")
        except:
            print("Some thing happend!! could not sign in")

        return render_template('signup.html')


@main.route('/logout', methods=["GET", "POST"])
def logout():
    """ remove the current from the session """
    session.pop('user', None)
    print('You have been logged out')
    return redirect(url_for("main.homepage"))


@main.route('/reset_password', methods=['GET', 'POST'])
def reset_password():
    if request.method == "GET":
        return '''
               <form action='/reset_password' method='POST'>
                <input type='text' name='email' id='email' placeholder='email'/>
                <input type='submit' name='submit'/>
               </form>
               '''
    elif request.method == "POST":
        # Sending Password reset email
        user_email = request.form.get("email")
        reset_email = auth.send_password_reset_email(user_email)
        print("Please check your email to reset the password")
        return render_template("index.html")


@main.route('/add_sth')
def addSth():
    """ The function can write data into certain collection and user uid"""
    if session['user']:  # Check if user has logged in yet
        token = session['user']  # To access to the currenr user's uid
        user = auth.get_account_info(token)['users'][0]['localId']
        data = {"name": "Mortimer 'Morty' Smith"}
        """
        The structure of the database should be
        | - project name <lunch chat>
            | - collection
                | - user's uid
                    | - data you want to safe
        """
        collection = "profile"
        firebase.database().child(collection).child(user).push(data)
        print('data inserted')
        return render_template('/index.html')
    else:
        print("You need to log in first")
        return redirect(url_for("main.homepage"))
