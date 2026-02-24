from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

keyboard = ReplyKeyboardMarkup(
    keyboard = [
        [KeyboardButton(text='Матчі сьогодні')],
        [KeyboardButton(text='Підписатись на команду')]
    ],
    resize_keyboard=True
)