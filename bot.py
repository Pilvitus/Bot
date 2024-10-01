import os
import telebot
from flask import Flask, request

app = Flask(__name__)
bot = telebot.TeleBot(os.environ['TELEGRAM_TOKEN'])

@app.route('/' + os.environ['TELEGRAM_TOKEN'], methods=['POST'])
def get_message():
    json_str = request.get_json(force=True)
    update = telebot.types.Update.de_json(json_str)
    bot.process_new_updates([update])
    return '!', 200

@app.route('/')
def webhook():
    return 'Webhook is set up!', 200

if __name__ == '__main__':
    bot.remove_webhook()
    bot.set_webhook(url='https://<your-app-name>.railway.app/' + os.environ['TELEGRAM_TOKEN'])
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))








from telegram.ext import Updater, CommandHandler, MessageHandler, filters

# Функция для команды /start
def start(update, context):
    update.message.reply_text('Привет! Я бот для курса математики 10-11 классов. Спрашивай меня о формулах, задачах и теории!')

# Функция для обработки текстовых сообщений
def handle_message(update, context):
    text = update.message.text.lower()  # Приводим текст к нижнему регистру для удобства обработки
    if "привет" in text:
        update.message.reply_text("Привет! Как могу помочь с математикой?")
    elif "формула" in text:
        update.message.reply_text("Могу подсказать формулы по алгебре и геометрии. Спрашивай!")
    else:
        update.message.reply_text("Я пока не знаю такой команды, но учусь :)")

# Основная функция запуска бота
def main():
    # Вставь свой токен сюда
    TOKEN = "7876725841:AAH_XrZvJeiyqPtOwmfGZNIoacG7ZaI8W24"

    # Создаем объект Updater для связи с Telegram API
    updater = Updater(TOKEN)

    # Получаем диспетчер для регистрации обработчиков
    dp = updater.dispatcher

    # Регистрируем обработчик команды /start
    dp.add_handler(CommandHandler("start", start))

    # Регистрируем обработчик текстовых сообщений
    dp.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Запускаем бота
    updater.start_polling()

    # Бот будет работать, пока его не остановят
    updater.idle()

# Запускаем бота
if __name__ == '__main__':
    main()

