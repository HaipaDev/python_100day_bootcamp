import requests
from datetime import datetime

APP_ID="47dfa0d5"
APP_KEY="34073f3eb128949a740f9f8e20866660"

NUTRITIONIX_ENDPOINT="https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_text = input("Tell me which exercises you did: ")
GENDER = "male"
WEIGHT_KG = 52
HEIGHT_CM = 173
AGE = 20

nutritionix_params={
    "query":exercise_text,
    "gender":GENDER,
    "weight_kg":WEIGHT_KG,
    "height_cm":HEIGHT_CM,
    "age":AGE
}
headers={
    "x-app-id":APP_ID,
    "x-app-key":APP_KEY,
    "Content-Type":"application/json",
}

nutritionix_response=requests.post(NUTRITIONIX_ENDPOINT, json=nutritionix_params, headers=headers)
nutritionix_result=nutritionix_response.json()
print(nutritionix_result)


SHEETY_ENDPOINT="https://api.sheety.co/cc5eca37bcc3158ca737f3526177fb3f/workoutTracking/workouts"
ENV_SHEETY_USERNAME="MaciejKrefft03"
ENV_SHEETY_PASSWORD="hyperek"
GOOGLE_SHEET_NAME = "workout"

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

print("\n")
for exercise in nutritionix_result["exercises"]:
    sheety_params={
        GOOGLE_SHEET_NAME: {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    } 

    response=requests.post(SHEETY_ENDPOINT, json=sheety_params, auth=(ENV_SHEETY_USERNAME,ENV_SHEETY_PASSWORD))
    result=response.json()
    print(result)