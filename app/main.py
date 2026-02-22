import os
import asyncio
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from bot.handlers import commands

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

async def on_start_up():
    return

async def main():
    dp.include_router(router=commands.router)
    dp.startup.register(on_start_up)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())