from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler

# Функция для обработки команды /start
async def start(update: Update, context):
    await update.message.reply_text(f'Привет, {update.effective_user.first_name}!')

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
