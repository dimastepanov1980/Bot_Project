import logging
import asyncio
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters
from handlers import start, handle_message
from config import TELEGRAM_TOKEN
import httpx

# Включаем логирование
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Функция для отправки данных в CRM
async def send_to_crm(data):
    async with httpx.AsyncClient() as client:
        try:
            response = await client.post("https://your-crm-url/webhook", json=data)
            response.raise_for_status()
        except httpx.HTTPStatusError as e:
            logging.error(f"Error sending to CRM: {e.response.text}")

# Обработчик команды /start
async def start(update: Update, context):
    await update.message.reply_text('Привет! Как я могу помочь?')
    await send_to_crm({"event": "start", "message": update.message.text})

# Обработчик сообщений
async def handle_message(update: Update, context):
    user_message = update.message.text
    response = "Это ответ от ChatGPT"  # Ваш код для получения ответа от ChatGPT
    await update.message.reply_text(response)
    await send_to_crm({"event": "message", "user_message": user_message, "response": response})

# Настройка и запуск Telegram-бота
async def run_bot():
    application = Application.builder().token(TELEGRAM_TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    await application.start()
    await application.updater.start_polling()

# Запуск бота
async def main():
    bot_task = asyncio.create_task(run_bot())
    await bot_task

if __name__ == '__main__':
    asyncio.run(main())