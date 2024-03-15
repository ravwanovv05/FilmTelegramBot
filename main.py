import logging
from aiogram.utils import executor
from bot.dispatcher import dp
from bot.handlers.add_serial_from_bot import (
    add_serial_handler, name_serial_handler, name_part_serial_handler,
    language_serial_handler, release_date_serial_handler, mp4_serial_handler)

from bot.handlers.advertising import (
    forward_advertising_handler, advertising_caption_handler,register_advertising_handler,
    register_advertising_description_handler, register_advertising_content_handler)

from bot.handlers.categories import (
    category_list_handler, back_to_categories, back_to_subcategories,
    next_prev_subcategories)

from bot.handlers.add_film_from_bot import (
    add_film_handler, film_name_handler, film_language_handler,
    film_release_date_handler, film_category_handler, film_mp4_handler)
from bot.handlers.feedback import feedback_handler, register_feedback_handler

from bot.handlers.films import (
    search_film_handler, searched_films_handler, films_by_category_handler,
    film_by_category_handler, next_prev_film_ct_handler, next_prev_film_search_handler, films_by_subcategory_handler,
    next_prev_film_subct_handler)

from bot.handlers.start_handler import start_handler


dp.register_message_handler(start_handler, commands=['start'])

dp.register_message_handler(feedback_handler, lambda message: message.text == 'Fikr-mulohaza ♻️')
dp.register_message_handler(register_feedback_handler, state='feedback')

dp.register_message_handler(category_list_handler, lambda message: message.text == 'Kategorialar 📂')

dp.register_message_handler(search_film_handler, lambda message: message.text == 'Qidirish 🔍')
dp.register_message_handler(searched_films_handler, state='search')
dp.register_callback_query_handler(next_prev_film_search_handler, lambda query: query.data.startswith(('nextfilmsr', 'prevfilmsr', 'delete_searched_films')))

# from handlers/films.py for get film by category
dp.register_callback_query_handler(films_by_category_handler, lambda query: query.data.startswith(('category', 'delete_category')))
dp.register_callback_query_handler(film_by_category_handler, lambda query: query.data.startswith('film_by_id'))
dp.register_callback_query_handler(next_prev_film_ct_handler, lambda query: query.data.startswith(('nextfilmct', 'prevfilmct')))
dp.register_callback_query_handler(next_prev_film_subct_handler, lambda query: query.data.startswith(('nextfilmsubct', 'prevfilmsubct',)))
dp.register_callback_query_handler(next_prev_subcategories, lambda query: query.data.startswith(('nextsubct', 'prevsubct')))
dp.register_callback_query_handler(back_to_categories, lambda query: query.data.startswith('back_to_categories'))
dp.register_callback_query_handler(back_to_subcategories, lambda query: query.data.startswith('back_to_subcategories'))

# from handlers/films.py for get film by subcategory
dp.register_callback_query_handler(films_by_subcategory_handler, lambda query: query.data.startswith('subcategory'))


# from handlers/add_film_from_bot.py for add film
dp.register_message_handler(add_film_handler, commands=['add'])
dp.register_message_handler(film_name_handler, state='film_name')
dp.register_message_handler(film_language_handler, state='film_language')
dp.register_message_handler(film_release_date_handler, state='film_release_date')
dp.register_callback_query_handler(film_category_handler, lambda query: query.data.startswith('add_category'), state='film_category')
dp.register_message_handler(film_mp4_handler, content_types=['video'], state='film_formats')

# from handlers/add_serial_from_bot.py for add serial
dp.register_message_handler(add_serial_handler, commands=['addserial'])
dp.register_callback_query_handler(name_serial_handler, lambda query: query.data.startswith('add_subcategory_'), state='serial_id')
dp.register_message_handler(name_part_serial_handler, state='serial_name_part')
dp.register_message_handler(language_serial_handler, state='serial_language')
dp.register_message_handler(release_date_serial_handler, state='serial_release_date')
dp.register_message_handler(mp4_serial_handler, content_types=['video'], state='serial_formats')

# advertising forwarding
dp.register_message_handler(forward_advertising_handler, commands=['forwardadvertising'])
dp.register_message_handler(advertising_caption_handler, content_types=['video', 'photo', 'document'], state='advertising_caption')

# advertising register
dp.register_message_handler(register_advertising_handler, commands=['registeradvertising'])
dp.register_message_handler(register_advertising_description_handler, state='description')
dp.register_message_handler(register_advertising_content_handler, content_types=['video', 'photo'], state='content')


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)
