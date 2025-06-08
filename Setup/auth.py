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

  

get_auth("account_inquiry")