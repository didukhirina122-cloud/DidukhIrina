import telebot

def main_menu():
    # Create main menu keyboard
    # Створення головного меню клавіатури
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row("🔎 Пошук манги", "🎲 Випадкова манга")
    markup.row("🔥 Топ манги", "❤️ Улюблене", "📘 Прочитане")
    return markup