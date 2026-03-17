import requests
import os
import datetime as dt


def fetch_data(post_completet_url, authentication_keys, query):
    responce = requests.post(url=post_completet_url,
                             headers=authentication_keys, json=query)
    responce.raise_for_status()
    result = responce.json()

    today = dt.datetime.now()
    formated_date = f"{today.strftime("%d")}/{today.strftime("%m")}/{today.strftime("%Y")}"
    formated_time = f"{today.time().hour}:{today.time().minute}:{today.time().second}"
    exercise = result['exercises'][0]['name']
    duration = result['exercises'][0]['duration_min']
    calories = result['exercises'][0]['nf_calories']

    return (formated_date, formated_time, exercise, duration, calories)


def post_data(formated_date, formated_time, exercise, duration, calories, BEARER_AUTH):

    sheety_post_url = "https://api.sheety.co/7b4bc79779875e5d99eeb9add88f2f3d/adWorkouts/workouts"
    workout = {
        "workout": {
            "date": formated_date,
            "time": formated_time,
            "exercise": exercise,
            "duration": duration,
            "calories": calories
        }
    }
    bearer_headers = {
        "Authorization": f"Bearer {BEARER_AUTH}"
    }
    responce = requests.post(
        url=sheety_post_url, json=workout, headers=bearer_headers)
    result = responce.json()
    print(result)


def main():
    APP_ID = os.environ.get("SHEETY_APP_ID")
    API_KEY = os.environ.get("SHEETY_API_KEY")
    BEARER_AUTH = os.environ.get("NEWS_API")

    URL = "https://app.100daysofpython.dev"
    WEIGHT = 73  # Optional: Weight in kg (1-500)
    HEIGHT = 168  # Optional: Height in cm (1-300)
    AGE = 30  # Optional: Age (1-150)
    GENDER = "male"  # Optional: "male" or "female"
    exercise = input("Which exercise you did: ")

    post_url = "/v1/nutrition/natural/exercise"
    post_completet_url = f"{URL}/{post_url}"

    authentication_keys = {
        "x-app-id": APP_ID,
        "x-app-key": API_KEY
    }

    query = {
        "query": exercise,
        "weight_kg": WEIGHT,
        "height_cm": HEIGHT,
        "age": AGE,
        "gender":  GENDER
    }
    formated_date, formated_time, exercise, duration, calories = fetch_data(
        post_completet_url, authentication_keys, query)
    post_data(formated_date, formated_time, exercise,
              duration, calories, BEARER_AUTH)


if __name__ == '__main__':
    main()
