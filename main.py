import types

from config import BOT_TOKEN
from aiogram.filters import Command
from aiogram.types import Message
from aiogram import Bot, Dispatcher,F
from asyncio import run
from requests import get

async def main():
 bot = Bot(token=BOT_TOKEN)
 dp = Dispatcher()
#
 @dp.message (Command(commands=['catfact']))
 async def cat_fact(message: Message):
     print(f'[LOG] user {message.from_user.id} used command /catfact')
     print(f'[LOG] запрашиваю факт о котах')
     response = get('https://catfact.ninja/fact')
     print(f'[LOG] получен результат со статусом {response.status_code}')
     response_json = response.json()
     print(response_json['fact'])

     await message.answer(response_json['fact'])

 @dp.message(F.text)
 async def cat_text(message: Message):
     print(f'[LOG] пользователь {message.from_user.id} написал текст')
     print(f'[LOG] фильрую данный текст')
     await message.answer('оч интересно')
     print(f'[LOG] соо успешно обработалось со статусом {F.status_code}')


 @dp.message(Command(commands = ['breed']))
 async def breeding(message: Message):
     print(f'[LOG] пользователь {message.from_user.id} нажал команду /breed')
     print(f'[LOG] запрашиваю породу кота')
     response = get('https://catfact.ninja/breeds')
     print(f'[LOG] получен результат со статусом {response.status_code}')
     response_json = response.json
     print(response_json['data'][0]['country'])
     print(response_json['data'][0]['breed'])


 @dp.message(Command(commands=['start']))
 async def start(message: Message):
     print(f'[LOG] пользователь {message.from_user.id} нажал кнопку /start')
     await message.answer(f'привет {message.from_user.full_name}')

 await dp.start_polling(bot)



print(f'[LOG] Бот запущен')
run(main()) # запускает цикл событий (dp)
