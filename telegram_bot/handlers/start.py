from telebot import types
from bot import bot

def register_start_handlers():
    @bot.message_handler(commands=["start"])
    def start(message):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.row("🔎 Пошук манги", "🎲 Випадкова манга")
        markup.row("🔥 Топ манги", "❤️ Улюблене", "📘 Прочитане")
        bot.send_message(
            message.chat.id,
            "Привіт! Не знаєш, що прочитати? Давай допоможу☺️",
            reply_markup=markup
        )
