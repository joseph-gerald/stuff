import os
from dotenv import load_dotenv
from tronpy.keys import PrivateKey

load_dotenv() 

WALLETS = []
WALLETS_LENGTH = os.getenv("WALLETS")

for i in range(1, int(WALLETS_LENGTH) + 1):
    public_key = os.getenv(f"{i}_PUB")
    private_key = os.getenv(f"{i}_PRI")
    password = os.getenv(f"{i}_PAS")
    
    WALLETS.append({
        "public_key": public_key,
        "private_key": private_key,
        "password": password
    })

API_KEY = os.getenv("API_KEY")
PORT = os.getenv("PORT")