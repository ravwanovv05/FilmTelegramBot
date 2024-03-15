from aiogram.types import ReplyKeyboardMarkup


def start_button():
    design = [
        ['Qidirish 🔍'],
        ['Kategorialar 📂', 'Fikr-mulohaza ♻️']
    ]
    markup = ReplyKeyboardMarkup(keyboard=design, resize_keyboard=True, one_time_keyboard=True)
    return markup
