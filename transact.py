import os
import requests
from dotenv import load_dotenv


load_dotenv()
client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET") 
partner_id = os.getenv("PARTNER_ID")


def bal():
    URI = "https://api-uat.unionbankph.com/partners/sb/accounts/v2/balances/106142386237"

    header = {
        "accept": "application/json" ,
        "content-type": "application/json" ,
        "x-ibm-client-id": client_id ,
        "x-ibm-client-secret": client_secret
    }
    
    response = requests.get(URI, headers=header)

    print(response.status_code) 
    print(response.json())  

def transfer():
    URL = "https://api-uat.unionbankph.com/partners/sb/partners/v3/transfers/single"

    token = os.getenv("TRAN_ACCESS")

    header = {
        "accept": "application/json" ,
        "content-type": "application/json" ,
        "x-ibm-client-id": client_id ,
        "x-ibm-client-secret": client_secret,
        "authorization": f"Bearer {token}",
        "x-partner-id": "5dff2cdf-ef15-48fb-a87b-375ebff415bb"
    }

    data = {
        "senderRefId": "UB12342389423427",
        "tranRequestDate": "2024-10-10T12:11:50.333",
        "accountNo": "106142386237",
        "amount": {
            "currency": "PHP",
            "value": "11234"
        },
        "remarks": "Transfer remarks",
        "particulars": "Transfer particulars",
        "info": [
            {
            "index": 1,
            "name": "Recipient",
            "value": "Juan Dela Cruz"
            },
            {
            "index": 2,
            "name": "Message",
            "value": "Happy Birthday"
            }
        ]     
    }

    response = requests.post(URL, json=data,  headers=header)

    print(response.status_code) 
    print(response.json())  

def transfer2():
   
    TRANSFER_URL = "https://api-uat.unionbankph.com/partners/sb/ubp/v1/transfers"

    token = os.getenv("TRAN_ACCESS")

   
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "x-ibm-client-id": client_id,
        "x-ibm-client-secret": client_secret,
        "authorization": f"Bearer {token}",
        "x-partner-id": partner_id
    }

 
    data = {
        "senderRefId": "000001",
        "tranRequestDate": "2019-08-16T07:37:16.333",
        "amount": {
            "currency": "PHP",
            "value": "100"
        },
        "accountNumber": "102110024391",
        "remarks": "Transfer remarks",
        "particulars": "Transfer particulars",
        "sender": {
            "name": "API Team",
            "address": {
            "line1": "UnionBank",
            "line2": "Meralco Avenue",
            "city": "Pasig",
            "province": "Metro Manila",
            "zipCode": "1990",
            "country": "Philippines"
            }
        },
        "beneficiary": {
            "name": "Juan dela Cruz",
            "address": {
            "line1": "UnionBank",
            "line2": "Meralco Avenue",
            "city": "Pasig",
            "province": "Metro Manila",
            "zipCode": "1990",
            "country": "Philippines"
            }
        },
        "validateBeneficiary": "false",
        "msb": "true"
    }

 
    response = requests.post(TRANSFER_URL, json=data, headers=headers)

  
    print(response.status_code) 
    print(response.text)  

def check():
 
    SENDER_REF_ID = "00001" 
    TRANSFER_URL = f"https://api-uat.unionbankph.com/partners/sb/online/v1/transfers/single/{SENDER_REF_ID}"

    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "x-ibm-client-id": client_id,
        "x-ibm-client-secret": client_secret,
        "x-partner-id": partner_id
    }


    response = requests.get(TRANSFER_URL, headers=headers)

    print(response.status_code) 
    print(response.json())  

def cash():
    TRANSFER_URL = "https://api-uat.unionbankph.com/partners/sb/partners/cashin/v1/single"

    token = os.getenv("SAND_ACCESS")


    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "x-ibm-client-id": client_id,
        "x-ibm-client-secret": client_secret,
        "authorization": f"Bearer {token}"
    }

    data = {
        "senderRefId": "UBAB01770",
        "tranRequestDate": "2020-02-03T12:50:59.123",
        "accountNo": "109594480006",
        "amount": {
            "currency": "PHP",
            "value": "1.00"
        },
        "remarks": "Transfer remarks",
        "particulars": "Transfer particulars",
        "info": [
            {
            "index": 1,
            "name": "Recipient",
            "value": "Juan Dela Cruz"
            },
            {
            "index": 2,
            "name": "Message",
            "value": "Happy Birthday"
            }
        ]
    }

    response = requests.post(TRANSFER_URL, json=data, headers=headers)

    print(response.status_code) 
    print(response.text)  

def intrac():
  
    SENDER_REF_ID = "002"  
    TRANSFER_URL = f"https://api-uat.unionbankph.com/partners/sb/ubp/v1/transfers/{SENDER_REF_ID}"


    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "x-ibm-client-id": client_id,
        "x-ibm-client-secret": client_secret,
        "x-partner-id": partner_id
    }

    
    response = requests.get(TRANSFER_URL, headers=headers)

 
    print(response.status_code)  
    print(response.json())  

def account():
    URL = "https://api-uat.unionbankph.com/partners/sb/accounts/v1/info"
    token = os.getenv("ACC_ACCESS")  

    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "x-ibm-client-id": client_id,
        "x-ibm-client-secret": client_secret,
        "authorization": f"Bearer {token}"
    }

    response = requests.get(URL, headers=headers)
    print(response.status_code)
    print(response.json())

transfer()