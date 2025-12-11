import requests
import random
import telebot
from config import bot, API_URL, FAV_FILE, READ_FILE
from keyboards.inline import search_results_markup, manga_details_markup
from states.user_states import get_user_list


def search_manga_api(title, limit=5):
    # Search manga via API
    # Пошук манги через API
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
    # Extract cover URL
    # Отримання посилання на обкладинку
    manga_id = manga["id"]
    for rel in manga["relationships"]:
        if rel["type"] == "cover_art":
            file_name = rel["attributes"]["fileName"]
            return f"https://uploads.mangadex.org/covers/{manga_id}/{file_name}"
    return None


def get_random_manga_api():
    # Get random manga
    # Отримання випадкової манги
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


def send_manga_info(chat_id, manga):
    # Send formatted manga info card
    # Відправка відформатованої картки манги
    info = manga["attributes"]
    manga_id = manga["id"]

    name = info["title"].get("en") or next(iter(info["title"].values()))
    cover = get_cover_url(manga)
    markup = manga_details_markup(manga_id)

    if cover:
        bot.send_photo(chat_id, cover, caption=f"*{name}*", parse_mode="Markdown", reply_markup=markup)
    else:
        bot.send_message(chat_id, f"*{name}*", parse_mode="Markdown", reply_markup=markup)


# --- Handlers ---
# --- Обробники ---

@bot.message_handler(func=lambda m: m.text == "🔎 Пошук манги")
def menu_search(message):
    msg = bot.send_message(message.chat.id, "Введи назву манги:")
    bot.register_next_step_handler(msg, process_search)


def process_search(message):
    title = message.text.strip()
    results = search_manga_api(title)

    if not results:
        bot.send_message(message.chat.id, "Мангу не знайдено 😢")
        return

    bot.send_message(message.chat.id, "🔎 Знайдено:", reply_markup=search_results_markup(results))


@bot.message_handler(func=lambda m: m.text == "🎲 Випадкова манга")
def random_manga_handler(message):
    manga = get_random_manga_api()
    if not manga:
        bot.send_message(message.chat.id, "Не вдалося отримати мангу 😢")
        return
    send_manga_info(message.chat.id, manga)


@bot.message_handler(func=lambda m: m.text == "🔥 Топ манги")
def top_manga(message):
    results = search_manga_api("", limit=5)
    if not results:
        bot.send_message(message.chat.id, "Не вдалося отримати топ 😢")
        return
    bot.send_message(message.chat.id, "🔥 Топ манги:", reply_markup=search_results_markup(results))


def show_list(message, filename, title_text):
    # Helper to show lists (read/fav)
    # Помічник для показу списків
    user_list = get_user_list(message.chat.id, filename)
    if not user_list:
        bot.send_message(message.chat.id, f"Список {title_text} порожній 😢")
        return

    markup = telebot.types.InlineKeyboardMarkup()
    for manga_id in user_list:
        # Fetching details for each saved ID (can be slow, but simple)
        r = requests.get(f"{API_URL}/manga/{manga_id}", params={"includes[]": ["cover_art"]}).json()
        if "data" in r:
            manga = r["data"]
            name = manga["attributes"]["title"].get("en") or next(iter(manga["attributes"]["title"].values()))
            markup.add(telebot.types.InlineKeyboardButton(name, callback_data=f"manga_{manga['id']}"))

    bot.send_message(message.chat.id, f"{title_text}:", reply_markup=markup)


@bot.message_handler(func=lambda m: m.text == "❤️ Улюблене")
def show_favorites(message):
    show_list(message, FAV_FILE, "❤️ Улюблене")


@bot.message_handler(func=lambda m: m.text == "📘 Прочитане")
def show_read(message):
    show_list(message, READ_FILE, "📘 Прочитане")