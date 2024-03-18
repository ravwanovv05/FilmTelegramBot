from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from bot.api.categories import Category
from bot.api.films import Film


def films_by_category_button(page_num, category=None):
    obj = Film()
    film_list = obj.films_by_category(category)
    design, film_name = [], []
    items_per_page = 10

    start_index = (page_num - 1) * items_per_page
    end_index = min(start_index + items_per_page, len(film_list))

    for i in range(start_index, end_index):
        film_name.append(
            InlineKeyboardButton(
                f"{film_list[i]['name']}({film_list[i]['size']} mb)", callback_data=f"film_by_id_{film_list[i]['id']}"
            )
        )

        design.append(film_name)
        film_name = []

        if len(film_name) == 1 and i == len(film_list) - 1:
            design.append(film_name)

    if page_num > 1 and end_index < len(film_list):
        design.append([
            InlineKeyboardButton('⬅ Ortga', callback_data=f'prevfilmct_{page_num}_{category}'),
            InlineKeyboardButton('Oldinga ➡', callback_data=f'nextfilmct_{page_num}_{category}')
        ])
        design.append([InlineKeyboardButton('↩️', callback_data='back_to_categories')])
        ikm = InlineKeyboardMarkup(inline_keyboard=design)
        return ikm

    if page_num > 1:
        design.append([InlineKeyboardButton('⬅ Ortga', callback_data=f'prevfilmct_{page_num}_{category}')])

    if end_index < len(film_list):
        design.append([InlineKeyboardButton('Oldinga ➡', callback_data=f'nextfilmct_{page_num}_{category}')])

    design.append([InlineKeyboardButton('↩️', callback_data='back_to_categories')])

    ikm = InlineKeyboardMarkup(inline_keyboard=design)
    return ikm


def films_by_subcategory_button(subcategory, page_num):
    obj = Film()
    film_list = obj.films_by_category(subcategory)
    parent_id = Category().parent_category(subcategory)['id']
    design, film_name = [], []
    items_per_page = 10

    start_index = (page_num - 1) * items_per_page
    end_index = min(start_index + items_per_page, len(film_list))

    for i in range(start_index, end_index):
        film_name.append(
            InlineKeyboardButton(
                f"{film_list[i]['name']}({film_list[i]['size']} mb)", callback_data=f"film_by_id_{film_list[i]['id']}"
            )
        )

        design.append(film_name)
        film_name = []

        if len(film_name) == 1 and i == len(film_list) - 1:
            design.append(film_name)

    if page_num > 1 and end_index < len(film_list):
        design.append([
            InlineKeyboardButton('⬅ Ortga', callback_data=f'prevfilmsubct_{page_num}_{subcategory}'),
            InlineKeyboardButton('Oldinga ➡', callback_data=f'nextfilmsubct_{page_num}_{subcategory}')
        ])
        design.append([InlineKeyboardButton('↩️', callback_data=f"back_to_subcategories_{parent_id}")])
        ikm = InlineKeyboardMarkup(inline_keyboard=design)
        return ikm

    if page_num > 1:
        design.append([InlineKeyboardButton('⬅ Ortga', callback_data=f'prevfilmsubct_{page_num}_{subcategory}')])

    if end_index < len(film_list):
        design.append([InlineKeyboardButton('Oldinga ➡', callback_data=f'nextfilmsubct_{page_num}_{subcategory}')])

    design.append([InlineKeyboardButton('↩️', callback_data=f"back_to_subcategories_{parent_id}")])

    ikm = InlineKeyboardMarkup(inline_keyboard=design)
    return ikm


def searched_film_button(page_num, search_film):
    film = Film()
    film_list = film.search_film(search_film)
    design, film_name = [], []
    items_per_page = 10

    start_index = (page_num - 1) * items_per_page
    end_index = min((start_index + items_per_page), len(film_list))

    for i in range(start_index, end_index):
        film_name.append(
            InlineKeyboardButton(
                f"{film_list[i]['name']}({film_list[i]['size']} mb)", callback_data=f"film_by_id_{film_list[i]['id']}"
            )
        )

        design.append(film_name)
        film_name = []

        if len(film_name) == 1 and i == len(film_list) - 1:
            design.append(film_name)

    if page_num > 1 and end_index < len(film_list):
        design.append([
            InlineKeyboardButton('⬅ Ortga', callback_data=f'prevfilmsr_{page_num}_{search_film}'),
            InlineKeyboardButton('Oldinga ➡', callback_data=f'nextfilmsr_{page_num}_{search_film}')
        ])
        design.append([InlineKeyboardButton('❌', callback_data="delete_searched_films")])
        ikm = InlineKeyboardMarkup(inline_keyboard=design)
        return ikm

    if page_num > 1:
        design.append([InlineKeyboardButton('⬅ Ortga', callback_data=f'prevfilmsr_{page_num}_{search_film}')])

    if end_index < len(film_list):
        design.append([InlineKeyboardButton('Oldinga ➡', callback_data=f'nextfilmsr_{page_num}_{search_film}')])
    design.append([InlineKeyboardButton('❌', callback_data="delete_searched_films")])

    ikm = InlineKeyboardMarkup(inline_keyboard=design)
    return ikm


def film_detail_button(film_detail):
    design = [
        [InlineKeyboardButton(f"{film_detail['name']} ({film_detail['size']} mb)", callback_data=f"message_id_{film_detail['message_id']}")]
    ]
    ikm = InlineKeyboardMarkup(inline_keyboard=design)
    return ikm
