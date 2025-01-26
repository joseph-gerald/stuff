import os
from dotenv import load_dotenv

load_dotenv() 

PRIVATE_KEY = os.getenv("PRIVATE_KEY")
PUBLIC_KEY = os.getenv("PUBLIC_KEY")
API_KEY = os.getenv("API_KEY")
PASSWORD = os.getenv("PASSWORD")
PORT = os.getenv("PORT")