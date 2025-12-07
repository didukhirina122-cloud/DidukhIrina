from bot import bot
from api import search_manga, get_random_manga
from helpers import add_to_list, get_user_list
from keyboards.inline import manga_list_keyboard
from keyboards.reply import main_menu
from send_info import send_manga_info
import requests
from config import API_URL

def register_message_handlers():

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

        bot.send_message(message.chat.id, "🔎 Знайдено:", reply_markup=manga_list_keyboard(results))

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
            bot.send_message(message.chat.id, "Помилка 😢")
            return

        bot.send_message(message.chat.id, "🔥 Топ манги:", reply_markup=manga_list_keyboard(results))

    @bot.message_handler(func=lambda m: m.text == "❤️ Улюблене")
    def show_favorites(message):
        user_list = get_user_list(message.chat.id, "favorites.json")
        if not user_list:
            bot.send_message(message.chat.id, "Список улюблених порожній 😢")
            return

        items = []
        for manga_id in user_list:
            r = requests.get(f"{API_URL}/manga/{manga_id}", params={"includes[]": ["cover_art"]}).json()
            if "data" in r:
                items.append(r["data"])

        bot.send_message(message.chat.id, "❤️ Улюблене:", reply_markup=manga_list_keyboard(items))

    @bot.message_handler(func=lambda m: m.text == "📘 Прочитане")
    def show_read(message):
        user_list = get_user_list(message.chat.id, "read.json")
        if not user_list:
            bot.send_message(message.chat.id, "Список прочитаного порожній 😢")
            return

        items = []
        for manga_id in user_list:
            r = requests.get(f"{API_URL}/manga/{manga_id}", params={"includes[]": ["cover_art"]}).json()
            if "data" in r:
                items.append(r["data"])

        bot.send_message(message.chat.id, "📘 Прочитане:", reply_markup=manga_list_keyboard(items))
