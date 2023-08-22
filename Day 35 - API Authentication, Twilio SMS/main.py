import requests
import datetime

# OWM_ENDPOINT="https://api.openweathermap.org/data/2.5/weather"
# params={
#     "q":"Gdansk,PL",
#     "appid":"69f04e4613056b159c2761a9d9e664d2",#f8554e53e374e397788339a68e1a7294
# }
OWM_ENDPOINT="https://api.openweathermap.org/data/2.5/onecall"
params={
    "lat":54.1332,
    "lon":18.2031,
    "exclude":"current,minutely,daily",
    "appid":"f8554e53e374e397788339a68e1a7294",
}

response=requests.get(OWM_ENDPOINT,params)
response.raise_for_status()
data=response.json()

first_12h_ids=[]
will_rain=False
weather_12h_slice=data["hourly"][:12]
for h in weather_12h_slice:
    weather_id=int(h["weather"][0]["id"])
    first_12h_ids.append(weather_id)
    if weather_id<700:
        will_rain=True
print(first_12h_ids)


# Download the helper library from https://www.twilio.com/docs/python/install
print("\n")
import os
import subprocess
subprocess.run(["pip3", "install", "twilio"])
from twilio.rest import Client
# from twilio.http.http_client import TwilioHttpClient

# proxy_client=TwilioHttpClient()
# proxy_client.session.proxies={"https",os.environ["https_proxy"]}
print("\n")

if will_rain:
    print("Its gonna rain today! Dont forget to bring an umbrella ☂️")
    
    # Find your Account SID and Auth Token at twilio.com/console
    # and set the environment variables. See http://twil.io/secure
    TWILIO_ACCOUNT_SID = os.environ["TWILIO_ACCOUNT_SID"]
    TWILIO_AUTH_TOKEN = os.environ["TWILIO_AUTH_TOKEN"]
    MY_PHONE_NUMBER = os.environ["MY_PHONE_NUMBER"]
    print(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, MY_PHONE_NUMBER)
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)#, http_client=proxy_client)

    message = client.messages \
                    .create(
                        body="Its gonna rain today! Dont forget to bring an umbrella ☂️",
                        from_="+14706348778",
                        to=MY_PHONE_NUMBER
                    )
    print(message.sid)