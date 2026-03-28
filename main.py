import types
from random import choice
from config import BOT_TOKEN
from aiogram.filters import Command
from aiogram.types import Message , KeyboardButton, ReplyKeyboardMarkup, BotCommand, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from aiogram import Bot, Dispatcher,F
import asyncio
from time import sleep

async def main():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()


    btn_1 = InlineKeyboardButton(
        text = 'pizza',
        callback_data = 'food_1'
    )

    btn_2 = InlineKeyboardButton(
        text = 'sushi',
        url  = 'food_2'
    )

    s = []
    for i in range(1):
        s.append(btn_1)
    keyboard = InlineKeyboardMarkup(
        inline_keyboard= s
    )

    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[[btn_1], [btn_2]]
    )

    @dp.message(F.text)
    async def text(message: Message):
        await message.answer(
            f'вот клава',
            reply_markup=keyboard
        )

    @dp.callback_query(F.data.startwith('food'))
    async def callback_handler(callback: CallbackQuery):
        await callback.edit_text('ваш заказ оформлен')
#callback.answer
#callback.message.answer()
#awat callback.message.edit_text('ваш заказ оформлен")
    s = [
        'вам отправиди пиццу',
        'вам отправили суши'
    ]

    data = callback.data
    slited_data = data.split('-')
    index = int(slited_data[1]) - 1
    await callback.message.answer(s[data])



    s = {
        'food_1': 'pizza',
        'food_2': 'sushi'
    }

    data = callback.data
    await callback.message.answer(f'вы выбрали{s[data]}')
    await asyncio.sleep(1)
    await callback.answer('оформлен заказ')
    await asyncio.sleep(1)
    await callback.message.edit_text('ожидание курьера')
    await asyncio.sleep(1)
    await callback.message.edit_text('заказ готов')



    await dp.start_polling(bot)



print(f'[LOG] Бот запущен')
asyncio.run(main()) # запускает цикл событий (dp)