import types
from random import choice
from config import BOT_TOKEN
from aiogram.filters import Command
from aiogram.types import Message , KeyboardButton, ReplyKeyboardMarkup, BotCommand
from aiogram import Bot, Dispatcher,F
import asyncio
import click
from requests import get
import os
from random import randint


async def main():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()

    commands = [
        BotCommand(command='/start', description='эта команда начинает бот'),
        BotCommand(command= '/help', description='эта команда помогает'),
        BotCommand(command= '/neperejivay', description='эта команда не переживает'),
        BotCommand(command='/perejivaet', description='эта команда переживает')
        ]

    await bot.set_my_commands(commands)



    knopka_1 = KeyboardButton( text = 'command1')
    knopka_2 = KeyboardButton( text = 'command2')
    knopka_3 = KeyboardButton( text = 'command3')

    keyboard = ReplyKeyboardMarkup(keyboard=[[knopka_1], [knopka_2, knopka_3],], # передаем туда кнопки, формируем клавиатуру
                                             resize_keyboard=True, #сжалась кнопка до высоты текста и ширины экрана телефона
                                   input_field_placeholder='пиши :3'
                                   )

    knopka_11 = KeyboardButton(text='гони фото')
    keyboard_2 = ReplyKeyboardMarkup(keyboard=[[knopka_11]],
                                   # передаем туда кнопки, формируем клавиатуру
                                   resize_keyboard=True,  # сжалась кнопка до высоты текста и ширины экрана телефона
                                   input_field_placeholder='пиши :3'
                                   )

    @dp.message(Command(commands= ['start']))
    async def start_handler(message: Message):
        await message.answer(
            text = 'пр че как',
            reply_markup = keyboard
        )

    @dp.message(F.text == 'command2')
    async def command2_handler(message: Message):
        print('[LOG] команда 2 запускается')
        await message.answer(
            text = 'амфореус имба',
            reply_markup = keyboard
        )

    @dp.message(F.text == 'command1')
    async def comand1(message: Message):
        await message.answer(
            text = 'i',
            reply_markup = keyboard
        )

    @dp.message(F.text == 'command3')
    async def comand3(message: Message):
        await message.answer(
            text = 'ЗАЗАЗАЗАЗАЗАЗАЗААЗАЗАЗАЗААЗАЗ отправь мне фото.',
            reply_markup = keyboard
        )

    @dp.message(F.text == 'отправь фото')
    async def command4(message: Message):
        await message.answer_photo(
            photo= 'https://i.ytimg.com/vi/UMd8Fd6wkds/maxresdefault.jpg?sqp=-oaymwEmCIAKENAF8quKqQMa8AEB-AH-CYAC0AWKAgwIABABGFcgWihlMA8=&rs=AOn4CLDDe_ZxXyDCbc0iNIYRbD0QD3bjdQ',
            reply_markup = keyboard_2
        )




    await dp.start_polling(bot)



print(f'[LOG] Бот запущен')
asyncio.run(main()) # запускает цикл событий (dp)
