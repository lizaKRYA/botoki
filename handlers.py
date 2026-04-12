from lexicon import MANICUR_USLUGA, RESNICI_USLUGA, PIERCING_USLUGA, DATA1, DATA2,DATA4, TEXT
from aiogram.filters import Command
from keyboards import get_book_keyboard, main_menu
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, callback_query
from aiogram import Router, F, types
import asyncio

router = Router()

@router.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer(
        f"Здравствуйте, {message.from_user.first_name}! 👋\nВыберите интересующую вас услугу:",
        reply_markup=main_menu
    )


@router.callback_query(F.data.startswith("svc_"))
async def show_service_details(callback: types.CallbackQuery):
    if callback.data == DATA1:
        text = MANICUR_USLUGA
    elif callback.data == DATA2:
        text = RESNICI_USLUGA
    else:
        text = PIERCING_USLUGA

    await callback.message.edit_text(text=text, reply_markup=get_book_keyboard())
    await callback.answer()


@router.callback_query(F.data == DATA4)
async def process_booking(callback: types.CallbackQuery):
    await callback.message.edit_text(
        text=TEXT
    )
    await callback.answer()