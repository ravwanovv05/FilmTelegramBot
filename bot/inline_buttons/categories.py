from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from bot.api.categories import Category


def add_category_button():
    obj = Category()
    category_list = obj.category_list()
    design, category_name = [], []

    for i in range(len(category_list)):
        category_name.append(
            InlineKeyboardButton(category_list[i]['name'], callback_data=f"add_category_{category_list[i]['id']}")
        )

        if len(category_name) == 2:
            design.append(category_name)
            category_name = []

        if len(category_name) == 1 and i == len(category_list) - 1:
            design.append(category_name)

    ikm = InlineKeyboardMarkup(inline_keyboard=design, row_width=2)
    return ikm


def category_button():
    obj = Category()
    category_list = obj.category_list()
    design, category_name = [], []

    for i in range(len(category_list)):
        category_name.append(
            InlineKeyboardButton(category_list[i]['name'], callback_data=f"category_{category_list[i]['id']}")
        )

        if len(category_name) == 2:
            design.append(category_name)
            category_name = []

        if len(category_name) == 1 and i == len(category_list) - 1:
            design.append(category_name)
    design.append([InlineKeyboardButton('🗑', callback_data='delete_category')])
    ikm = InlineKeyboardMarkup(inline_keyboard=design, row_width=2)
    return ikm


def subcategory_button(parent_id, page_num):
    obj = Category()
    subcategory_list = obj.sub_categories_by_parent_id(parent_id)
    design, subcategory_name = [], []
    items_per_page = 10

    start_index = (page_num - 1) * items_per_page
    end_index = min(start_index + items_per_page, len(subcategory_list))

    for i in range(start_index, end_index):
        subcategory_name.append(
            InlineKeyboardButton(subcategory_list[i]['name'], callback_data=f"subcategory_{subcategory_list[i]['id']}")
        )
        if len(subcategory_name) == 2:
            design.append(subcategory_name)
            subcategory_name = []

        if len(subcategory_name) == 1 and i == len(subcategory_list) - 1:
            design.append(subcategory_name)

    if page_num > 1 and end_index < len(subcategory_list):
        design.append([
            InlineKeyboardButton('⬅ Ortga', callback_data=f'prevsubct_{page_num}_{parent_id}'),
            InlineKeyboardButton('Oldinga ➡', callback_data=f'nextsubct_{page_num}_{parent_id}')
        ])
        design.append([InlineKeyboardButton('↩', callback_data='back_to_categories')])
        ikm = InlineKeyboardMarkup(inline_keyboard=design)
        return ikm

    if page_num > 1:
        design.append([InlineKeyboardButton('⬅ Ortga', callback_data=f'prevsubct_{page_num}_{parent_id}')])

    if end_index < len(subcategory_list):
        design.append([InlineKeyboardButton('Oldinga ➡', callback_data=f'nextsubct_{page_num}_{parent_id}')])

    design.append([
        InlineKeyboardButton('↩', callback_data='back_to_categories')
    ])

    ikm = InlineKeyboardMarkup(inline_keyboard=design)
    return ikm


def add_subcategory_button():
    obj = Category()
    category_list = obj.sub_categories()
    design, subcategory_name = [], []

    for i in range(len(category_list)):
        subcategory_name.append(
            InlineKeyboardButton(category_list[i]['name'], callback_data=f"add_subcategory_{category_list[i]['id']}")
        )

        if len(subcategory_name) == 2:
            design.append(subcategory_name)
            subcategory_name = []

        if len(subcategory_name) == 1 and i == len(category_list) - 1:
            design.append(subcategory_name)

    ikm = InlineKeyboardMarkup(inline_keyboard=design, row_width=2)
    return ikm
