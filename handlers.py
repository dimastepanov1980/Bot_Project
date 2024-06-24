import logging
from telegram import Update, ForceReply
from telegram.ext import CallbackContext
from openai_client import get_assistant_response

logger = logging.getLogger(__name__)

# Команда /start
async def start(update: Update, context: CallbackContext) -> None:
    user = update.effective_user
    await update.message.reply_markdown_v2(
        fr'Привет, {user.mention_markdown_v2()}\!',
        reply_markup=ForceReply(selective=True),
    )

# Обработка сообщений
async def handle_message(update: Update, context: CallbackContext) -> None:
    user_message = update.message.text
    chat_id = update.message.chat_id
    logger.info(f"Получено сообщение: {user_message}")

    try:
        ai_reply = await get_assistant_response(user_message, chat_id)
        logger.info(f"Ответ OpenAI: {ai_reply}")
        await update.message.reply_text(ai_reply)
    except Exception as e:
        logger.error(f"Ошибка при получении ответа от OpenAI: {e}")
        await update.message.reply_text('Произошла ошибка при обработке вашего запроса.')