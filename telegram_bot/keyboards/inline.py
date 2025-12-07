from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton


def manga_list_kb(results):
    markup = InlineKeyboardMarkup()
    for manga in results:
        name = manga["attributes"]["title"].get("en") or \
               next(iter(manga["attributes"]["title"].values()))
        markup.add(InlineKeyboardButton(name, callback_data=f"manga_{manga['id']}"))
    return markup
