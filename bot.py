from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes

# Функція для обробки команди /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'Привіт, {update.effective_user.first_name}, цей бот створено для навчання з математики!')

# Функція для обробки команди /info
async def info(update: Update, context: ContextTypes.DEFAULT_TYPE):
    info_text = (
        "Цей бот допоможе вам вивчити математику!\n"
        "Доступні команди:\n"
        "/start - почати спілкування з ботом\n"
        "/info - отримати інформацію про курс\n"
        "/task - отримати випадкове завдання\n"
        "/quiz - пройти тест\n"
    )
    await update.message.reply_text(info_text)

# Функція для обробки команди /task
async def task(update: Update, context: ContextTypes.DEFAULT_TYPE):
    task_text = "Розв'яжіть рівняння: 2x + 3 = 7"
    await update.message.reply_text(task_text)

# Функція для обробки команди /quiz
async def quiz(update: Update, context: ContextTypes.DEFAULT_TYPE):
    quiz_text = (
        "Відповідайте на запитання:\n"
        "Яка площа кола з радіусом 3? (Виберіть відповідь)\n"
        "1) 9π\n"
        "2) 6π\n"
        "3) 12π\n"
    )
    await update.message.reply_text(quiz_text)

# Обробляємо текстові повідомлення
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()
    if "привіт" in text:
        await update.message.reply_text("Привіт! Як можу допомогти з математикою?")
    elif "формула" in text:
        await update.message.reply_text("Можу підказати формули по алгебрі та геометрії. Спрашивай!")
    else:
        await update.message.reply_text("Я поки не знаю такої команди, але вчуся :)")

# Основна функція для запуску бота
if __name__ == '__main__':
    # Вставте ваш токен нижче
    TOKEN = '7876725841:AAH_XrZvJeiyqPtOwmfGZNIoacG7ZaI8W24'

    # Створюємо додаток для бота
    app = ApplicationBuilder().token(TOKEN).build()

    # Додаємо команди
    app.add_handler(CommandHandler('start', start))
    app.add_handler(CommandHandler('info', info))
    app.add_handler(CommandHandler('task', task))
    app.add_handler(CommandHandler('quiz', quiz))

    # Додаємо обробник текстових повідомлень
    app.add_handler(MessageHandler(None, handle_message))

    # Запускаємо бота
    app.run_polling()
