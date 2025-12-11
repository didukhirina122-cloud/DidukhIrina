import os
import telebot
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('TOKEN')

bot = telebot.TeleBot(TOKEN)

API_URL = "https://api.mangadex.org"
FAV_FILE = "favorites.json"
READ_FILE = "read.json"