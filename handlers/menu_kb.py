from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from lexicons.lexicon_ru import START_BTN_TEXT, COURSES_TEXT, COURSES_INFO
from handlers.menu_kb import menu_kb
from aiogram.fam.stats import State, StatesGroup

router = Router()

class Registration(StatesGroup):
    waiting_name =State()
    waiting_username = State()

@router.message(F.text == START_BTN_TEXT[0])
async def courses_handler(message: Message):
    await message.answer(
        COURSES_TEXT,
        reply_markup=await menu_kb()
    )

@router.callback_query(F.data.startswith('courses_'))
async def menu_handler(data: CallbackQuery):
    text = data.data
    info_text = COURSES_INFO[text]
    keyboard = await join_course()
    await data.message.edit_text(info_text)
    await data.message.edit_reply_markup(keyboard)
    info_text,
    reply_markup = await menu_kb()

@router.callback_query(F.data == ' записаться')
async def singup_handler(data: CallbackQuery, state: FSMContext):
    await data.message.answer('введите ваше имя:')
    await state.set_state(Registration.waiting_name)

@router.message(Registration.waiting_name)
async def process_name(message: Message, state: FSMContext):
    await message.answer('введите username')
    await state.update_data(name = message.text)
    await state.set_state(Registration.waiting_username)

@router.message(Registration.waiting_username)
async def process_username(message: Message, state: FSMContext):
    state_data = await state.get_data()
    name  = state_data.get('name', 'inderfined')
    await message.answer(
        f'ваше имя: {name}\n ваш username: {message.text}'
    )
    await state.set_state(None)
    await state.clear() #отчищает память

