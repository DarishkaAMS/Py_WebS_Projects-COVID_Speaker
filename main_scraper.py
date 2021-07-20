from dotenv import load_dotenv
import json
import os
import requests

load_dotenv()

API_KEY = os.environ.get('API_KEY')
PROJECT_TOKEN = os.environ.get("PROJECT_TOKEN")
RUN_TOKEN = "RUN_TOKEN"

response = requests.get(
    f'https://www.parsehub.com/api/v2/projects/{PROJECT_TOKEN}/last_ready_run/data',
    params={'api_key': API_KEY})

data = json.loads(response.text)

print(data)