from aiogram import types
from aiogram.dispatcher import FSMContext
from bot.api.films import Film
from bot.dispatcher import bot
from bot.inline_buttons.categories import add_category_button
from bot.util.telegram import ADMIN_ID, CHANNEL_ID


async def add_film_handler(message: types.Message, state: FSMContext):

    if message.from_user.id == ADMIN_ID:
        await state.set_state('film_name')
        await message.answer("Film nomini kiritng 📛")
    else:
        await message.answer("Afsuski siz admin emassiz 😔")


async def film_name_handler(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['film_name'] = message.text

    await state.set_state('film_language')
    await message.answer("Film qaysi tilda 🌐")


async def film_language_handler(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['film_language'] = message.text

    await state.set_state('film_release_date')
    await message.answer("Filmni chiqgan san'asi 📅")


async def film_release_date_handler(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['film_release_date'] = message.text

    await state.set_state('film_category')
    await message.answer("Film kategoriasini tanlang 📂", reply_markup=add_category_button())


async def film_category_handler(query: types.CallbackQuery, state: FSMContext):
    category = int(query.data.split('_')[-1])
    async with state.proxy() as data:
        data['film_category'] = category

    await state.set_state('film_formats')
    await bot.delete_message(chat_id=query.message.chat.id, message_id=query.message.message_id)
    await bot.send_message(chat_id=query.from_user.id, text="Film 🎥")


async def film_mp4_handler(message: types.Message, state: FSMContext):
    if message.video:
        size = message.video.file_size / (1024 * 1024)
        file_unique_id = message.video.file_unique_id
        async with state.proxy() as data:
            data['film_formats'] = {
                'size': f"{size:.1f}",
                'file_unique_id': file_unique_id,
            }
        film = Film()
        film.add_film_from_bot(data)
        await state.finish()
        await bot.copy_message(CHANNEL_ID, message.from_user.id, message.message_id, caption=data['film_name'])

