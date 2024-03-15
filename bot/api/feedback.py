import requests
import os
from dotenv import load_dotenv

load_dotenv()


class Feedback:

    def create_feedback(self, data):
        url = os.getenv('CREATE_FEEDBACK')
        sorted_data = {
            'name': data['name'],
            'telegram_id': data['telegram_id'],
            'message': data['feedback']
        }
        response = requests.post(url, json=sorted_data)
        return response.json()
