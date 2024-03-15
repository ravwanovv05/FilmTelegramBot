import os
import requests
from dotenv import load_dotenv

load_dotenv()


class TelegramUser:

    def add_user(self, data):
        url = os.getenv('ADD_USER')
        response = requests.post(url, data=data)
        return response.json()

    def user_list(self):
        url = os.getenv('USER_LIST')
        response = requests.get(url)
        return response.json()



