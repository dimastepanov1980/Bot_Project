import logging
import httpx

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