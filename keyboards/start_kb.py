from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from lexicons.lexicons_ru import LIST_COURSES, JOIN_TEXTS

async def menu_kb():
    list_bts = []
    for keys, values in LIST_COURSES.items():
        button = InlineKeyboardButton(
            text = keys,
            callback_data = values
        )
        list_bts.append([button])
    keyboards = InlineKeyboardMarkup(
        inline_keyboard= list_bts
    )
    return keyboards


async def join_course():
    s = []
    for text, data in JOIN_TEXTS.items():
        button = InlineKeyboardButton(
            text = text,
            callback_data =data
        )
        s.append(button)
    keyboard = InlineKeyboardMarkup(
        inline_keyboard = [s]
    )
    return keyboard