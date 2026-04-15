from lexicons.lexicon_ru import START_BTN_TEXT, COURSES_TEXT, COURSES_INFO
from handlers.keyboards import menu_kb()
from aiogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.filters import Command
from aiogram import F, Router
from aiogram.types import Message

router = Router()
counter = 0
user_answ = []


@router.message(F.text == START_BTN_TEXT[0])
async def courses_handler(message: Message):
    await message.answer(
        COURSES_TEXT,
        reply_markup = await menu_kb()
    )

@router.callback_query(F.data.startswith('courses_'))
async def menu_handler(data: CallbackQuery):
    text = data.data
    info_text = COURSES_INFO[text]

    await data.message.edit_text(info_text)