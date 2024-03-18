from itertools import chain
from aiogram import types
from aiogram.dispatcher import FSMContext

from bot.api.films import Film
from bot.inline_buttons.categories import category_button, add_category_button, subcategory_button
from bot.inline_buttons.films import searched_film_button, films_by_category_button, film_detail_button, \
    films_by_subcategory_button
from bot.dispatcher import bot
from bot.util.telegram import CHANNEL_ID


# FILMS BY CATEGORY
async def films_by_category_handler(query: types.CallbackQuery):

    if query.data.startswith('delete_category'):
        await bot.delete_message(query.message.chat.id, query.message.message_id)

    else:
        category = query.data.split('_')[-1]
        data = query.values
        category_name = ''
        reply_markups = list(chain(*data['message']['reply_markup']['inline_keyboard']))

        for mrk in reply_markups:
            if mrk['callback_data'] == query.data:
                category_name = mrk['text']

        if category_name == 'Seriallar':
            await bot.edit_message_text(
                category_name, query.message.chat.id, query.message.message_id, reply_markup=subcategory_button(category, page_num=1))
        else:
            await bot.edit_message_text(
                category_name, query.message.chat.id, query.message.message_id, reply_markup=films_by_category_button(page_num=1, category=category))


async def next_prev_film_ct_handler(query: types.CallbackQuery):
    page_num = int(query.data.split('_')[1])
    category = int(query.data.split('_')[-1])
    if query.data.startswith('next'):
        page_num += 1
    else:
        page_num -= 1
    await bot.edit_message_reply_markup(
        query.message.chat.id, query.message.message_id,
        reply_markup=films_by_category_button(page_num, category=category)
    )


# FILM BY ID, CATEGORY
async def film_by_category_handler(query: types.CallbackQuery):
    film_id = int(query.data.split('_')[-1])
    film_detail = Film().film_detail(film_id)
    message_id = film_detail['message_id']
    name = f"📺 |➺ {film_detail['name']}\n"
    language = f"🌐 |➺ {film_detail['language']} tilida\n"
    release_date = f"📅 |➺ {film_detail['release_date']}"
    caption = name + language + release_date
    await bot.delete_message(query.message.chat.id, query.message.message_id)
    await bot.copy_message(query.message.chat.id, CHANNEL_ID, message_id, caption=caption)


# FILMS BY SUBCATEGORY
async def films_by_subcategory_handler(query: types.CallbackQuery):
    category = int(query.data.split('_')[-1])
    data = query.values
    category_name = ''
    reply_markups = list(chain(*data['message']['reply_markup']['inline_keyboard']))

    for mrk in reply_markups:
        if mrk['callback_data'] == query.data:
            category_name = mrk['text']

    await bot.edit_message_text(
        category_name, query.message.chat.id, query.message.message_id,
        reply_markup=films_by_subcategory_button(page_num=1, subcategory=category))


async def next_prev_film_subct_handler(query: types.CallbackQuery):
    page_num = int(query.data.split('_')[1])
    category = int(query.data.split('_')[-1])
    if query.data.startswith('next'):
        page_num += 1
    else:
        page_num -= 1
    await bot.edit_message_reply_markup(
        query.message.chat.id, query.message.message_id,
        reply_markup=films_by_subcategory_button(subcategory=category, page_num=page_num)
    )


# SEARCH FILM
async def search_film_handler(message: types.Message, state: FSMContext):
    await state.set_state('search')
    await message.answer("🔍")


async def searched_films_handler(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['search'] = message.text
    search_film = data['search']
    await bot.send_message(message.from_user.id, "Topilgan ma'lumotlar 🎞", reply_markup=searched_film_button(1, search_film))
    await state.finish()


async def next_prev_film_search_handler(query: types.CallbackQuery):

    if query.data.startswith(('nextfilmsr', 'prevfilmsr')):
        page_num = int(query.data.split('_')[1]) if query.data.split('_')[1] else 1
        search_film = query.data.split('_')[-1]

        if query.data.startswith('nextfilmsr'):
            page_num += 1
            await bot.edit_message_reply_markup(query.message.chat.id, query.message.message_id, reply_markup=searched_film_button(page_num, search_film))

        elif query.data.startswith('prevfilmsr'):
            page_num -= 1
            await bot.edit_message_reply_markup(query.message.chat.id, query.message.message_id, reply_markup=searched_film_button(page_num, search_film))
    else:
        await bot.delete_message(query.message.chat.id, query.message.message_id)



# @dp.channel_post_handler(content_types=['video', 'photo', 'document'])
# async def channel_post(message: types.Message):
#     if message.caption and message.caption.startswith('film'):
#         if message.video:
#             data = message.caption
#             file_unique_id = message.video.file_unique_id
#             # Film().add_film(data, file_id)
#             print(message.video.file_size / (1024 * 1024))
#             print(message.video.file_id)
#             print(file_unique_id)
#             await message.bot.copy_message(6872449936, from_chat_id=CHANNEL_ID, message_id=message.message_id)
#     if message.photo:
#         photo = message.photo[-1]
