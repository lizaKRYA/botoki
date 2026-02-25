from config import Config, load_config
from aiogram import Bot, Dispatcher, F
import asyncio
from pathlib import Path
from aiogram.types import Message,FSInputFile
config: Config = load_config()
bot_token = config.bot.token
print(bot_token)
bot = Bot(token=bot_token)
dp = Dispatcher()
'''
#домашняя папка пользоваеля
HOME_DIR = Path.home()
#раюочий стол
DESKTOP_DIR = HOME_DIR / "Desktop"
#папка
DOWNLOAD_DIR = DESKTOP_DIR / "Download"

@dp.message(F.photo)
    #bot -
async def photo_handler(message: Message, bot: Bot):
    photo = message.photo[-1]
    file = await bot.get_file(photo.file_id)
    await bot.download_file(file.file_path, DOWNLOAD_DIR)
'''
'''
@dp.message(F.text.lower()=='гони фото')
async def song_photo_url(message: Message):
    #нельзя отправить текст> 4096
    #нельзя отправить caption > 1024
    photo = 'https://yandex.ru/images/search?img_url=https%3A%2F%2Fupload-os-bbs.hoyolab.com%2Fupload%2F2025%2F01%2F22%2F134246182%2Fe701c77c5c1cc2866877cb95ee845f6c_6446799511393735519.webp&lr=22&pos=0&rpt=simage&source=serp&text=phainon'
    await message.answer_photo(
        photo,
        caption = 'во псина'
    )
    #отправка локального файла
    photo = FSInputFile('files/test_1.jpg')
    await message.answer_photo(
        photo = photo,
        caption = 'во фото'
    )
'''

@dp.message(F.photo)
async def photo_reply(message: Message):
    photo = message.photo[-1]
    await message.reply_photo(
        photo = photo.file_id,
        caption = 'мда не кидай мне больше эту фигню'


    )
    # пользователь отправляет фото, вернуть это же фото

async def main():

    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())

# git checkout -b dog