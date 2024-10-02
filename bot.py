from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler

# Функция для обработки команды /start
async def start(update: Update, context):
    await update.message.reply_text(f'Привіт, {update.effective_user.first_name}, цей бот створенно для навчання з математики!')

# Обрабатываем текстовые сообщения
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    text = message.text.lower()
    if "привіт" in text:
        bot.send_message(message.chat.id, "Привіт! Як я можу допомогти тобі з математикою?")
    elif "формула" in text:
        bot.send_message(message.chat.id, "Можу підсказати формули по алгебрі та геометрії. Запитуй!")
    else:
        bot.send_message(message.chat.id, "Я поки не знаю цього, але я вчусь :)")


# Основная функция для запуска бота
if __name__ == '__main__':
    # Вставьте ваш токен ниже
    TOKEN = '7876725841:AAH_XrZvJeiyqPtOwmfGZNIoacG7ZaI8W24'

    # Создаем приложение для бота
    app = ApplicationBuilder().token(TOKEN).build()

    # Добавляем команду /start
    app.add_handler(CommandHandler('start', start))

    # Запускаем бота
    app.run_polling()
