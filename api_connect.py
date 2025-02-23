import json
import requests
from dotenv import load_dotenv
import os

load_dotenv()

NINJA_API_KEY = os.getenv('NINJA_API_KEY') 


def get_from_api(muscle, difficulty = None):
    api_url = f'https://api.api-ninjas.com/v1/exercises?muscle={muscle}'

    if difficulty:
        api_url += f'&difficulty={difficulty}'

    response = requests.get(api_url, headers={'X-Api-Key': NINJA_API_KEY})

    if response.status_code == requests.codes.ok:
        return json.loads(response.text)
    else:
        raise Exception(f"API request error: {response.status_code}")