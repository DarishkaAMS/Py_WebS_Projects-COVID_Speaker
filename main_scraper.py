import requests

from dotenv import load_dotenv

load_dotenv()

API_KEY = "API_KEY"
PROJECT_TOKEN = "PROJECT_TOKEN"
RUN_TOKEN = "RUN_TOKEN"

response = requests.get(
    f'https://www.parsehub.com/api/v2/projects/{PROJECT_TOKEN}/last_ready_run/data',
    params={'api_key': API_KEY})
