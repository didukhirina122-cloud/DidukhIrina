from telebot.types import ReplyKeyboardMarkup


def main_menu_kb():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row("🔎 Пошук манги", "🎲 Випадкова манга")
    markup.row("🔥 Топ манги", "❤️ Улюблене", "📘 Прочитане")
    return markup
