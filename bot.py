import os
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from flask import Flask, request

app = Flask(__name__)

# Функция для команды /start
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Привет! Я бот для курса математики 10-11 классов. Спрашивай меня о формулах, задачах и теории!')

# Функция для обработки всех текстовых сообщений
def handle_message(update: Update, context: CallbackContext) -> None:
    text = update.message.text.lower()  # Приводим текст к нижнему регистру для удобства обработки
    if "привет" in text:
        update.message.reply_text("Привет! Как могу помочь с математикой?")
    elif "формула" in text:
        update.message.reply_text("Могу подсказать формулы по алгебре и геометрии. Спрашивай!")
    else:
        update.message.reply_text("Я пока не знаю такой команды, но учусь :)")

# Основная функция запуска бота
def main() -> None:
    # Вставь свой токен сюда
    TOKEN = os.environ['TELEGRAM_TOKEN']

    # Создаем объект Updater для связи с Telegram API
    updater = Updater(TOKEN)

    # Получаем диспетчер для регистрации обработчиков
    dp = updater.dispatcher

    # Регистрируем обработчик команды /start
    dp.add_handler(CommandHandler("start", start))

    # Регистрируем обработчик текстовых сообщений
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))  # Обработка всех текстовых сообщений

    # Запускаем бота
    updater.start_polling()
    updater.idle()  # Ожидаем завершения

@app.route('/' + os.environ['TELEGRAM_TOKEN'], methods=['POST'])
def webhook():
    json_str = request.get_json(force=True)
    update = Update.de_json(json_str, bot)
    dp.process_update(update)
    return '!', 200

@app.route('/')
def index():
    return 'Webhook is set up!', 200

if __name__ == '__main__':
    main()
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
