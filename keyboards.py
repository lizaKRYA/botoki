from lexicon import  MANICUR, RESNICI, PIERCING, LINK1, LINK2, LINK3, DATA1, DATA2, DATA3,DATA4, ORDER,
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

main_menu = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text=MANICUR, callback_data=DATA1, url=LINK1 )],
            [InlineKeyboardButton(text= RESNICI, callback_data=DATA2, url= LINK2)],
            [InlineKeyboardButton(text=PIERCING, callback_data=DATA3, url= LINK3)]
        ]
    )

def get_book_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text=ORDER, callback_data=DATA4)]
        ]
    )

