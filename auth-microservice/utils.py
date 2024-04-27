
import boto3
import json

def firebase_credential():
    ssm = boto3.client('ssm')
    response = ssm.get_parameter(Name='firebase-auth-microservice', WithDecryption=True)
    creds = response['Parameter']['Value']
    firebase = pyrebase.initialize_app(json.loads(creds))
    return firebase.auth()

def expire_at():
    pass