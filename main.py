
import asyncio
from idlelib.undo import Command
from configs.config import BOT_TOKEN
from aiogram import Bot, Dispatcher
from asyncio import run
from aiogram import F
from aiogram.filters import Command
from aiogram.types import  Message, CallbackQuery
from lexicons.lexicon import QUESTIONS, START_TEST_BTN, START_TEST_ANSW, RESULT_TEST_ANSW
from keyboards.keyboards import get_menu_keyboards
from handlers import router

async def main():
    bot = Bot(token = BOT_TOKEN)
    dp = Dispatcher()

    dp.include_router(router)

    await dp.start_polling(bot)
    # asyncio.sleep()

print("[LOG] Бот запущен")
run(main()) #запускает цикла событий (dp)
