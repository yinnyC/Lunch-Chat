"""Import packages and modules."""
import os
from flask import Blueprint, request, render_template, redirect, url_for, session, flash

# Import app and db from events_app package so that we can run app
from events_app import app, auth, firebase
from events_app.main.utils import getUserID, loginUser, getUserRole

main = Blueprint("main", __name__)
student = Blueprint("student", __name__)


@main.route("/test_recruiter_profile")
def test_recruiter_profile():
    """
    Return template for create_user_profile.
    """
    return render_template('recruiter_profile.html')


##########################################
#          Auth Routes                   #
##########################################
@main.route("/")
def homepage():
    """
    Return template for homepage.
    """
    return render_template('index.html')


@main.route("/signup_role", methods=["POST"])
def signup_role():
    """
    Store the role user picked into session 
    and redirect user to signup page.
    """
    if session['user']:
        return redirect(url_for("main.login"))
    else:
        session['role'] = request.form['submit_button']
        return redirect(url_for("main.signup"))


@main.route('/signup', methods=["GET", "POST"])
def signup():
    """ 
    Get method: Return signup template 
    and pass the role user choosed to template
    POST method:Create an account, store user role to db 
    and redirect to create profile page
    """
    if request.method == "GET":
        role = session['role']
        if role == None:
            return render_template("Auth/re_direct_role.html")
        else:
            return render_template("Auth/signup.html", role=role)
    elif request.method == "POST":
        try:
            email = request.form.get("email")
            password = request.form.get("password")
            # Create User Account
            signup_user = auth.create_user_with_email_and_password(
                email, password)
            loginUser(email, password)  # Login user to create session
            userID = getUserID()  # Save User's role with UserID to db
            firebase.database().child('Role').child(userID).update(
                {"role": request.form.get("role")})
            print("account created!")
            role = getUserRole()  # Redirect user to create profile
            if role == 'Students':
                return redirect(url_for("student.create_student_profile"))
            elif role == 'Recruiters':
                return redirect(url_for("recruiter.create_recruiter_profile"))
            else:
                return render_template('Auth/login.html')
        except:
            role = session['role']
            error = "Could not sign up"
            return render_template("Auth/signup.html", role=role, error=error)


@main.route('/login', methods=["GET", "POST"])
def login():
    """ Return login template."""
    if request.method == "GET":
        if session['user'] and getUserID():
            role = session['role']
            if role == 'Students':
                return redirect(url_for("student.student_main"))
            elif role == 'Recruiters':
                return redirect(url_for("recruiter.recruiter_main"))
            else:
                return render_template('Auth/login.html')
        else:
            return render_template('Auth/login.html')
    elif request.method == "POST":
        try:
            email = request.form.get("email")
            password = request.form.get("password")
            loginUser(email, password)
            role = getUserRole()  # Redirect user to create user profile
            flash("sign In Successfully")
            if role == 'Students':
                return redirect(url_for("student.student_main"))
            else:
                return redirect(url_for("recruiter.recruiter_main"))
        except:
            error = "Some thing happend!! could not sign in"
            return render_template('login.html', error=error)


@main.route('/logout', methods=["GET", "POST"])
def logout():
    """ remove the current from the session """
    session['user'] = None
    session['role'] = None
    print('You have been logged out')
    return redirect(url_for("main.homepage"))


@main.route('/reset_password', methods=['GET', 'POST'])
def reset_password():
    if request.method == "GET":
        return render_template('Auth/forgot_password.html')
    elif request.method == "POST":
        # Sending Password reset email
        user_email = request.form.get("email")
        reset_email = auth.send_password_reset_email(user_email)
        flash("Please check your email to reset the password")
        return render_template('Auth/forgot_password.html')


@main.route('/add_sth')
def addSth():
    """ The function is an example of how to insert data in the firebase realtimeDB"""
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
        firebase.database().child(collection).child(user).update(data)
        print('data inserted')
        return render_template('/index.html')
    else:
        print("You need to log in first")
        return redirect(url_for("main.homepage"))