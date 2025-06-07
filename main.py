import pandas as pd
import os
import requests
from dotenv import load_dotenv
import json

load_dotenv()
client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET") 
partner_id = os.getenv("PARTNER_ID")


def extract(type):
    code = os.getenv("ACC_HIS_ACCESS_CODE")
    TRANSACTIONS_URL = "https://api-uat.unionbankph.com/partners/sb/portal/online/accounts/v1/transactions"

    params = {
        "tranType": "D",
    }

    headers = {
        "Accept": "application/json",
        "content-type": "application/json",
        "x-ibm-client-id": client_id,
        "x-ibm-client-secret": client_secret,
        "Authorization": f"{type} {code}",
        "x-partner-id": "01bbb51e-1e6c-4bd4-af9c-450957522aac"
    }
    
    response = requests.get(TRANSACTIONS_URL, params=params,  headers=headers)

    return response.json()

def transform(data):
    df = pd.DataFrame(columns=['id', 'transactionID', 'transactionType', 'amount', 'currency', 'transactionDate', 'remarks', 'balance', 'postedDate'])


    for record in data['records']:
        dict = {
            'id': record['recordNumber'], 
            'transactionID': record['tranId'], 
            'transactionType': record['tranType'], 
             'amount': record['amount'], 
            'currency': record['currency'], 
            'transactionDate': record['tranDate'], 
            'remarks': record['remarks'], 
            'balance': record['balance'], 
            'postedDate': record['postedDate']
            }

        df = pd.concat([df, pd.DataFrame(dict,index=[0])])
        df = df.reset_index(drop=True)

    print(df)

def load(data_frame):
    pass

transform(extract("Bearer"))