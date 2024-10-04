from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes

# Функція для обробки команди /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'Привіт, {update.effective_user.first_name}, цей бот створено для навчання математики!')

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

import random
from telegram import Update
from telegram.ext import ContextTypes

# Функція для обробки команди /task
async def task(update: Update, context: ContextTypes.DEFAULT_TYPE):
    tasks = [
        "Розв'яжіть рівняння: 2x + 3 = 7",
        "Знайдіть похідну функції: f(x) = 3x^2 + 2x + 1",
        "Вирішіть нерівність: 5x - 2 > 3",
        "Обчисліть: 12 * 8 - 5",
        "Знайдіть площу кола з радіусом 7 см",
        "Розв'яжіть рівняння: 4x^2 - 16 = 0",
        "Знайдіть інтеграл: ∫ (2x + 3) dx",
        "Скільки буде 15% від 200?",
        "Обчисліть значення виразу: (3 + 5) * 2 - 4"
    ]

    # Випадковий вибір завдання
    task_text = random.choice(tasks)

    # Відповідь на повідомлення
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
        await update.message.reply_text("Можу підказати формули по алгебрі та геометрії. Запитуй!")
    else:
        await update.message.reply_text("Я поки не знаю такої команди, я ще вчуся, але я можу запропонувати заглянути в бібліотеку в секцію математики http://surl.li/nifmut :)")

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
