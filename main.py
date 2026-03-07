import types
from random import choice
from config import BOT_TOKEN
from aiogram.filters import Command
from aiogram.types import Message
from aiogram import Bot, Dispatcher,F
from asyncio import run
from requests import get

async def main():
 bot = Bot(token=BOT_TOKEN)
 dp = Dispatcher()

 @dp.message(F.text.contains('start'))
 async def start_handler(message: Message):
   await message.reply(f'ahoj {message.from_user.full_name}')
 @dp.message(Command(commands=['start']))
 async def start(message: Message):
     print(f'[LOG] пользователь {message.from_user.id} нажал кнопку /start')
     await message.answer(f'привет {message.from_user.full_name}')


 s ={5513935927, 6574836746, 1234567890}
 @dp.message( Command(commands= ['secret']), F.from_user.id.in_(s))
 async def secret(message: Message):
     await message.answer(' ahoj ! ja som oki bot')
 @dp.message(not(F.user_name.id == 5513935927 | 6574836746 | 1234567890))
 async def message(message: Message):
     await message.answer(' no')







 await dp.start_polling(bot)



print(f'[LOG] Бот запущен')
run(main()) # запускает цикл событий (dp)
