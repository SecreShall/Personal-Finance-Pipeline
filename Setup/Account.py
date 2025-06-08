import requests
import os
from dotenv import load_dotenv


try:
    load_dotenv()
    client_id = os.getenv("CLIENT_ID")
    client_secret = os.getenv("CLIENT_SECRET")
    password = os.getenv("PASSWORD")


    url = "https://api-uat.unionbankph.com/partners/sb/sandbox/v1/accounts"


    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "x-ibm-client-id": client_id,
        "x-ibm-client-secret": client_secret
    }


    account = {
            "username": "User1test1",
            "password": password,
            "account_name": "User1"
        }



    response = requests.post(url, headers=headers, json=account)


    print(response.status_code)  #
    print(response.json())  

except Exception as e:
            print(f"Account Created Failed... Error {e}")