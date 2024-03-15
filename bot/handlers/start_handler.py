from aiogram import types
from bot.api.users import TelegramUser
from bot.reply_buttons.reply_btn import start_button


async def start_handler(message: types.Message):
    data = {
        'first_name': message.from_user.first_name,
        'last_name': message.from_user.last_name,
        'username': message.from_user.username,
        'telegram_id': message.from_user.id,
        'language': message.from_user.language_code,
    }
    user = TelegramUser()
    user.add_user(data=data)
    await message.answer("Assalomualeykum bu bot orqali siz istalgan kinolaringizni mirqib tomosha qilishingiz mumkin", reply_markup=start_button())
