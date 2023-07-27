import requests

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/44e607cef40ef62a1bcc12431d9efe82/flightDealsDosyasınınKopyası/prices"
class DataManager:
    #This class is responsible for talking to the Google Sheet.

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT)
        response.raise_for_status()
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def uptade_destination_codes(self):
        for i in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": i["iataCode"],
                }

            }

            response = requests.put(url=f"{SHEETY_PRICES_ENDPOINT}/{i['id']}",
                                    json=new_data)
            print(response.text)

