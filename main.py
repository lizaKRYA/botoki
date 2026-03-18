import types
from random import choice
from config import BOT_TOKEN
from aiogram.filters import Command
from aiogram.types import Message
from aiogram import Bot, Dispatcher,F
import asyncio
from requests import get
import os
from random import randint

async def main():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()


    @dp.message(Command(commands = ['show']))
    async def show_command(message: Message):
        msg = await message.answer('загрузка')
        with open('data.txt', 'w') as f:
            f.write('curs:temperature\n')
            for _ in range(10):
                f.write(f'{randint(1,100)}:{randint(-30, 30)}\n')
                with open('data.txt', 'r') as f:
                    list_data = f.readlines()
                    if len(list_data) <= 1:
                        await message.answer('в файле нет данных')
                for i in list_data[1:]:
                    elements = i.split(':')
                    await message.answer(f'текущая температура на улице: {elements[1]}')
                    await asyncio.sleep(10)

    @dp.message(F.text.lower().endswith("контакт"))
    async def contact_handler(message: Message):
        print(f'[LOG] пользователь {message.from_user.id}  запросил контакт')
        await message.answer()
        await message.answer_contact(
        phone_number = '+79052408500',
        first_name ='Lafy' )
        print('[LOG] запрос успешно завершен')

    @dp.message(F.text.endswith("адрес"))
    async def address_handler(message: Message):
        await message.answer('да я знаю твой адрес берегись')
        print(f'[LOG] пользователь {message.from_user.id}  запросил адрес')
        await message.answer_location(
            latitude = 54,
            longitude = 22,
        )
        print('[LOG] запрос успешно завершен')
    @dp.message(Command(commands = ['start']))
    async def start_handler(message: Message):
        print(f'[LOG] пользователь {message.from_user.id}  применил функцию /start')
        await message.answer('пр')
        print("[LOG] ответ успешно отправлен пользователю")

    @dp.message()
    async def anything(message: Message):
        print('[LOG] ')
        await message.answer(message.text)

    @dp.message(Command(commands = 'silka'))
    async def silka_handler(message: Message):
        msg =  await message.answr('загрузка')
        with open('phainon.txt', 'r') as f:
            s = f.readlines()
            for i in s[1:]:
                nums, link = i.split(':')
                await message.answer(f'ля ссылки {link}')
                await asyncio.sleep(10)
                await msg.edit_text(f'для ссылки {link} были загружены данные')







    await dp.start_polling(bot)



print(f'[LOG] Бот запущен')
asyncio.run(main()) # запускает цикл событий (dp)
