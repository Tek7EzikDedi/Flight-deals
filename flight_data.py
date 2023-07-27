import requests
from pprint import pprint
from datetime import datetime, timedelta
import os


TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
TEQUILA_API_KEY = os.environ["TEQUILA_API_KEY"]

HEADER = {
    "apikey": TEQUILA_API_KEY
}

now = datetime.now().date()

date_from = (now + timedelta(days=1)).strftime("%d/%m/%Y")
date_to = (now + timedelta(days=6*30)).strftime("%d/%m/%Y")

class FlightData:

   def __init__(self):

    self.data = {}

   def low_price(self, id):
       params = {
           "fly_from": "LON",
           "fly_to": f"{id}",
           "date_from": date_from,
           "date_to": date_to,
           "nights_in_dst_from": 7,
           "nights_in_dst_to": 28,
           "curr": "GBP",
           "one_for_city": 1
       }
       response = requests.get(url=f"{TEQUILA_ENDPOINT}/v2/search", params=params, headers=HEADER)
       data = response.json()
       self.data = data
       price = data["data"][0]["price"]
       return price
