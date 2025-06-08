import pandas as pd
import os
import requests
from dotenv import load_dotenv
from token_handler import get_valid_token
from datetime import datetime, timedelta
import psycopg2


load_dotenv()
client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET") 
partner_id = os.getenv("PARTNER_ID")


def extract(auth_code):
    TRANSACTIONS_URL = "https://api-uat.unionbankph.com/partners/sb/portal/online/accounts/v1/transactions"

    #token = get_valid_token(auth_code)  

    token = "AAIkNGEyN2I2OTUtNTgxZS00MGZiLWIyN2MtMWZhZTczYTkxNzUxY5IYHWb4-6-AlOFGHhRiV-2TdIRstJxBqz3MH11g_LZNwclbnWJzanjsl-IJbySi2qqqOeu5DERPhfTzhwktP2pGW-SqXdhkN1iNRKoD2FxYFHgDr8jNshvnIM6OrSzxeDrWKwuTyqIlg6uAMIZMeHviTGJpiXD3VOYKGPivSDWTt5JSsw4oizx38dyM218Khpwpec233gNUjfjXUE5x5LXKMY39c_lNqbzpGDyieHPG5HE_iB3QN6QLgE6CQF1EahZwOQGAE9en8dL13umOnbnsvr8MHl-1h0WBZEUoohSH71ts9ku5MpXOKL5ARqwfEcK_pK5uSpNtLPDj3Bsq3r2lBOPFyNa6Y0pJRPCqink"

    yesterday = datetime.now() - timedelta(days=1)
    fromDate = yesterday.strftime("%Y-%m-%d")
    toDate = yesterday.strftime("%Y-%m-%d")

    params = {
        #"fromDate": fromDate,
        #"toDate": toDate,
        #"tranType": "D",
    }

    headers = {
        "Accept": "application/json",
        "content-type": "application/json",
        "x-ibm-client-id": client_id,
        "x-ibm-client-secret": client_secret,
        "Authorization": f"Bearer {token}",
        "x-partner-id": partner_id
    }
    
    response = requests.get(TRANSACTIONS_URL, params=params,  headers=headers)

    if (response.status_code) == 200:
        return response.json()
    else:
        print(response.text)
        return None

def transform(data):
    df = pd.DataFrame(columns=['transaction_id', 'transaction_type', 'amount', 'currency', 'transaction_date', 'remarks', 'balance', 'posted_date'])

    if None in data:
        return False
    else:
        for record in data['records']:
            dict = {
                'transaction_id': record['tranId'], 
                'transaction_type': record['tranType'], 
                'amount': record['amount'], 
                'currency': record['currency'], 
                'transaction_date': record['tranDate'], 
                'remarks': record['remarks'], 
                'balance': record['balance'], 
                'posted_date': record['postedDate']
                }
            df = pd.concat([df, pd.DataFrame(dict,index=[0])])
            transformed_data = df.reset_index(drop=True)

        transformed_data['transaction_type'] = transformed_data['transaction_type'].str.replace('D', 'Debit').replace('C', 'Credit')

        transformed_data['transaction_date'] = transformed_data['transaction_date'].str.replace('T', ' ')
        transformed_data['posted_date'] = transformed_data['posted_date'].str.replace('T', ' ')
        transformed_data['transaction_date'] = transformed_data['transaction_date'].str[:-4]
        transformed_data['posted_date'] = transformed_data['posted_date'].str[:-4]

        return transformed_data

def load(data):
    if data is not None and isinstance(data, pd.DataFrame) and not data.empty:
        try:
          
            load_dotenv()
            password_key = os.getenv("DB_PASS")

            connection = psycopg2.connect(
                host='localhost',
                database='demo',
                user='postgres',
                password=password_key
            )
            cursor = connection.cursor()


            insert_query = "INSERT INTO transactions (transaction_id, transaction_type, amount, currency, transaction_date, remarks, balance, posted_date) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"

            values = [tuple(row) for row in data.itertuples(index=False, name=None)]


            cursor.executemany(insert_query, values)
            connection.commit()
            print("Insert successful...")

        except Exception as e:
            print(f"Insertion failed... Error {e}")
        
        finally:
            cursor.close()
            connection.close()
    else:
        pass



auth_code = os.getenv("ACC_HIS_AUTH_CODE")
transactions_data = extract(auth_code)
if transactions_data:
    transformed_data = transform(transactions_data)
    load(transformed_data)