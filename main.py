import logging
import os
import asyncio
from quart import Quart, request
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters
from handlers import start, handle_message
from config import TELEGRAM_TOKEN
from dotenv import load_dotenv
import os

load_dotenv()

# Включаем логирование
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Инициализация Quart
app = Quart(__name__)

@app.route('/')
async def index():
    return 'Hello, World!'

async def run_bot():
    # Создание приложения
    application = Application.builder().token(TELEGRAM_TOKEN).build()

    # Регистрация команды /start
    application.add_handler(CommandHandler("start", start))

    # Регистрация обработчика сообщений
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Запуск бота
    await application.initialize()
    await application.start()
    await application.updater.start_polling()

async def main():
    # Запуск Telegram бота и Quart сервера параллельно
    bot_task = asyncio.create_task(run_bot())
    quart_task = asyncio.create_task(app.run_task(host='0.0.0.0', port=int(os.environ.get('PORT', 8000))))
    await asyncio.gather(bot_task, quart_task)

if __name__ == '__main__':
    asyncio.run(main())