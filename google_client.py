import gspread
import random
from google.oauth2.service_account import Credentials
from datetime import datetime
from telegram import Bot
import base64
import json
import os



# Подключаемся к Google Sheets
scopes = ["https://www.googleapis.com/auth/spreadsheets"]
credentials_json = os.getenv("GOOGLE_CREDENTIALS_JSON")
credentials_info = json.loads(base64.b64decode(credentials_json))
creds = Credentials.from_service_account_info(credentials_info, scopes=scopes)
client = gspread.authorize(creds)
sheet_id = "1DbDvZZZcOzOTy5IAd5Wr7rv8iwwS8aII3d6yMkdOZL8"
sheet = client.open_by_key(sheet_id)

# Функция для преобразования списка значений в список словарей
def convert_to_dicts(values):
    keys = values[0]
    return [dict(zip(keys, row)) for row in values[1:]]


import random
import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime

# Подключаемся к Google Sheets
scopes = ["https://www.googleapis.com/auth/spreadsheets"]
creds = Credentials.from_service_account_file("credentials.json", scopes=scopes)
client = gspread.authorize(creds)
sheet_id = "1DbDvZZZcOzOTy5IAd5Wr7rv8iwwS8aII3d6yMkdOZL8"
sheet = client.open_by_key(sheet_id)

# Функция для преобразования списка значений в список словарей
def convert_to_dicts(values):
    keys = values[0]
    return [dict(zip(keys, row)) for row in values[1:]]

# Функция для проверки доступности байков и возврата одного случайного байка
def check_bike_availability(start_date: str, end_date: str, cc: int = None) -> dict:
    bookings_sheet = sheet.worksheet('Booking').get_all_values()
    bikes_sheet = sheet.worksheet('Bike').get_all_values()

    bookings = convert_to_dicts(bookings_sheet)
    bikes = convert_to_dicts(bikes_sheet)

    available_bikes = []
    for bike in bikes:
        try:
            bike_cc = int(bike['cc']) if 'cc' in bike and bike['cc'] else None
            bike_number = int(bike['Number'])
        except ValueError:
            continue
        
        if cc is None or bike_cc == cc:
            is_available = True
            for booking in bookings:
                try:
                    booking_number = int(booking['Number'])
                except ValueError:
                    continue
                
                if booking_number == bike_number:
                    booking_start = datetime.strptime(booking['start_date'], "%d.%m.%Y")
                    booking_end = datetime.strptime(booking['end_date'], "%d.%m.%Y")
                    requested_start = datetime.strptime(start_date, "%d.%m.%Y")
                    requested_end = datetime.strptime(end_date, "%d.%m.%Y")
                    if not (requested_end < booking_start or requested_start > booking_end):
                        is_available = False
                        break
            if is_available:
                available_bikes.append(bike)

    return random.choice(available_bikes) if available_bikes else None


# Функция для бронирования байка
def create_booking(number: int, cc: int, name: str, contact: str, start_date: str, end_date: str, chat_id: int = None) -> list:
    bikes_sheet = sheet.worksheet('Bike').get_all_values()
    bikes = convert_to_dicts(bikes_sheet)
    
    bike = next((bike for bike in bikes if bike['Number'].isdigit() and bike['cc'].isdigit() and int(bike['Number']) == number and int(bike['cc']) == cc), None)
    
    if not bike:
        return f"Байк с номером {number} и мощностью {cc}cc не найден."
    
    formatted_start_date = datetime.strptime(start_date, "%d.%m.%Y")
    formatted_end_date = datetime.strptime(end_date, "%d.%m.%Y")
    days_rented = (formatted_end_date - formatted_start_date).days

    if days_rented <= 6:
        cost_per_day = int(bike['1-6'])
    elif days_rented <= 10:
        cost_per_day = int(bike['7-10'])
    elif days_rented <= 14:
        cost_per_day = int(bike['11-14'])
    elif days_rented <= 20:
        cost_per_day = int(bike['14-20'])
    elif days_rented <= 29:
        cost_per_day = int(bike['21-29'])
    else:
        cost_per_day = int(bike['30+'])

    total_cost = cost_per_day * days_rented

    bookings_sheet = sheet.worksheet('Booking')

    next_row = len(bookings_sheet.get_all_values()) + 1
    
    bookings_sheet.update_cell(next_row, 1, number)
    bookings_sheet.update_cell(next_row, 2, cc)
    bookings_sheet.update_cell(next_row, 3, name)
    bookings_sheet.update_cell(next_row, 4, contact)
    bookings_sheet.update_cell(next_row, 5, chat_id)
    bookings_sheet.update_cell(next_row, 6, formatted_start_date.strftime("%d.%m.%Y"))
    bookings_sheet.update_cell(next_row, 7, formatted_end_date.strftime("%d.%m.%Y"))
    bookings_sheet.update_cell(next_row, 8, days_rented)
    bookings_sheet.update_cell(next_row, 9, cost_per_day)
    bookings_sheet.update_cell(next_row, 10, total_cost)

    new_booking = [number, cc, name, contact, formatted_start_date.strftime("%d.%m.%Y"), formatted_end_date.strftime("%d.%m.%Y")]
    return new_booking