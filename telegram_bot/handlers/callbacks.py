import requests
from config import bot, API_URL, FAV_FILE, READ_FILE
from keyboards.inline import add_options_markup
from states.user_states import add_to_list
from handlers.messages import send_manga_info


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
    bot.send_message(call.message.chat.id, "Куди додати мангу?", reply_markup=add_options_markup(manga_id))

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
    # We can delete the message or send the main menu prompt again
    # Можна видалити повідомлення або відправити меню знову
    from handlers.start import start
    start(call.message)