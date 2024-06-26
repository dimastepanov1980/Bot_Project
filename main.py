import logging
import os
import asyncio
from quart import Quart, request
from telegram import Update, Bot
from telegram.ext import Application, CommandHandler, MessageHandler, filters
from handlers import start, handle_message
from config import TELEGRAM_TOKEN
from dotenv import load_dotenv

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

@app.route('/webhook', methods=['POST'])
async def webhook():
    data = await request.get_json()
    logging.info(f"Получены данные вебхука: {data}")
    
    update = Update.de_json(data, bot)
    await application.update_queue.put(update)
    
    return 'OK', 200

@app.route('/test', methods=['GET'])
async def test():
    return 'Test route working!'

async def run_bot():
    global bot
    global application
    application = Application.builder().token(TELEGRAM_TOKEN).build()
    bot = application.bot

    # Регистрация команды /start
    application.add_handler(CommandHandler("start", start))

    # Регистрация обработчика сообщений
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Запуск бота с вебхуками
    webhook_url = f"https://bot-project-8ab97ef4d3f4.herokuapp.com/webhook"
    await bot.set_webhook(webhook_url)
    await application.initialize()
    await application.start()
    await application.updater.start_webhook(
        listen="0.0.0.0",
        port=int(os.environ.get('PORT', 8000)),
        url_path='webhook'
    )
    logging.info("Telegram bot запущен и слушает вебхуки")
    await application.idle()

async def main():
    # Запуск Telegram бота и Quart сервера параллельно
    bot_task = asyncio.create_task(run_bot())
    quart_task = asyncio.create_task(app.run_task(host='0.0.0.0', port=int(os.environ.get('PORT', 8000))))
    await asyncio.gather(bot_task, quart_task)

if __name__ == '__main__':
    asyncio.run(main())