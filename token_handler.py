import os
from dotenv import load_dotenv
import requests
import time

load_dotenv()
client_id = os.getenv("CLIENT_ID")  
client_secret = os.getenv("CLIENT_SECRET") 
token_expiry = 0
refresh_token = None

def customer_token(auth_code):
    global token_expiry, refresh_token  

    TOKEN_URL = "https://api-uat.unionbankph.com/partners/sb/customers/v1/oauth2/token"
    

    data = {
        "grant_type": "authorization_code",
        "client_id": client_id,
        "redirect_uri": "http://localhost:8000/callback",
        "code": auth_code
    }

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/x-www-form-urlencoded"
    }

    response = requests.post(TOKEN_URL, data=data, headers=headers)
    data = response.json()

    if "access_token" in data:
        token_expiry = time.time() + data.get("expires_in", 3600)  
        refresh_token = data.get("refresh_token") 
        return data["access_token"]
    else:
        print("Error: Failed to retrieve access token")
        return None

def refresh_access_token():
    global token_expiry

    REFRESH_URL = "https://api.unionbankph.com/oauth/token"

    if not refresh_token:
        print("Error: No refresh token available.")
        return None

    payload = {
        "grant_type": "refresh_token",
        "refresh_token": refresh_token,
        "client_id": client_id,
        "client_secret": client_secret
    }

    response = requests.post(REFRESH_URL, data=payload)

    if response.status_code == 200:
        new_data = response.json()
        token_expiry = time.time() + new_data.get("expires_in", 3600)
        return new_data["access_token"]
    else:
        print(f"Error refreshing token: {response.text}")
        return None

def get_valid_token(auth_code):
    if auth_code is None:
        print("Error: auth_code is required but not provided.")
        return None
    if time.time() >= token_expiry:
        return refresh_access_token() or customer_token(auth_code)
    return customer_token(auth_code)

def partner_token(scope):

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

