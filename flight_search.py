import requests
import os

TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
TEQUILA_API_KEY = os.environ["TEQUILA_API_KEY"]

HEADER = {
    "apikey": TEQUILA_API_KEY
}



class FlightSearch:

    def get_destination_code(self, city_name):

        params = {
            "term": f"{city_name}"
        }
        response = requests.get(url=f"{TEQUILA_ENDPOINT}/locations/query", params=params, headers=HEADER)
        data = response.json()
        code = data["locations"][0]["code"]
        return code



