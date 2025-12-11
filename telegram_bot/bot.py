from config import bot
import handlers.start
import handlers.messages
import handlers.callbacks

if __name__ == "__main__":
    print("Bot is running...")
    bot.polling(none_stop=True)