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
        "redirect_uri": "https://ubpredirect.localtunnel.me/oauth/redirect",
        "code": auth_code
    }

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/x-www-form-urlencoded"
    }

    response = requests.post(TOKEN_URL, data=data, headers=headers)

    data = response.json()

    return data['token_type'], data['access_token']
    



def sample(type, code):
    TRANSACTIONS_URL = "https://api-uat.unionbankph.com/partners/sb/portal/online/accounts/v1/transactions"

    params = {
        "fromDate": "2017-01-01",
        "toDate": "2017-12-31",
        "tranType": "D"
    }
 
    headers = {
        "Accept": "application/json",
        "content-type": "application/json",
        "x-ibm-client-id": client_id,
        "x-ibm-client-secret": client_secret,
        "Authorization": f"{type} {code}",
        "x-partner-id": partner_id
    }
    
    response = requests.get(TRANSACTIONS_URL, params=params, headers=headers)

    print(response.status_code) 
    print(response.json()) 
 
