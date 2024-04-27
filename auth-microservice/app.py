from chalice import Chalice
import pyrebase

from utils import firebase_credential

app = Chalice(app_name='auth-microservice')

@app.route("/signup", methods=["POST"])
def signup():
    try:
        body = app.current_request.json_body
        email = body.get('email')
        password = body.get('password')
        user = firebase_credential.create_user_with_email_and_password(email, password)
        return {"user": user}, 200
    except Exception as e:
        return {"error": str(e)}, 500
    
@app.route("/login", methods=["POST"])
def login():
    try:
        body = app.current_request.json_body
        email = body.get('email')
        password = body.get('password')
        user = firebase_credential.sign_in_with_email_and_password(email, password)
        return {"user": user}, 200
    except Exception as e:
        return {"error": str(e)}, 500

@app.route("/refresh", methods=["POST"])
def refresh():
    try:
        body = app.current_request.json_body
        refresh_token = body.get('refresh_token')
        refreshed_user = firebase_credential.refresh(refresh_token)
        return {"id_token": refreshed_user}, 200
    except Exception as e:
        return {"error": str(e)}, 500