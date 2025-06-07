import requests
from dotenv import load_dotenv
import os

load_dotenv()
client_id = os.getenv("CLIENT_ID")
partner_id = os.getenv("CLIENT_ID")

AUTH_URL = "https://api-uat.unionbankph.com/partners/sb/customers/v1/oauth2/authorize"

params = {
    "client_id": client_id, 
    "response_type": "code",
    "redirect_uri": "http://localhost:8000/callback",
    "scope": "account_inquiry",
    "type": "single",
    "partnerId": partner_id
}

response = requests.get(AUTH_URL, params=params)
print(f"Redirect user to: {response.url}")  
