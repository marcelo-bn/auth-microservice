# Authentication Microservice with Chalice and Firebase

This microservice provides authentication functionality using Chalice, an AWS Serverless Microframework for Python, and Firebase Authentication.

### Prerequisites
Before using this microservice, ensure you have the following:

* Python 3.7 or later installed on your machine.
* AWS credentials configured locally with appropriate permissions.
* Access to the AWS Systems Manager Parameter Store to retrieve Firebase credentials securely.
* Firebase project set up with authentication enabled. You can create a Firebase project from the Firebase Console.
* Firebase Admin SDK service account JSON file. This file should be stored securely in the AWS Systems Manager Parameter Store.

### Installation
1. Clone this repository to your local machine:

2. Install Chalice and other dependencies:
    ```
    pip install -r requirements.txt
    ```

### Configuration
1. Upload your Firebase Admin SDK service account JSON file to the AWS Systems Manager Parameter Store with a parameter name like firebase-auth-microservice.

2. Configure your AWS credentials locally by running:
    ```
    aws configure
    ```

3. Modify the app.py file:
    * Replace 'firebase-auth-microservice' with your actual parameter name in the ssm.get_parameter(Name=...) line.
    * Customize routes and functions according to your requirements.

### Deploying the Microservice
Deploy the microservice using Chalice:
```
chalice deploy
```

### Usage
#### Signing Up
To register a new user, send a POST request to /signup with a JSON body containing the user's email and password:
```
curl -X POST \
  -H "Content-Type: application/json" \
  -d '{"email": "example@example.com", "password": "yourpassword"}' \
  https://your-chalice-api-url/signup
```

#### Logging In
To authenticate a user, send a POST request to /login with a JSON body containing the user's email and password:
```
curl -X POST \
  -H "Content-Type: application/json" \
  -d '{"email": "example@example.com", "password": "yourpassword"}' \
  https://your-chalice-api-url/login
```

#### Refreshing Token
To refresh the authentication token, send a POST request to /refresh with a JSON body containing the user's refresh token:
```
curl -X POST \
  -H "Content-Type: application/json" \
  -d '{"refresh_token": "your_refresh_token"}' \
  https://your-chalice-api-url/refresh
```

### Additional Notes
* Ensure proper security measures are implemented, such as HTTPS and authentication checks.
* Review the Chalice and Firebase documentation for advanced usage and customization options.
