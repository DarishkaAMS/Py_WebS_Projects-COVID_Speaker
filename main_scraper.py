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

    def get_total_cases(self):
        data = self.data['total']

        for content in data:
            if content['name'] == 'Coronavirus Cases:':
                return content['value']

    def get_total_cases(self):
        data = self.data['total']

        for content in data:
            if content['name'] == 'Deaths:':
                return content['value']

        return "Hmmm... I have not found anything with these criteria... Please try again"

    def get_country_data(self, country):
        data = self.data['country']

        for content in data:
            if content['name'].lower() == country.lower():
                return content
        return "Hmmm... I have not found anything with these criteria... Please try again"


data = Data(API_KEY, PROJECT_TOKEN)
print(data.get_country_data("Ukraine")['total_cases'])
print(data.get_country_data("Ukraine"))
