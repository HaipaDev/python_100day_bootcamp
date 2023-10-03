import requests
from pprint import pprint

SHEETY_PRICES_ENDPOINT="https://api.sheety.co/cc5eca37bcc3158ca737f3526177fb3f/flightDeals/prices"
ENV_SHEETY_USERNAME="MaciejKrefft03"
ENV_SHEETY_PASSWORD="hyperek"

class DataManager:
    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        # 2. Use the Sheety API to GET all the data in that sheet and print it out.
        response = requests.get(url=SHEETY_PRICES_ENDPOINT, auth=(ENV_SHEETY_USERNAME,ENV_SHEETY_PASSWORD))
        data = response.json()
        pprint(data)
        self.destination_data = data["prices"]
        return self.destination_data
    
    
    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data,
                auth=(ENV_SHEETY_USERNAME,ENV_SHEETY_PASSWORD)
            )
            pprint(response.text)