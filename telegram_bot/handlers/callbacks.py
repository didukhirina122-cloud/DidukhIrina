from bot import bot
import requests
from config import API_URL
from helpers import add_to_list
from send_info import send_manga_info

def register_callback_handlers():

    @bot.callback_query_handler(func=lambda call: call.data.startswith("manga_"))
    def callback_show(call):
        bot.answer_callback_query(call.id)
        manga_id = call.data.replace("manga_", "")
        r = requests.get(f"{API_URL}/manga/{manga_id}", params={"includes[]": ["cover_art"]}).json()

        if "data" not in r:
            bot.send_message(call.message.chat.id, "Помилка 😢")
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
        added = add_to_list(call.from_user.id, manga_id, "favorites.json")
        bot.send_message(call.message.chat.id, "Додано ❤️" if added else "Вже є ❤️")

    @bot.callback_query_handler(func=lambda call: call.data.startswith("addread_"))
    def callback_add_read(call):
        bot.answer_callback_query(call.id)
        manga_id = call.data.replace("addread_", "")
        added = add_to_list(call.from_user.id, manga_id, "read.json")
        bot.send_message(call.message.chat.id, "Додано 📘" if added else "Вже є 📘")
