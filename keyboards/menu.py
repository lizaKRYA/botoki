from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from lexicons.lexicon_ru import LIST_COURSES


async def menu_kb():
    list_btns = []
    for keys, values in LIST_COURSES.items():
        btn = InlineKeyboardButton(
            text = keys,
            callback_data = values
        )
        list_btns.append([btn])
    keyboards = InlineKeyboardMarkup(
        inline_keyboard=list_btns
    )
    return keyboards

async def join_courses():
    s =[]

    for key, val in JOIN_TEXT.items()
    button = InlineKeyboardButton(
        text = text,
        callback_data = data
    )
    s.append([button])

    keyboards = InlineKeyboardMarkup(
        inline_keyboard=[s]
    )