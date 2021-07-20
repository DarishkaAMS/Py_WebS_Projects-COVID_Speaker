from dotenv import load_dotenv
import json
import os
import requests

load_dotenv()

API_KEY = os.environ.get('API_KEY')
PROJECT_TOKEN = os.environ.get("PROJECT_TOKEN")
RUN_TOKEN = "RUN_TOKEN"


class Data:
    def __init__(self, api_key, project_token):
        self.api_key = api_key
        self.project_token = project_token
        self.params = {
            "api_key": self.api_key
        }
        self.get_data()

    def get_data(self):
        response = requests.get(
            f'https://www.parsehub.com/api/v2/projects/{PROJECT_TOKEN}/last_ready_run/data',
            params={'api_key': API_KEY})
        self.data = json.loads(response.text)
        # print(data['total'])


data = Data(API_KEY, PROJECT_TOKEN)
print(data.data['total'])
