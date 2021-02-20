import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()
key = os.getenv('KEY')

for year in range(2016, 2021):
    for month in range(1, 13):
        with open(f'../data/{year}_{month}.json', 'w') as file:
            response = requests.get(
                f"https://api.nytimes.com/svc/archive/v1/{year}/{month}.json?api-key={key}"
            )
            json.dump(response.json(), file)
