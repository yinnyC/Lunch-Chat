"""Import packages and modules."""
import os
from flask import Blueprint, request, render_template, redirect, url_for

# Import app and db from events_app package so that we can run app
from events_app import app

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
def signup_page():
    """Return signup template."""
    return render_template('signup.html')