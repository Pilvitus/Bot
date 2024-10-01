import os
import telebot
from flask import Flask, request

app = Flask(__name__)
bot = telebot.TeleBot(os.environ['7876725841:AAH_XrZvJeiyqPtOwmfGZNIoacG7ZaI8W24'])

# Устанавливаем маршрут для обработки сообщений
@app.route('/' + os.environ['7876725841:AAH_XrZvJeiyqPtOwmfGZNIoacG7ZaI8W24'], methods=['POST'])
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
    bot.set_webhook(url=f'https://Bot.railway.app/{os.environ["7876725841:AAH_XrZvJeiyqPtOwmfGZNIoacG7ZaI8W24"]}')
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
