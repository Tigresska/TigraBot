# Импортируем нужные компоненты
from telegram.ext import Updater
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import settings

logging.basicConfig(format= '%(asctime)s - %(levelname)s - %(message)s',
                    filename='bot.log', 
                    level=logging.INFO)

def main():
    """
    Initialize bot
    """
    # Создаем бота и передаем ему ключ для авторизации на серверах Telegram
    mybot = Updater(settings.API_KEY, use_context=True) #request_kwargs=PROXY)
    
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))


    logging.info("Бот стартовал")
    # Командуем боту начать ходить в Telegram за сообщениями
    mybot.start_polling()
    # Запускаем бота, он будет работать, пока мы его не остановим принудительно
    mybot.idle()

def greet_user(update, context):
    text = "Вызван /start"
    logging.info(text)
    print(text)
    update.message.reply_text(text)

def talk_to_me(update, context):
    user_text = f"Привет {update.message.chat.first_name}! Ты написал: {update.message.text}"
    logging.info("User: %s, Chat id: %s, Message: %s",
                    update.message.chat.username,
                    update.message.chat.id,
                    update.message.text)
    print(update.message)
    update.message.reply_text(user_text)
# Вызываем функцию main() - именно эта строчка запускает бота
main()