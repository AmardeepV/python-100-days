import requests
import datetime
import smtplib
import time


def find_iss():
    responce = requests.get(url="http://api.open-notify.org/iss-now.json")
    responce.raise_for_status()

    data = responce.json()
    longitude = float(data['iss_position']['longitude'])
    latitude = float(data['iss_position']['latitude'])

    location = (latitude, longitude)
    return location


def iss_in_range():
    iss_lat, iss_long = find_iss()
    # iss_lat = 43.04
    # iss_long = 11.4
    if LAT - 5 < iss_lat < LAT + 5 and LONG - 5 < iss_long < LONG + 5:
        return True
    else:
        return False


def sun_rise_set():
    parameters = {
        'lat': LAT,
        'lng': LONG,
        'formatted': 0
    }

    responce = requests.get(
        "https://api.sunrise-sunset.org/json", params=parameters)
    responce.raise_for_status()

    data = responce.json()
    sunrise_hour = int(data['results']['sunrise'].split('T')[1].split(':')[0])
    sunset_hour = int(data['results']['sunset'].split('T')[1].split(':')[0])
    current_hour = datetime.datetime.now().hour

    return sunrise_hour, sunset_hour, current_hour


def main():
    # Graz lat & long
    global LAT, LONG
    LAT = 47.076668
    LONG = 15.421371

    # Email
    SENDER_EMAIL = "amardeepverma03@gmail.com"
    PASSWORD = "qftahkjwdxlovuxm"
    RECEIVER_EMAIL = "pythontest0802@gmail.com"

    while True:
        time.sleep(60)
        iss_near_my_place = iss_in_range()
        sunrise_today, sunset_today, current_time = sun_rise_set()
        # sunrise_today, sunset_today, current_time = (22, 24, 21)
        # print(f"is ISS in range: {iss_near_my_place}")
        # print(
        #     f"sunrise time: {sunrise_today}, sunset time: {sunset_today}, current hour: {current_time}")

        if iss_near_my_place and current_time not in range(sunrise_today, sunset_today):
            print("It is dark and ISS is near by")

            try:
                with smtplib.SMTP("smtp.gmail.com") as connection:
                    connection.starttls()
                    connection.login(user=SENDER_EMAIL, password=PASSWORD)
                    connection.sendmail(from_addr=SENDER_EMAIL,
                                        to_addrs=RECEIVER_EMAIL,
                                        msg="Subject:ISS is near by\n\n ISS is near by Graz and It is also dark outside, you can see it")
            except:
                print("Check Username and Password")
        else:
            print("ISS is not near by")


if __name__ == '__main__':
    main()
