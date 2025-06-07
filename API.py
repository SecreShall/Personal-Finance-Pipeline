import os
from dotenv import load_dotenv
import requests

load_dotenv()
client_id = os.getenv("CLIENT_ID")  
client_secret = os.getenv("CLIENT_SECRET") 
partner_id = os.getenv("PARTNER_ID")
auth_code = os.getenv("AUTH_CODE")

def access_code():
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

    return data['token_type'], data['access_token']
