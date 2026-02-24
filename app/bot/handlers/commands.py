from aiogram import Router, types, F
from aiogram.filters import CommandStart
from services.user_se import add_new_user
from bot.keyboards.menu import keyboard

router = Router()

@router.message(CommandStart())
async def start(message = types.Message):
    first_name = message.from_user.first_name
    user_id = message.from_user.id
    username = message.from_user.username
    
    await add_new_user(user_id, username)
    await message.answer(f'Привіт <b>{first_name}</b>', parse_mode='HTML')
    await message.answer('Оберіть дію: ', reply_markup=keyboard)

@router.message(F.text == 'Матчі сьогодні')
async def todays_matches(message = types.Message):
    await message.answer('matches')