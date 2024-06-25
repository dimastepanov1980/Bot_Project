import requests
import json
from datetime import datetime, timedelta


client_secret = 'nePiE4EXdgbl30VVPMsfp9luJdb5kfXcHS10DGlbGLh3ta11xdeNvkDJCh56IFhd' 
client_id = '57b8ab72-5e83-4704-b4df-0a5ebc502b2d'

subdomain = 'dimastepanov1980'
redirect_uri = 'https://rent-bike-test-2d40e58cbc88.herokuapp.com'
authorization_code = 'def502005d1033c44967ae14ba1f521f84d79c034a9a5db8883268663cf60542c6c55e8b2b92686d68f68450e7a678c1fd1b0401121672583c0c4b6f6b2f039c1e41e3882e90772bb80d25d3fda7533b4fba8b1846e95125a2456f1ae113aa0545cd552191d8093b2d819f04a22c7e1350659cc78f3a06423649437caaaa7b788a3f0bbf975dce1f78d1174fca8587206720aee2696947e22020a7a39d958da2661c5def07605d38f4d94e126ce3fd86ef75574d743f2fbb5768748bd70e2995056c4156d501849bcbefb63325a3b5408e3259825b53eb3cd4c3d517c48db849d4bc713409039653cf56375d9eadcf79eaccb0ce2afb143a926334494d6709c41def2c82a600a5c0258875cd9760c772c57d66b4d4fe9f1c3540facd7c498c0009fb7d648c309fabe08e3c37135d40e48f03604321dd1b693c6bd8ff4d06c3ebae7650aee09eb2be98661abb133afd454806b8c29e7d5675eee36c05f0792f342eb3af7e201f974be33bcc6fc57b9f38d926afa67f7f4f3454694b680c47eec168355a87bad4293033e8e00f975f5cdf80733fa9594a732e2e24b1cf5c7680620b0544c989bdef11bf6c537ad26b8147d41518d07b0d61d74cc869c10f7fa027ba6db42b25790d2b88351d05fcd7ac7a0594221c4bf61c2e9ce7758b26e61d664d3465a2c02748d6cc4f383b0be69c94f12ebd7d7763c0556956918efc94af06cd98'
access_token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6IjY3MTlmODhhMDY4N2UzNjhhNWJiYjg5NWNhMzZlYWNhMGUyYzQ1N2RmZWZiMTVlN2FmMjNlNWE5NGY5NDkzNGYwMzJkYzlkNTgyNDZmYTEyIn0.eyJhdWQiOiI1N2I4YWI3Mi01ZTgzLTQ3MDQtYjRkZi0wYTVlYmM1MDJiMmQiLCJqdGkiOiI2NzE5Zjg4YTA2ODdlMzY4YTViYmI4OTVjYTM2ZWFjYTBlMmM0NTdkZmVmYjE1ZTdhZjIzZTVhOTRmOTQ5MzRmMDMyZGM5ZDU4MjQ2ZmExMiIsImlhdCI6MTcxOTA1ODMxMCwibmJmIjoxNzE5MDU4MzEwLCJleHAiOjE3MTkxNDQ3MTAsInN1YiI6IjExNTIxNDU1IiwiZ3JhbnRfdHlwZSI6IiIsImFjY291bnRfaWQiOjMzMTAzMDE1LCJiYXNlX2RvbWFpbiI6ImtvbW1vLmNvbSIsInZlcnNpb24iOjIsInNjb3BlcyI6WyJwdXNoX25vdGlmaWNhdGlvbnMiLCJmaWxlcyIsImNybSIsImZpbGVzX2RlbGV0ZSIsIm5vdGlmaWNhdGlvbnMiXSwiaGFzaF91dWlkIjoiYTdhOGZiMjYtMjczYS00OTM5LTljZjctOGYzOTg3ZGI3ZjZkIn0.m1Gfy6UKeoAe-Wz8BKM0EnoI3Fvdxlg6AeXwNpBOSS5LyWPFuLK6qkPqu1xDE1MLnCcem-Vl6ziqtSH-TZGEYnymujJUVoraL_T_hu-MOi9QtJjOH0jJdyzw0N_OvzlTiSRxnuPC6qj4SQuAbMP5yS4unjYoo2PAqQI_Nvv2wAa4K6CfGB_RN6s-SN2pI0Jk55UdVFa0wVEp2BhGW2jQ9EKZnliGwUxa2ZOBTlrLVBpPyErsruQmjCbF7Ynf3Q7frYag_h3Yp3uER-rVDqEOiMrNjyFW0Eyuu9ekC7IuhfsPdcmfm7WpXyRJqLP8u5fYKTnQ4dpdeQSocH-qnV9vyg'
refresh_token = 'def502005bc0171f573119627f87710a0c1b538c59630cea63a92f49223f0ca44e911bb085b8d62df1e42e2f17acc05d639867fd476121e6a88a954af940ad418ca39730df533f2af899e099345c6011f39445f3f695bc13fcdd0846f2464bf2988810a03e444b8d144a2b5a61e807daf5c0e85d3331e9c3b7df43f844d36bf90d4104bbc6c3c0436718f0aa9f5f168d64526e085686e00de1d5c702c3b253fbe9719210bc66567e5aa80a511a4cc8ee03ab81222e7c353a1aeab3b5d202a72b6908d586910b7f5008de3247ffc6a5ff30736b543ce2ba73968d3bdf91ab0f3dd5534ca5519bdbcd4a723e449da960b98d59164c4c29c7cbc585081b18bdda060a796e6eef77eccd0deae88defd3ebdb4a17c156abc6bf88ee71e311df8e6afb950ab9ed84442b6788c54fee477bf5c987590cd79dd7f157906f4eb035639b7c11c8323b7ac9fa32417ba2245b09440fe5b80db76df2168a071b1918b0de941a3dd58125070f981fb5cedfcc4f77f5a31f268b5d4d055e8d6f9233cd47969be3dbebdbabb0c4d81680c2a708114bbe556ec7f6920db041e31b8020bbc1765bb5db375172cead814b3b0c96556aa63121ea5c62e85f43f34f946d1dea2ed451dc7a4ecf8d52aef56fa73f0c40bd858b35e353eeda75d06af3dd842cf78dcb3e42f6ef0e8d3c6aeff2fa32d3573b38'

