import requests
from config import Config, load_config
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
import asyncio
from aiogram.filters import Command, CommandObject
config: Config = load_config()
bot_token = config.bot.token
print(bot_token)
bot = Bot(token=bot_token)


dp = Dispatcher()

@dp.message(Command(commands=['start']))
async def process_start(message: Message):
    await message.answer('Привет я твой первый бот')

@dp.message(Command(commands=['help']))
async def process_help(message: Message):
    await message.answer("чем могу помочь?")

@dp.message(Command(commands=['breeds']))
async def show_breeds(message: Message):
    result = requests.get('https://dog.ceo/api/breeds/list/all')
    result_json = result.json()
    dogs_types = result_json['message'].keys()
    s = '\n'.join(list(dogs_types)[:30])
    await message.answer(s)

@dp.message(Command(commands=['dog']))
async def process_dog(message: Message, command: CommandObject):
    if command.args:
        s = requests.get(f'https://dog.ceo/api/breed/{command.args}/images/random')
    else:
      s = requests.get('https://dog.ceo/api/breeds/image/random')
    json_s = s.json()
#requests + bs4
    if json_s.get('status') == 'success':
        #print(json_s.get('message'))
        await message.answer_photo(photo = json_s.get('message'))
    else:
        await message.answer('неправильно :( я не могу так ')



    print(s.content)


async def main():

    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())

