import os
from dotenv import load_dotenv
import requests

load_dotenv()
client_id = os.getenv("CLIENT_ID")  
client_secret = os.getenv("CLIENT_SECRET") 


def get_token(auth_code):
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

    print(data['access_token'])

def part(auth_code):
    pass

get_token(os.getenv("ACC_HIS_AUTH_CODE"))