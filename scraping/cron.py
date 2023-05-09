import requests
from datetime import datetime
from cressive_test.settings.common import BASE_URL, API_TOKEN


def start_scraping():
    print(
        f"********************* STARTING SCRAPING AT {datetime.now()} **************************"
    )
    url = f"{BASE_URL}/api/v1/scraping/start/"
    header = {"Authorization": f"Token {API_TOKEN}"}
    response = requests.get(url, headers=header)
    print(f"response: {response}")
