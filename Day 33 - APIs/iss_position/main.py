import requests
import datetime as dt
import smtplib
import time

MY_LAT=54.121281
MY_LNG=17.978121
MY_EMAIL="maciejkrefft03@gmail.com"
MAIL_PASSWORD="mwwnsttuqrcshaxu"

def is_iss_above_me():
    response_iss=requests.get("http://api.open-notify.org/iss-now.json")
    response_iss.raise_for_status()

    data_iss=response_iss.json()
    iss_latitude=float(data_iss["iss_position"]["latitude"])
    iss_longitude=float(data_iss["iss_position"]["longitude"])
    iss_position=(iss_latitude,iss_longitude)
    print(iss_position)
    return ((MY_LAT-5 <= iss_latitude <= MY_LAT+5) and (MY_LNG-5 <= iss_longitude <= MY_LNG+5))

def is_night():
    parameters_sunset={
        "lat": MY_LAT,
        "lng": MY_LNG,
        "formatted": 0,
    }

    response_sunset=requests.get(f"https://api.sunrise-sunset.org/json",params=parameters_sunset)
    response_sunset.raise_for_status()

    data_sunset=response_sunset.json()
    sunrise_time=data_sunset["results"]["sunrise"].split("T")[1].split("+")[0]
    sunset_time=data_sunset["results"]["sunset"].split("T")[1].split("+")[0]
    sunrise_hour=int(sunrise_time.split(":")[0])
    sunset_hour=int(sunset_time.split(":")[0])
    print(f"Sunrise time: {sunrise_hour}")
    print(f"Sunset time: {sunset_hour}")
    
    now=dt.datetime.now()
    print(f"Your time: {now.hour}")

    return now.hour>=sunset_hour or now.hour<=sunrise_hour


while True:
    print("\n")
    print(f"Is ISS above you: {is_iss_above_me()}")
    print(f"Is it night for you: {is_night()}")
    if(is_iss_above_me() and is_night()):
        connection=smtplib.SMTP("smtp.gmail.com",port=587)
        connection.starttls()
        connection.login(MY_EMAIL,MAIL_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg="Subject:Look up\n\nThe ISS is above you in the sky!"
        )
        print("The ISS is above you in the sky! Message sent!")
    time.sleep(60)