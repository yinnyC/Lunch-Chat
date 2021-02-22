"""Helper functions for app."""
from flask import session
from events_app import app, auth, firebase


def getUserID():
    token = session['user']  # To access to the currenr user's uid
    user = auth.get_account_info(token)['users'][0]['localId']
    return user


def loginUser(email, password):
    sign_user = auth.sign_in_with_email_and_password(email, password)
    sign_user = auth.refresh(sign_user['refreshToken'])
    session['user'] = sign_user['idToken']


def getUserRole():
    user = getUserID()
    role = firebase.database().child("Role").child(user).get()
    role_data = [data.val() for data in role.each()]
    return role_data[0]['role']
