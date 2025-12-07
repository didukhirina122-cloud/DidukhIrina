import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TOKEN")
API_URL = "https://api.mangadex.org"

FAV_FILE = "favorites.json"
READ_FILE = "read.json"