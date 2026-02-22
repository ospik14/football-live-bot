from aiogram import Router, types
from aiogram.filters import CommandStart

router = Router()

@router.message(CommandStart())
async def start(message = types.Message):
    first_name = message.from_user.first_name
    await message.answer(f'Привіт <b>{first_name}</b>', parse_mode='HTML')