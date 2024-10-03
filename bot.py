import openai
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters

# Инициализация API OpenAI
openai.api_key = 'sk-svcacct-7wU0wIHtirD6vwnouRx4JhvjwKV7o5YZ1QFoUqDKBhhNU2Ee5P9HdFl5eq_bT3BlbkFJLYvJgCga9hj7ka2czpfcmo8DrPhKxcbDfGUinhz_2Tr4w4x27ieaXVqdLMQA'

# Функция для общения с ChatGPT
def chatgpt_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()

# Обработка сообщений от пользователей
async def handle_message(update: Update, context):
    user_message = update.message.text
    gpt_response = chatgpt_response(user_message)
    await update.message.reply_text(gpt_response)

# Команда /start
async def start(update: Update, context):
    await update.message.reply_text("Привет! Я бот с поддержкой ChatGPT. Задавай вопросы!")

if __name__ == '__main__':
    # Инициализация бота
    application = ApplicationBuilder().token('7876725841:AAH_XrZvJeiyqPtOwmfGZNIoacG7ZaI8W24').build()

    # Обработчики команд и сообщений
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Запуск бота
    application.run_polling()
