from config import BOT_TOKEN
from aiogram.filters import Command
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, callback_query
from aiogram import Bot, Dispatcher,F
import asyncio

async def main():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()

   

    a = InlineKeyboardMarkup(
        InlineKeyboardButton( text='счетчик',
                              url =
    ))

    @dp.callback_query(Command(commnads=['menu']))
    async def start(callback: CallbackQuery):
        await callback.message.edit_text(
            'выбери действие',
            reply_markup=InlineKeyboardMarkup()
        )


    await dp.start_polling(bot)



print(f'[LOG] Бот запущен')
asyncio.run(main()) # запускает цикл событий (dp)