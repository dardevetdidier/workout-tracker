import requests
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()
GENDER = "male"
WEIGHT_KG = 65
HEIGHT_CM = 175
AGE = 46

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": os.environ.get('APP_ID'),
    "x-app-key": os.environ.get('API_KEY'),
}

exercise_data = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(url=exercise_endpoint, json=exercise_data, headers=headers)
result = response.json()

date = datetime.strftime(datetime.now(), "%d/%m/%Y")
time = datetime.strftime(datetime.now(), "%H:%M:%S")
exercise = result['exercises'][0]['name'].title()
duration = result['exercises'][0]['duration_min']
calories = result['exercises'][0]['nf_calories']

# sheety request

add_row_endpoint = os.environ.get('SHEET_ENDPOINT')
body = {
    "workout": {
        "date": date,
        "time": time,
        "exercise": exercise,
        "duration": duration,
        "calories": calories
    }
}
headers = {
    "Authorization": os.environ.get('TOKEN')
}

response = requests.post(url=add_row_endpoint, json=body, headers=headers)

