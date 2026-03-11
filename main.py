import types
from random import choice
from config import BOT_TOKEN
from aiogram.filters import Command
from aiogram.types import Message
from aiogram import Bot, Dispatcher,F
from asyncio import run
from requests import get
import os

async def main():
 bot = Bot(token=BOT_TOKEN)
 dp = Dispatcher()



 @dp.message(F.video | F.photo)
 async def get_video(message: Message, bot: Bot):
     os.makedirs('downloads', exist_ok= True)
     file = message.photo
     if message.photo:
         file = await bot.get_file(message.photo[-1].file_id)
         PATH = os.path.join("downloads", f"{file.file_unique_id}.jpg")
     else:
         file = await bot.get_file(message.video[0].file_id)
         PATH = os.path.join('downloads', f'{file.file_unique_id}.mp4')
     await bot.download_file(file.file_id, destination= PATH)

     await bot.download_file(file.file_id)

     await message.answer('крутые фото или видео')


 await dp.start_polling(bot)



print(f'[LOG] Бот запущен')
run(main()) # запускает цикл событий (dp)
