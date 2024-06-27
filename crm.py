import logging
import httpx
import asyncio

async def send_to_crm(data):
    crm_url = f"https://bike-crm-7f78192cffc8.herokuapp.com/webhook"  # Установите URL CRM в пустую строку для тестирования
    if not crm_url:
        logging.info(f"CRM URL is empty. Data to send: {data}")
        return

    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(crm_url, json=data)
            response.raise_for_status()
            logging.info(f"Data sent to CRM: {data}")
        except httpx.HTTPStatusError as e:
            logging.error(f"Error sending to CRM: {e.response.text}")

data = {
    "user_id": "12345",
    "text": " Новое тестовое сообщение",
    "message_type": "info",
    "created_at": "2024-06-27T10:30:56"
}

async def main():
    await send_to_crm(data)

# Запуск асинхронного контекста
asyncio.run(main())