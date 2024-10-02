import os
import sys
import telebot
from flask import Flask, request

app = Flask(__name__)

# Проверяем наличие переменной окружения TELEGRAM_TOKEN
if 'TELEGRAM_TOKEN' not in os.environ:
    print("Ошибка: Переменная окружения TELEGRAM_TOKEN не установлена.")
    sys.exit(1)

bot = telebot.TeleBot(os.environ['TELEGRAM_TOKEN'])

# Устанавливаем обработчик команды /start
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет! Я бот для курса математики 10-11 классов. Спрашивай меня о формулах, задачах и теории!')

# Обрабатываем текстовые сообщения
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    text = message.text.lower()
    if "привет" in text:
        bot.send_message(message.chat.id, "Привет! Как могу помочь с математикой?")
    elif "формула" in text:
        bot.send_message(message.chat.id, "Могу подсказать формулы по алгебре и геометрии. Спрашивай!")
    else:
        bot.send_message(message.chat.id, "Я пока не знаю такой команды, но учусь :)")

# Устанавливаем маршрут для обработки сообщений от Telegram через вебхук
@app.route('/' + os.environ['TELEGRAM_TOKEN'], methods=['POST'])
def get_message():
    json_str = request.get_json(force=True)
    update = telebot.types.Update.de_json(json_str)
    bot.process_new_updates([update])
    return '!', 200

# Основной маршрут для проверки работы вебхука
@app.route('/')
def index():
    return 'Webhook is working!', 200

# Устанавливаем вебхук
if __name__ == '__main__':
    bot.remove_webhook()
    bot.set_webhook(url=f'https://bot-production-9fda.up.railway.app/{os.environ["TELEGRAM_TOKEN"]}')
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
