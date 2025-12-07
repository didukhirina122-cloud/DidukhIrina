import telebot
import requests
import os
import random
import json
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('TOKEN')
bot = telebot.TeleBot(TOKEN)


API_URL = "https://api.mangadex.org"

FAV_FILE = "favorites.json"
READ_FILE = "read.json"

# ------------------------------
# HELPER FUNCTIONS
# ------------------------------

def load_json(filename):
    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

def save_json(filename, data):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def add_to_list(user_id, manga_id, filename):
    data = load_json(filename)
    data.setdefault(str(user_id), [])
    if manga_id not in data[str(user_id)]:
        data[str(user_id)].append(manga_id)
        save_json(filename, data)
        return True
    return False

def get_user_list(user_id, filename):
    data = load_json(filename)
    return data.get(str(user_id), [])

# ------------------------------
# API FUNCTIONS
# ------------------------------

def search_manga(title, limit=5):
    url = f"{API_URL}/manga"
    params = {
        "title": title,
        "limit": limit,
        "includes[]": ["cover_art"],
        "contentRating[]": ["safe", "suggestive"]
    }
    r = requests.get(url, params=params).json()
    return r.get("data", [])

def get_cover_url(manga):
    manga_id = manga["id"]
    for rel in manga["relationships"]:
        if rel["type"] == "cover_art":
            file_name = rel["attributes"]["fileName"]
            return f"https://uploads.mangadex.org/covers/{manga_id}/{file_name}"
    return None

def get_random_manga():
    url = f"{API_URL}/manga"
    params = {
        "limit": 100,
        "includes[]": ["cover_art"],
        "contentRating[]": ["safe", "suggestive"]
    }
    r = requests.get(url, params=params)
    if r.status_code != 200:
        return None

    data = r.json().get("data", [])
    safe_list = [m for m in data if m["attributes"].get("contentRating") in ["safe", "suggestive"]]

    return random.choice(safe_list) if safe_list else None

# ------------------------------
# SEND INFO
# ------------------------------

def send_manga_info(chat_id, manga):
    info = manga["attributes"]
    manga_id = manga["id"]

    name = info["title"].get("en") or next(iter(info["title"].values()))
    cover = get_cover_url(manga)

    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton("➕ Додати", callback_data=f"add_{manga_id}"))
    markup.add(telebot.types.InlineKeyboardButton("🌐 Відкрити на MangaDex", url=f"https://mangadex.org/title/{manga_id}"))
    markup.add(telebot.types.InlineKeyboardButton("⬅ Назад", callback_data="back"))

    if cover:
        bot.send_photo(chat_id, cover, caption=f"*{name}*", parse_mode="Markdown", reply_markup=markup)
    else:
        bot.send_message(chat_id, f"*{name}*", parse_mode="Markdown", reply_markup=markup)

# ------------------------------
# HANDLERS
# ------------------------------

