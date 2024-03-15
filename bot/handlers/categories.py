from aiogram import types

from bot.dispatcher import dp, bot
from bot.inline_buttons.categories import category_button, subcategory_button


async def category_list_handler(message: types.Message):
    await message.answer("Kategorialar 📂", reply_markup=category_button())


async def back_to_categories(query: types.CallbackQuery):
    await bot.edit_message_text("Kategorialar 📂", query.message.chat.id, query.message.message_id, reply_markup=category_button())


async def back_to_subcategories(query: types.CallbackQuery):
    parent_id = int(query.data.split('_')[-1])
    await bot.edit_message_text("Seriallar", query.message.chat.id, query.message.message_id, reply_markup=subcategory_button(parent_id, page_num=1))


async def next_prev_subcategories(query: types.CallbackQuery):
    parent_id = int(query.data.split('_')[-1])
    page_num = int(query.data.split('_')[1])

    if query.data.startswith('next'):
        page_num += 1

    else:
        page_num -= 1

    await bot.edit_message_reply_markup(query.message.chat.id, query.message.message_id, reply_markup=subcategory_button(parent_id, page_num=page_num))

