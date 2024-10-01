import os
import telebot
from flask import Flask, request

app = Flask(__name__)
bot = telebot.TeleBot(os.environ['7876725841:AAH_XrZvJeiyqPtOwmfGZNIoacG7ZaI8W24'])

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