@bot.message_handler(commands=["start"])
def start(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row("🔎 Пошук манги", "🎲 Випадкова манга")
    markup.row("🔥 Топ манги", "❤️ Улюблене", "📘 Прочитане")
    bot.send_message(message.chat.id, "Привіт! Не знаєш, що прочитати? Давай допоможу☺️", reply_markup=markup)

@bot.message_handler(func=lambda m: m.text == "🔎 Пошук манги")
def menu_search(message):
    msg = bot.send_message(message.chat.id, "Введи назву манги:")
    bot.register_next_step_handler(msg, process_search)

def process_search(message):
    title = message.text.strip()
    results = search_manga(title)

    if not results:
        bot.send_message(message.chat.id, "Мангу не знайдено 😢")
        return

    markup = telebot.types.InlineKeyboardMarkup()
    for manga in results:
        name = manga["attributes"]["title"].get("en") or next(iter(manga["attributes"]["title"].values()))
        markup.add(telebot.types.InlineKeyboardButton(name, callback_data=f"manga_{manga['id']}"))

    bot.send_message(message.chat.id, "🔎 Знайдено:", reply_markup=markup)

@bot.message_handler(func=lambda m: m.text == "🎲 Випадкова манга")
def random_manga_handler(message):
    manga = get_random_manga()
    if not manga:
        bot.send_message(message.chat.id, "Не вдалося отримати мангу 😢")
        return
    send_manga_info(message.chat.id, manga)

@bot.message_handler(func=lambda m: m.text == "🔥 Топ манги")
def top_manga(message):
    results = search_manga("", limit=5)

    if not results:
        bot.send_message(message.chat.id, "Не вдалося отримати топ 😢")
        return

    markup = telebot.types.InlineKeyboardMarkup()
    for manga in results:
        name = manga["attributes"]["title"].get("en") or next(iter(manga["attributes"]["title"].values()))
        markup.add(telebot.types.InlineKeyboardButton(name, callback_data=f"manga_{manga['id']}"))

    bot.send_message(message.chat.id, "🔥 Топ манги:", reply_markup=markup)

@bot.message_handler(func=lambda m: m.text == "❤️ Улюблене")
def show_favorites(message):
    user_list = get_user_list(message.chat.id, FAV_FILE)
    if not user_list:
        bot.send_message(message.chat.id, "Список улюблених порожній 😢")
        return

    markup = telebot.types.InlineKeyboardMarkup()
    for manga_id in user_list:
        r = requests.get(f"{API_URL}/manga/{manga_id}", params={"includes[]": ["cover_art"]}).json()
        if "data" in r:
            manga = r["data"]
            name = manga["attributes"]["title"].get("en") or next(iter(manga["attributes"]["title"].values()))
            markup.add(telebot.types.InlineKeyboardButton(name, callback_data=f"manga_{manga['id']}"))

    bot.send_message(message.chat.id, "❤️ Улюблене:", reply_markup=markup)

@bot.message_handler(func=lambda m: m.text == "📘 Прочитане")
def show_read(message):
    user_list = get_user_list(message.chat.id, READ_FILE)
    if not user_list:
        bot.send_message(message.chat.id, "Список прочитаного порожній 😢")
        return

    markup = telebot.types.InlineKeyboardMarkup()
    for manga_id in user_list:
        r = requests.get(f"{API_URL}/manga/{manga_id}", params={"includes[]": ["cover_art"]}).json()
        if "data" in r:
            manga = r["data"]
            name = manga["attributes"]["title"].get("en") or next(iter(manga["attributes"]["title"].values()))
            markup.add(telebot.types.InlineKeyboardButton(name, callback_data=f"manga_{manga['id']}"))

    bot.send_message(message.chat.id, "📘 Прочитане:", reply_markup=markup)

# ------------------------------
# CALLBACKS
# ------------------------------

@bot.callback_query_handler(func=lambda call: call.data.startswith("manga_"))
def callback_show_manga(call):
    bot.answer_callback_query(call.id)

    manga_id = call.data.replace("manga_", "")
    r = requests.get(f"{API_URL}/manga/{manga_id}", params={"includes[]": ["cover_art"]}).json()

    if "data" not in r:
        bot.send_message(call.message.chat.id, "Помилка завантаження манги 😢")
        return

    send_manga_info(call.message.chat.id, r["data"])

@bot.callback_query_handler(func=lambda call: call.data.startswith("add_"))
def callback_add(call):
    bot.answer_callback_query(call.id)
    manga_id = call.data.replace("add_", "")

    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton("❤️ Улюблене", callback_data=f"addfav_{manga_id}"))
    markup.add(telebot.types.InlineKeyboardButton("📘 Прочитане", callback_data=f"addread_{manga_id}"))
    bot.send_message(call.message.chat.id, "Куди додати мангу?", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data.startswith("addfav_"))
def callback_add_fav(call):
    bot.answer_callback_query(call.id)
    manga_id = call.data.replace("addfav_", "")
    added = add_to_list(call.from_user.id, manga_id, FAV_FILE)
    if added:
        bot.send_message(call.message.chat.id, "Додано до улюблених ❤️")
    else:
        bot.send_message(call.message.chat.id, "Вже є у списку ❤️")

@bot.callback_query_handler(func=lambda call: call.data.startswith("addread_"))
def callback_add_read(call):
    bot.answer_callback_query(call.id)
    manga_id = call.data.replace("addread_", "")
    added = add_to_list(call.from_user.id, manga_id, READ_FILE)
    if added:
        bot.send_message(call.message.chat.id, "Додано до прочитаного 📘")
    else:
        bot.send_message(call.message.chat.id, "Вже є у списку 📘")

@bot.callback_query_handler(func=lambda call: call.data == "back")
def callback_back(call):
    bot.answer_callback_query(call.id)
    start(call.message)

# ------------------------------
# RUN
# ------------------------------

print("Bot is running...")
bot.polling(none_stop=True)
