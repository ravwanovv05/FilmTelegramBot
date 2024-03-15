from aiogram.dispatcher import FSMContext
from bot.api.users import TelegramUser
from bot.dispatcher import dp, bot
from aiogram import types
from bot.util.telegram import ADMIN_ID


async def forward_advertising_handler(message: types.Message, state: FSMContext):
    if message.from_user.id == ADMIN_ID:
        await state.set_state('advertising_caption')
        await message.answer("Reklamani yuboring 💥")
    else:
        await message.answer("Afsuski siz admin emassiz 😔")


async def advertising_caption_handler(message: types.Message, state: FSMContext):
    users = TelegramUser().user_list()
    caption = message.text
    sent_count = 0

    async with state.proxy() as data:
        data['advertising_caption'] = caption

    for user in users:
        user_id = int(user['telegram_id'])
        user_firstname = user['first_name']

        try:
            await bot.copy_message(user_id, message.chat.id, message.message_id, caption=data['advertising_caption'])
            sent_count += 1
        except Exception as e:
            await bot.send_message(message.from_user.id, f"Spam foydalanuvchi: {user_firstname}")

    await message.answer(f"Umumiy {sent_count} ta foydalanuvchiga yuborildi!")
    await state.finish()


# register advertising
async def register_advertising_handler(message: types.Message, state: FSMContext):
    if message.from_user.id == ADMIN_ID:
        await state.set_state('description')
        await message.answer("Rekalama uchun tavsif 🧾")
    else:
        await message.answer("Afsuski siz admin emassiz 😔")


async def register_advertising_description_handler(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['description'] = message.text
    await state.set_state('content')
    await message.answer("Video yoki rasm yuboring 📤")


async def register_advertising_content_handler(message: types.Message, state: FSMContext):
    users = TelegramUser().user_list()
    sent_count = 0

    async with state.proxy() as data:
        data['content'] = message.content_type

    for user in users:
        user_id = int(user['telegram_id'])

        try:
            await bot.copy_message(user_id, message.chat.id, message.message_id, caption=data['description'])
            sent_count += 1
        except Exception as e:
            pass
    await state.finish()
    await message.answer(f"Umumiy {sent_count} ta foydalanuvchiga yuborildi!")
