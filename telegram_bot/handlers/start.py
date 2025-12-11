from config import bot
from keyboards.reply import main_menu


@bot.message_handler(commands=["start"])
def start(message):
    # 👇 ДОДАЙ ЦЕЙ РЯДОК 👇
    print(f"!!! ОТРИМАВ КОМАНДУ START від ID: {message.chat.id} !!!")

    bot.send_message(
        message.chat.id,
        "Привіт! Не знаєш, що прочитати? Давай допоможу☺️",
        reply_markup=main_menu()
    )