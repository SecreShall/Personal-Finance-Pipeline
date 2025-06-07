import requests
from dotenv import load_dotenv
import os

load_dotenv()
client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")
partner_id = os.getenv("CLIENT_ID")

def get_auth(scope):

    AUTH_URL = "https://api-uat.unionbankph.com/partners/sb/convergent/v1/oauth2/authorize"

    params = {
        "client_id": client_id, 
        "response_type": "code",
        "redirect_uri": "http://localhost:8000/callback",
        "scope": scope,
        "type": "single"
    }

    response = requests.get(AUTH_URL, params=params)
    print(f"Redirect user to: {response.url}")  

def partner_auth(scope):

    TOKEN_URL = "https://api-uat.unionbankph.com/partners/sb/partners/v1/oauth2/authorize"

  
    headers = {
        "accept": "application/json",
        "content-type": "application/x-www-form-urlencoded",
        "x-client-id": client_id,
        "x-client-secret": client_secret
    }

    username = "partner_sb"
    password = "p@ssw0rd"


    data = {
        "grant_type": "password",
        "client_id": client_id,
        "username": username,
        "password": password,
        "scope": scope
    }

  
    response = requests.post(TOKEN_URL, data=data, headers=headers)

    print(response.status_code)  
    print(response.json())  

get_auth("account_inquiry")