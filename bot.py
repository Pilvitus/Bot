import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Функция для обработки команды /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Привет! Я ваш бот.')

# Основная функция для запуска бота
def main():
    token = os.getenv('TELEGRAM_TOKEN')
    application = ApplicationBuilder().token(token).build()

    # Добавляем обработчик команды /start
    application.add_handler(CommandHandler("start", start))

    # Запускаем бота
    application.run_polling()

if __name__ == '__main__':
    main()
