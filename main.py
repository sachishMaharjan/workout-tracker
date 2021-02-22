import requests
from datetime import datetime
import os

# APP ID and API KEY for NUTRITION API
APP_ID = os.environ['APP_ID']
API_KEY = os.environ['API_KEY']

# Calculating date and time
TODAY = datetime.now()
DATE = TODAY.strftime("%d/%m/%Y")
TIME = TODAY.strftime("%H:%M:%S")


headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

nutrition_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

nutrition_params = {
    "query": input("Tell me what exercise you did: ")
    # "query": "ran 3 miles and walk 5 km."
}

response = requests.post(url=nutrition_endpoint, json=nutrition_params, headers=headers)
# print(response.text)
nutrition_data = response.json()["exercises"]


# ------------------------------------- Sheety API --------------------------------------- #

shetty_endpoints = os.environ['SHETTY_ENDPOINT']

for exercise in nutrition_data:

    headers = {
        "Authorization": f"Bearer {os.environ['BEARER_KEY']}"
    }

    shetty_params = {
        "workout": {
            "date": DATE,
            "time": TIME,
            "exercise": exercise["name"],
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }

    response = requests.post(url=shetty_endpoints, json=shetty_params, headers=headers)
    print(response.text)