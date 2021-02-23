"""Import packages and modules."""

import os
from flask import Blueprint, request, render_template, redirect, url_for, session, flash

# Import app and db from events_app package so that we can run app
from events_app import app, auth, firebase
from events_app.main.utils import getUserID

recruiter = Blueprint("recruiter", __name__)
main = Blueprint("main", __name__)
