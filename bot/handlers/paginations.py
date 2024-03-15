from aiogram import types
from bot.inline_buttons.films import films_by_category_button
from bot.dispatcher import bot


async def films_pagination(query: types.CallbackQuery):
    page_num = int(query.data.split('_')[-1]) if query.message.text else 1
    print(page_num)
    if query.data.startswith('next'):
        page_num += 1
    else:
        page_num -= 1

    await bot.edit_message_reply_markup(
        chat_id=query.message.chat.id, message_id=query.message.message_id,
        reply_markup=films_by_category_button(page_num)
    )
