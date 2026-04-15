
import asyncio
from idlelib.undo import Command
from configs.config import BOT_TOKEN
from aiogram import Bot, Dispatcher
from asyncio import run
from aiogram import F
from aiogram.filters import Command
from aiogram.types import  Message, CallbackQuery
from lexicons.lexicon_ru import QUESTIONS, START_TEST_BTN, START_TEST_ANSW, RESULT_TEST_ANSW
from handlers.keyboards import get_menu_keyboards
from handlers import router




#redis
s = 0
async def main():
    bot = Bot(token = BOT_TOKEN)
    dp = Dispatcher()

    dp.include_router(router)
    dp.include_router(menu_router)
    await dp.start_polling(bot)
    # asyncio.sleep()

print("[LOG] Бот запущен")
run(main()) #запускает цикла событий (dp)
