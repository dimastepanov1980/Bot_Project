import time
import json
from openai import OpenAI
from config import OPENAI_API_KEY, ASSISTANT_ID, TELEGRAM_TOKEN
from config_instructions import INSTRUCTIONS
from config_function import TOOLS
from getdatetime import get_current_datetime
from google_client import check_bike_availability, create_booking  # Импортируем функции из google_client.py

client = OpenAI(
    api_key=OPENAI_API_KEY
)
assistant = client.beta.assistants.update(
  assistant_id = ASSISTANT_ID,
  name="Bike rent Assistance",
  instructions=INSTRUCTIONS,
  tools=TOOLS,
  model="gpt-4o",
  temperature=0.5
)

assistant = client.beta.assistants.retrieve(
  assistant_id = ASSISTANT_ID
)

thread = client.beta.threads.create()

async def get_assistant_response(user_message: str, chat_id: int = None) -> str:
    
    client.beta.threads.messages.create(
        thread_id=thread.id,
        role="user",
        content=user_message
    )
    
    run = client.beta.threads.runs.create_and_poll(thread_id=thread.id, assistant_id=assistant.id)
    print(f" * Run Status: {run.id}")

    while run.status != "completed":
        run = client.beta.threads.runs.retrieve(thread_id=thread.id, run_id=run.id)

        tool_outputs = []
        
        for tool in run.required_action.submit_tool_outputs.tool_calls:
            if tool.function.name == "check_bike_availability":
                arguments = json.loads(tool.function.arguments)  # Преобразование строки в словарь
                start_date = arguments['start_date']
                end_date = arguments['end_date']
                cc = int(arguments['cc'])
                available_bikes = check_bike_availability(start_date, end_date, cc)              
                availability = json.dumps(available_bikes)  # Преобразование списка в строку для ответа
                tool_outputs.append({
                    "tool_call_id": tool.id,
                    "output": availability
                })
            if tool.function.name == "get_current_datetime":
                current_time = get_current_datetime()              
                tool_outputs.append({
                    "tool_call_id": tool.id,
                    "output": current_time
                })
            if tool.function.name == "create_booking":
                arguments = json.loads(tool.function.arguments)  # Преобразование строки в словарь
                start_date = arguments['start_date']
                end_date = arguments['end_date']
                cc = int(arguments['cc'])
                number = int(arguments['number'])
                name = arguments['name']
                contact = arguments['contact']
                booking_result = create_booking(number, cc, name, contact, start_date, end_date, chat_id)
                availability = json.dumps(booking_result)  # Преобразование списка в строку для ответа
                tool_outputs.append({
                    "tool_call_id": tool.id,
                    "output": availability
                })
        if tool_outputs:
            try:
                run = client.beta.threads.runs.submit_tool_outputs_and_poll(
                    thread_id=thread.id,
                    run_id=run.id,
                    tool_outputs=tool_outputs
                )
                print("Tool outputs submitted successfully.")
            except Exception as e:
                print("Failed to submit tool outputs:", e)
        else:
            print("No tool outputs to submit.")

        print(f" * Run Status: {run.status}")
        print(f" * Run: {run}")
        time.sleep(1)
    else:
        print(f"* Run Completed!")

    response = client.beta.threads.messages.list(thread_id=thread.id)
    response_messages = response.data
    last_message = response_messages[0]
    return last_message.content[0].text.value