from aiogram import types
from aiogram.dispatcher import FSMContext

from bot.api.feedback import Feedback


async def feedback_handler(message: types.Message, state: FSMContext):
    await state.set_state('feedback')
    await message.answer("Agar sizda qandaydur takliflar bo'lsa fikringizni yozib qoldiring")


async def register_feedback_handler(message: types.Message, state: FSMContext):
    name = message.from_user.first_name
    telegram_id = message.from_user.id

    async with state.proxy() as data:
        data['name'] = name
        data['telegram_id'] = telegram_id
        data['feedback'] = message.text

    feedback = Feedback()
    feedback.create_feedback(data)

    await state.finish()
    await message.answer("Rahmat ☺")

