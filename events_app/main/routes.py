"""Import packages and modules."""
import os
from flask import Blueprint, request, render_template, redirect, url_for, session, flash

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
    return render_template('index.html')


@main.route('/signup', methods=["GET", "POST"])
def signup():
    """Return signup template."""
    if request.method == "GET":
        return render_template("signup.html")
    elif request.method == "POST":
        try:
            email = request.form.get("email")
            password = request.form.get("password")
            signup_user = auth.create_user_with_email_and_password(
                email, password)
            print("account created!")
            flash("account created!")
            return render_template('login.html')
        except:
            print("could not sign up")
            error = "could not sign up"
            return render_template('signup.html', error=error)


@main.route('/login', methods=["GET", "POST"])
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
            print("sign In Successfully")
            flash("sign In Successfully")
            return redirect(url_for("main.student_main"))
        except:
            print("Some thing happend!! could not sign in")
            error = "Some thing happend!! could not sign in"
            return render_template('login.html', error=error)


@main.route('/logout', methods=["GET", "POST"])
def logout():
    """ remove the current from the session """
    session.pop('user', None)
    print('You have been logged out')
    return redirect(url_for("main.homepage"))


@main.route('/reset_password', methods=['GET', 'POST'])
def reset_password():
    if request.method == "GET":
        return render_template('forgot_password.html')
    elif request.method == "POST":
        # Sending Password reset email
        user_email = request.form.get("email")
        reset_email = auth.send_password_reset_email(user_email)
        print("Please check your email to reset the password")
        flash("Please check your email to reset the password")
        return render_template('forgot_password.html')


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


@main.route('/student_main')
def student_main():
    if session['user']:
        token = session['user']  # To access to the currenr user's uid
        user = auth.get_account_info(token)['users'][0]['localId']
        collection = "student_profile"
        user_profile = firebase.database().child(collection).child(user).get()
        user_profile_data = [data.val() for data in user_profile.each()]

        data = {
            "name": user_profile_data[0]['name'],
            "bio": user_profile_data[0]['bio'],
            "school": user_profile_data[0]['school'],
            "degree": user_profile_data[0]['degree'],
            "graduationDate": user_profile_data[0]['graduationDate'],
        }
        return render_template('student_main.html', **data)
    else:
        print("please login first")
        return redirect(url_for("main.homepage"))


@main.route('/create_student_profile', methods=['GET', 'POST'])
def create_student_profile():
    if session['user']:  # Check if user has logged in yet
        if request.method == "GET":
            return '''
                <form action='/create_student_profile' method='POST'>
                    <input type='text' name='name' id='name' placeholder='name'/>
                    <textarea type='text' name='bio' id='bio' placeholder='bio'></textarea>
                    <input type='text' name='school' id='school' placeholder='school'/>
                    <input type='text' name='degree' id='degree' placeholder='degree'/>
                    <input type='date' name='graduationDate' id='graduationDate' placeholder='graduationDate'/>
                    <input type='submit' name='submit'/>
                </form>
                '''
        elif request.method == "POST":
            data = {
                "name": request.form.get("name"),
                "bio": request.form.get("bio"),
                "school": request.form.get("school"),
                "degree": request.form.get("degree"),
                "graduationDate": request.form.get("graduationDate")
            }
            token = session['user']  # To access to the currenr user's uid
            user = auth.get_account_info(token)['users'][0]['localId']
            collection = "student_profile"
            firebase.database().child(collection).child(user).push(data)
            print('data inserted')
            return redirect(url_for("main.student_main"))

    else:
        print("You need to log in first")
        return redirect(url_for("main.homepage"))


@main.route('/update_student_profile', methods=['GET', 'POST'])
def update_student_profile():
    """ The function can update data for the student profile """
    if session['user']:
        if request.method == "GET":
            return '''
                <form action='/update_student_profile' method='POST'>
                    <input type='text' name='name' id='name' placeholder='name'/>
                    <textarea type='text' name='bio' id='bio' placeholder='bio'></textarea>
                    <input type='text' name='school' id='school' placeholder='school'/>
                    <input type='text' name='degree' id='degree' placeholder='degree'/>
                    <input type='date' name='graduationDate' id='graduationDate' placeholder='graduationDate'/>
                    <input type='submit' name='submit'/>
                </form>
                '''

        elif request.method == "POST":
            data = {
                "first_name": request.form.get("first_name"),
                "last_name": request.form.get("last_name"),
                "school": request.form.get("school"),
                "concentration": request.form.get("concentration")
            }
            token = session['user']
            user = auth.get_account_info(token)['users'][0]['localId']
            collection = "student_profile"
            firebase.database().child(collection).child(user).update(data)
            print('data updated!')
            return redirect(url_for("main.student_main"))

    else:
        print("You have to be logged in first!")
        return redirect(url_for("main.homepage"))