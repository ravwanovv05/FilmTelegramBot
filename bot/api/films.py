import requests
import os
from dotenv import load_dotenv

load_dotenv()


class Film:

    def add_film_from_bot(self, data):
        url = os.getenv('ADD_FILM_FROM_BOT')
        data = {
            'name': data['film_name'],
            'language': data['film_language'],
            'size': data['film_formats']['size'],
            'release_date': data['film_release_date'],
            'file_unique_id': data['film_formats']['file_unique_id'],
            'category': data['film_category']
        }
        response = requests.post(url, data=data)
        return response.json()

    def add_serial_from_bot(self, data):
        url = os.getenv('ADD_FILM_FROM_BOT')
        data = {
            'name': data['serial_name_part'],
            'language': data['serial_language'],
            'size': data['serial_formats']['size'],
            'release_date': data['serial_release_date'],
            'file_unique_id': data['serial_formats']['file_unique_id'],
            'category': data['serial_id']
        }
        response = requests.post(url, data=data)
        return response.json()

    def search_film(self, name):
        url = f"{os.getenv('SEARCH_FILM')}{name}"
        response = requests.get(url)
        films = response.json()
        return films

    def films_by_category(self, category):
        url = f"{os.getenv('FILMS_BY_CATEGORY')}{category}"
        response = requests.get(url)
        return response.json()

    def film_detail(self, film_id):
        url = f"{os.getenv('FILM_DETAIL')}{film_id}"
        response = requests.get(url)
        return response.json()

    def update_file_unique_id_film(self, file_unique_id, message_id):
        url = f"{os.getenv('UPDATE_FILE_UNIQUE_ID_FILM')}{file_unique_id}"
        response = requests.patch(url, data={'message_id': message_id})
        return response.json()

# print(Film().search_film('t'))

