import telebot

def search_results_markup(results):
    # Generate buttons for search results
    # Генерація кнопок для результатів пошуку
    markup = telebot.types.InlineKeyboardMarkup()
    for manga in results:
        name = manga["attributes"]["title"].get("en") or next(iter(manga["attributes"]["title"].values()))
        markup.add(telebot.types.InlineKeyboardButton(name, callback_data=f"manga_{manga['id']}"))
    return markup

def manga_details_markup(manga_id):
    # Buttons under manga info
    # Кнопки під інформацією про мангу
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton("➕ Додати", callback_data=f"add_{manga_id}"))
    markup.add(telebot.types.InlineKeyboardButton("🌐 Відкрити на MangaDex", url=f"https://mangadex.org/title/{manga_id}"))
    markup.add(telebot.types.InlineKeyboardButton("⬅ Назад", callback_data="back"))
    return markup

def add_options_markup(manga_id):
    # Buttons to choose where to add manga
    # Кнопки вибору, куди додати мангу
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton("❤️ Улюблене", callback_data=f"addfav_{manga_id}"))
    markup.add(telebot.types.InlineKeyboardButton("📘 Прочитане", callback_data=f"addread_{manga_id}"))
    return markup