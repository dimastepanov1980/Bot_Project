import logging
import os
import asyncio
from quart import Quart
from telegram.ext import Application, CommandHandler, MessageHandler, filters
from handlers import start, handle_message
from config import TELEGRAM_TOKEN
from dotenv import load_dotenv
import httpx

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

@app.route('/test', methods=['GET'])
async def test():
    return 'Test route working!'

async def send_to_crm(data):
    crm_url = ""  # Установите URL CRM в пустую строку для тестирования
    if not crm_url:
        logging.info(f"CRM URL is empty. Data to send: {data}")
        return

    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(crm_url, json=data)
            response.raise_for_status()
        except httpx.HTTPStatusError as e:
            logging.error(f"Error sending to CRM: {e.response.text}")

async def run_bot():
    global application
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