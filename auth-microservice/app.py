import json
from datetime import datetime, timedelta, timezone

import boto3
from chalice import Chalice
import pyrebase


app = Chalice(app_name='auth-microservice')

# Firebase client
ssm = boto3.client('ssm')
response = ssm.get_parameter(Name='firebase-auth-microservice', WithDecryption=True)
creds = response['Parameter']['Value']
firebase = pyrebase.initialize_app(json.loads(creds)).auth()

# Expire date calculation
def expire_date(expires_in: int):
    expire = datetime.now(timezone.utc) + timedelta(seconds=expires_in)
    return expire.isoformat()

@app.route("/signup", methods=["POST"])
def signup():
    """
    Registers a new user with the provided email and password.
    Returns:
        dict: created user information or an error message if an exception occurs.
    """
    try:
        body = app.current_request.json_body
        user = firebase.create_user_with_email_and_password(email=body.get('email'), password=body.get('password'))
        user["expireDate"] = expire_date(int(user["expiresIn"]))
        return user
    except firebase.AuthError as e:
        return {"error": str(e)}

@app.route("/login", methods=["POST"])
def login():
    """
    Authenticates a user with the provided email and password.
    Returns:
        dict: User information if successful or an error message if an exception occurs.
    """
    try:
        body = app.current_request.json_body
        user = firebase.sign_in_with_email_and_password(email=body.get('email'), password=body.get('password'))
        user["expireDate"] = expire_date(int(user["expiresIn"]))
        return user
    except firebase.AuthError as e:
        return {"error": str(e)}

@app.route("/refresh", methods=["POST"])
def refresh():
    """
    Refreshes the authentication token.
    Returns:
        dict: New authentication token if successful or an error message if an exception occurs.
    """
    try:
        body = app.current_request.json_body
        refreshed_user = firebase.refresh(refresh_token=body.get('refresh_token'))
        return refreshed_user
    except firebase.AuthError as e:
        return {"error": str(e)}
