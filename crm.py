import logging
import httpx

async def send_to_crm(data):
    crm_url = "https://bike-crm-7f78192cffc8.herokuapp.com/webhook"  # Установите правильный URL вашего CRM
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