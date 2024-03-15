from aiogram import types
from aiogram.dispatcher import FSMContext

from bot.api.films import Film
from bot.dispatcher import dp, bot
from bot.inline_buttons.categories import add_subcategory_button
from bot.util.telegram import ADMIN_ID, CHANNEL_ID


async def add_serial_handler(message: types.Message, state: FSMContext):

    if message.from_user.id == ADMIN_ID:
        await state.set_state('serial_id')
        await bot.send_message(message.from_user.id, "Qo'shmoqchi bo'lgan serialingizni tanlang 🎞", reply_markup=add_subcategory_button())
    else:
        await bot.send_message(message.from_user.id, "Afsuski siz admin emassiz 😔")


async def name_serial_handler(query: types.CallbackQuery, state: FSMContext):
    subcategory = int(query.data.split('_')[-1])
    async with state.proxy() as data:
        data['serial_id'] = subcategory

    await state.set_state('serial_name_part')
    await bot.delete_message(query.message.chat.id, query.message.message_id)
    await bot.send_message(query.from_user.id, "Serialning nomi va qismi 🎦")


async def name_part_serial_handler(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['serial_name_part'] = message.text

    await state.set_state('serial_language')
    await bot.send_message(message.from_user.id, "Serial qaysi tilda 🌐")


async def language_serial_handler(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['serial_language'] = message.text

    await state.set_state('serial_release_date')
    await bot.send_message(message.from_user.id, "Serialning chiqgan san'asi 📅")


async def release_date_serial_handler(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['serial_release_date'] = message.text

    await state.set_state('serial_formats')
    await bot.send_message(message.from_user.id, "Serial 🎦")


async def mp4_serial_handler(message: types.Message, state: FSMContext):
    if message.video:
        size = message.video.file_size / (1024 * 1024)
        file_unique_id = message.video.file_unique_id
        async with state.proxy() as data:
            data['serial_formats'] = {
                'size': f"{size:.1f}",
                'file_unique_id': file_unique_id,
            }
        serial = Film()
        serial.add_serial_from_bot(data)
        await state.finish()
        await bot.copy_message(CHANNEL_ID, message.from_user.id, message.message_id, caption=data['serial_name_part'])
