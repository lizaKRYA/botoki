from config import BOT_TOKEN
from aiogram.filters import Command
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, callback_query
from aiogram import Bot, Dispatcher,F, types
import asyncio
from lexicon import MANICUR_USLUGA, RESNICI_USLUGA, PIERCING_USLUGA, MANICUR, RESNICI, PIERCING, LINK1, LINK2, LINK3, DATA1, DATA2, DATA3,DATA4, ORDER, TEXT
from handlers import router
async def main():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()

    dp.include_router(router)


    await dp.start_polling(bot)



print(f'[LOG] Бот запущен')
asyncio.run(main()) # запускает цикл событий (dp)