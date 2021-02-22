"""Import packages and modules."""
import os
from flask import Blueprint, request, render_template, redirect, url_for, session, flash

# Import app and db from events_app package so that we can run app
from events_app import app, auth, firebase
from events_app.main.utils import getUserID, getUserRole, getStudentProfile

student = Blueprint("student", __name__)
main = Blueprint("main", __name__)


@student.route("/student/chooserole")
def chooserole():
    """
    Return template for create_user_profile.
    """
    return render_template('re_direct_student_recruiter.html')


@student.route('/student/main')
def student_main():
    if session['user']:
        user = getUserID()  # To access to the currenr user's uid
        data = getStudentProfile(user)
        return render_template('Students/profile_info.html', **data)
    else:
        print("please login first")
        return redirect(url_for("main.homepage"))


@student.route('/student/create_profile', methods=['GET', 'POST'])
def create_student_profile():
    if session['user']:  # Check if user has logged in yet
        if request.method == "GET":
            return render_template('Students/create_profile.html')
        elif request.method == "POST":
            data = {
                "name": request.form.get("name"),
                "bio": request.form.get("bio"),
                "school": request.form.get("school"),
                "degree": request.form.get("degree"),
                "graduationDate": request.form.get("graduationDate")
            }
            user = getUserID()
            firebase.database().child("student_profile").child(user).update(
                data)
            print('data inserted')
            return redirect(url_for("student.student_main"))

    else:
        print("You need to log in first")
        return redirect(url_for("main.homepage"))


@student.route('/student/update_profile', methods=['GET', 'POST'])
def update_student_profile():
    """ The function can update data for the student profile """
    if session['user']:
        if request.method == "GET":
            user = getUserID()  # To access to the currenr user's uid
            data = getStudentProfile(user)
            return render_template('Students/update_profile.html', **data)
        elif request.method == "POST":
            data = {
                "name": request.form.get("name"),
                "school": request.form.get("school"),
                "degree": request.form.get("degree"),
                "graduationDate": request.form.get("graduationDate"),
                "bio": request.form.get("bio")
            }
            user = getUserID()
            firebase.database().child("student_profile").child(user).update(
                data)
            print('data updated!')
            return redirect(url_for("student.student_main"))
    else:
        print("You have to be logged in first!")
        return redirect(url_for("main.homepage"))