import requests
import os
from dotenv import load_dotenv

load_dotenv()


class Category:

    def category_list(self):
        url = os.getenv('CATEGORY_LIST')
        response = requests.get(url)
        return response.json()

    def sub_categories_by_parent_id(self, parent_id):
        url = f"{os.getenv('SUB_CATEGORIES_BY_PARENT_ID')}{parent_id}"
        response = requests.get(url)
        return response.json()

    def sub_categories(self):
        url = os.getenv('SUB_CATEGORIES')
        response = requests.get(url)
        return response.json()

    def parent_category(self, category_id):
        category_id = int(category_id)
        url = f"{os.getenv('PARENT_CATEGORY')}{category_id}"
        response = requests.get(url)
        return response.json()

# print(Category().category_list())
