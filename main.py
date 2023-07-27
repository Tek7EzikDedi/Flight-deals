#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import requests
from pprint import pprint
from data_manager import DataManager
from flight_data import FlightData
from notification_manager import NotificationManager

data_manager = DataManager()
sheet_data = DataManager().get_destination_data()

if sheet_data[0]["iataCode"] == "":
    from flight_search import FlightSearch
    flight_search = FlightSearch()
    for i in sheet_data:
        i["iataCode"] = flight_search.get_destination_code(i["city"])

manager = NotificationManager()
flight_data = FlightData()
for i in sheet_data:
    if i["lowestPrice"] > flight_data.low_price(i["iataCode"]):
        i["lowestPrice"] = flight_data.low_price(i["iataCode"])
        my_data = flight_data.data["data"][0]
        manager.send_email(price=my_data["price"], cityFrom=my_data["cityFrom"], cityTo=my_data["cityTo"], deep_link=my_data["deep_link"])


data_manager.destination_data = sheet_data
data_manager.uptade_destination_codes()

