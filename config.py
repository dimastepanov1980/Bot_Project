from dotenv import load_dotenv
import os

# Загрузка переменных среды из .env файла
load_dotenv()

# Получение токенов из переменных среды
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
ASSISTANT_ID = os.getenv('ASSISTANT_ID')
THREAD_ID = os.getenv('THREAD_ID')
print(ASSISTANT_ID)