"""
token_url = 'https://dimastepanov1980.kommo.com/oauth2/access_token'
response = requests.post(token_url, data={
    'client_id': client_id,
    'client_secret': client_secret,
    'grant_type': 'authorization_code',
    'code': authorization_code,
    'redirect_uri': redirect_uri
})

tokens = response.json()
"""


url = f'https://{subdomain}.kommo.com/api/v4/tasks'

# Заголовки для авторизации
headers = {
    'Authorization': f'Bearer {access_token}',
    'Content-Type': 'application/json'
}

def create_contact_in_kommo(user_name, user_contact):
    contact_url = f'https://{subdomain}.kommo.com/api/v4/contacts'

    contact_data = [{
        'name': user_name,
        'custom_fields_values': [
            {
                'field_code': 'PHONE',
                'values': [{'value': user_contact}]
            }
        ]
    }]

    response = requests.post(contact_url, headers=headers, data=json.dumps(contact_data))
    if response.status_code == 200:
        contact_id = response.json()['_embedded']['contacts'][0]['id']
        print(f"Контакт успешно создан в Kommo с ID {contact_id}")
        return contact_id
    else:
        print(f"Ошибка при создании контакта в Kommo: {response.status_code}, {response.text}")
        return None

def create_chat_in_kommo(contact_id):
    chat_url = f'https://{subdomain}.kommo.com/api/v4/chats'
    chat_data = {
        'contacts_id': [contact_id],
        'name': 'Chat with Bot',
        'type': 'incoming'
    }

    response = requests.post(chat_url, headers=headers, data=json.dumps(chat_data))
    
    # Выводим полный ответ от сервера для отладки
    print("Response status code:", response.status_code)
    print("Response text:", response.text)

    if response.status_code == 200:
        chat_id = response.json()['_embedded']['chats'][0]['id']
        print("chat id успешно создан:", chat_id)
        return chat_id
    else:
        print("Ошибка: chat_id не был создан")
        return None
    

def send_message_to_chat(chat_id, message):
    message_url = f'https://{subdomain}.kommo.com/api/v4/chats/messages'
    message_data = {
        'chat_id': chat_id,
        'text': message
    }

    response = requests.post(message_url, headers=headers, data=json.dumps(message_data))
    if response.status_code == 200:
        print("Сообщение успешно отправлено")
    else:
        print(f"Ошибка при отправке сообщения: {response.status_code}, {response.text}")
    
def send_task_to_kommo(chat_id, message, user_name, user_contact):
    contact_id = create_contact_in_kommo(user_name, user_contact)
    if contact_id is None:
        return
    # Время завершения задачи - 1 час от текущего времени
    complete_till = int((datetime.now() + timedelta(hours=1)).timestamp())
    
    # Данные задачи
    data = [{
        'text': f"Диалог с клиентом {user_name} ({user_contact}): {message}",
        'complete_till': complete_till,
        'entity_id': contact_id,
        'entity_type': 'contacts'
    }]

    # Отправка данных в Kommo
    response = requests.post(url, headers=headers, data=json.dumps(data))
    if response.status_code == 200:
        print("Диалог успешно отправлен в Kommo")
    else:
        print(f"Ошибка при отправке диалога в Kommo: {response.status_code}, {response.text}")

# Пример использования
# Пример использования
user_name = 'Иван Иванов123'
user_contact = '+6678999887'
message = 'Привет, у меня есть вопрос о вашем сервисе.'

contact_id = create_contact_in_kommo(user_name, user_contact)
if contact_id:
    chat_id = create_chat_in_kommo(contact_id)
    if chat_id:
        send_message_to_chat(chat_id, message)
        