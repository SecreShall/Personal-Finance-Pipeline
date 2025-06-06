import os
from dotenv import load_dotenv
import requests

load_dotenv()
client_id = os.getenv("CLIENT_ID")  # Load client ID from .env
client_secret = os.getenv("CLIENT_SECRET")  # Load client secret from .env
auth_code = os.getenv("AUTH_CODE")

def access_code():
    TOKEN_URL = "https://api-uat.unionbankph.com/partners/sb/customers/v1/oauth2/token"

    data = {
        "grant_type": "authorization_code",
        "client_id": client_id,
        "redirect_uri": "https://ubpredirect.localtunnel.me/oauth/redirect",
        "code": auth_code
    }

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/x-www-form-urlencoded"
    }

    response = requests.post(TOKEN_URL, data=data, headers=headers)

    print(response.status_code)
    print(response.json()) 

    # Filter JSON and return access_code



def sample(code):
    TRANSACTIONS_URL = "https://api-uat.unionbankph.com/partners/sb/portal/online/accounts/v1/transactions"
 
    headers = {
        "Accept": "application/json",
        "content-type": "application/json",
        "x-ibm-client-id": client_id,
        "x-ibm-client-secret": client_secret,
        "Authorization": f"Bearer {code}",
        "x-partner-id": "5dff2cdf-ef15-48fb-a87b-375ebff415bb"
    }
    
    response = requests.get(TRANSACTIONS_URL,  headers=headers)


    print(response.status_code) 
    print(response.json()) 
 
