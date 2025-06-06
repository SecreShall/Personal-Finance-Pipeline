import requests
import os
from dotenv import load_dotenv
import json

# Load API credentials from .env file
load_dotenv()
client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")
password = os.getenv("PASSWORD")

# UnionBank Sandbox API URL
url = "https://api-uat.unionbankph.com/partners/sb/sandbox/v1/accounts"

# Headers for authentication
headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "x-ibm-client-id": client_id,
    "x-ibm-client-secret": client_secret
}

# Request body for account creation
account = {
        "username": "account_sample",
        "password": password,
        "account_name": "User1"
    }



response = requests.post(url, headers=headers, json=account)

# Print API response
print(response.status_code)  # Check if successful (200)
print(response.json())  # Show created account details