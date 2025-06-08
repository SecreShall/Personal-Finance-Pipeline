import pandas as pd
import os
import requests
from dotenv import load_dotenv
from access_token import get_valid_token


load_dotenv()
client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET") 
partner_id = os.getenv("PARTNER_ID")


def extract(auth_code):
    TRANSACTIONS_URL = "https://api-uat.unionbankph.com/partners/sb/portal/online/accounts/v1/transactions"

    #token = get_valid_token(auth_code)  

    token = "AAIkNGEyN2I2OTUtNTgxZS00MGZiLWIyN2MtMWZhZTczYTkxNzUxY5IYHWb4-6-AlOFGHhRiV-2TdIRstJxBqz3MH11g_LZNwclbnWJzanjsl-IJbySi2qqqOeu5DERPhfTzhwktP2pGW-SqXdhkN1iNRKoD2FxYFHgDr8jNshvnIM6OrSzxeDrWKwuTyqIlg6uAMIZMeHviTGJpiXD3VOYKGPivSDWTt5JSsw4oizx38dyM218Khpwpec233gNUjfjXUE5x5LXKMY39c_lNqbzpGDyieHPG5HE_iB3QN6QLgE6CQF1EahZwOQGAE9en8dL13umOnbnsvr8MHl-1h0WBZEUoohSH71ts9ku5MpXOKL5ARqwfEcK_pK5uSpNtLPDj3Bsq3r2lBOPFyNa6Y0pJRPCqink"

    if not token:
        print("Error: No valid access token.")
        return None

    params = {
        "tranType": "D",
    }

    headers = {
        "Accept": "application/json",
        "content-type": "application/json",
        "x-ibm-client-id": client_id,
        "x-ibm-client-secret": client_secret,
        "Authorization": f"Bearer {token}",
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



auth_code = os.getenv("ACC_HIS_AUTH_CODE")
transactions_data = extract(auth_code)
if transactions_data:
    transformed_data = transform(transactions_data)
    load(transformed_data)