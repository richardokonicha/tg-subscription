import os
from dotenv import load_dotenv
load_dotenv()

TOKEN = os.getenv("TOKEN")
DEBUG = (os.getenv("DEBUG") == "True")
WEBHOOK_URL = os.getenv("WEBHOOK_URL")

