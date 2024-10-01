from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Функция для команды /start
def start(update, context):
    update.message.reply_text('Привет! Я бот для курса математики 10-11 классов.')

# Функция для обработки текстовых сообщений
def handle_message(update, context):
    text = update.message.text.lower()
    if "привет" in text:
        update.message.reply_text("Привет! Как могу помочь с математикой?")
    elif "формула" in text:
        update.message.reply_text("Могу подсказать формулы по алгебре и геометрии. Спрашивай!")
    else:
        update.message.reply_text("Я пока не знаю такой команды, но учусь :)")

# Основная функция запуска бота
def main():
    # Вставь свой токен сюда
    updater = Updater("ТВОЙ_ТОКЕН", use_context=True)
    dp = updater.dispatcher

    # Добавление команд
    dp.add_handler(CommandHandler("start", start))

    # Обработка обычных текстовых сообщений
    dp.add_handler(MessageHandler(Filters.text, handle_message))

    # Запуск бота
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
