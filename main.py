import pandas as pd
import os
import requests
from dotenv import load_dotenv

load_dotenv()
client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET") 
partner_id = os.getenv("PARTNER_ID")

def extract(type, code):
    TRANSACTIONS_URL = "https://api-uat.unionbankph.com/partners/sb/portal/online/accounts/v1/transactions"

    params = {
        "fromDate": "2017-01-01",
        "toDate": "2017-12-31",
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

    return response.json() 

def transform(data):
    pass

def load(data_frame):
    pass