#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import requests
from datetime import datetime,timedelta
from pprint import pprint

from flight_search import FlightSearch
from data_manager import DataManager

flight_search = FlightSearch()
data_manager = DataManager()
sheet_data = data_manager.get_destination_data()


# for row in sheet_data:
#     if row["iataCode"] == "":
#         row["iataCode"] = flight_search.get_destination_code(row["city"])
# print(f"sheet_data:\n {sheet_data}")
# data_manager.destination_data = sheet_data
# data_manager.update_destination_codes()

if sheet_data[0]["iataCode"] == "":
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])
    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()

# ORIGIN_CITY_IATA="LON"
ORIGIN_CITY_IATA="GDN"
tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

for destination in sheet_data:
    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )
    if flight is not None:
        if flight.price < destination["lowestPrice"]:
            pprint(f"Found cheap flight for: {flight.destination_city} !")