from aiogram import F, Router, Bot
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from aiogram.utils import keyboard
from lexicons.lexicon_ru import START_BTN_TEXT, COURSES_TEXT, COURSES_INFO
from keyboards.menu_kb import menu_kb, contact_keyboard, join_course
from aiogram.fsm.state import State, StatesGroup
class Registration(StatesGroup):
    waiting_fio = State()
    waiting_contact = State()

router = Router()

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
 #   await data.message.edit_reply_markup(keyboard)
    reply_markup = await menu_kb()

@router.callback_query(F.data == ' записаться')
async def singup_handler(data: CallbackQuery, state: FSMContext):
    await data.message.answer('введите ваше имя:')
    await state.set_state(Registration.waiting_fio)

@router.message(Registration.waiting_contact)
async def waiting_contact_handler(message: Message, state: FSMContext):
    await message.answer(
        'введите свой контакт',
    reply_markup=await contact_keyboard()
    )
    await state.update_data(contact = message.text)
    await state.set_state(Registration.waiting_contact)

@router.message(Registration.waiting_fio)
async def process_fio(message: Message, state: FSMContext):
    await message.answer('введите СВОЕ ФИО')
    await state.update_data({'FIO': message.text})
    await state.set_state(Registration.waiting_contact)
'''
@router.message(Registration.waiting_klass)
async def process_klass(message: Message, state: FSMContext ):
    await message.answer('введите класс и школу')
    await state.update_data(klass = message.text)
    await state.set_state(Registration.waiting_klass)
'''

@router.message(F.contact, Registration.waiting_contact)
async def process_username(message: Message, state: FSMContext, bot: Bot):
    phone = message.contact.phone_number
    state_data = await state.get_data()
    fio  = state_data.get('fio', 'inderfined')
    contact = state_data.get('contact', 'inderfined')
    klass = state_data.get('klass', 'inderfined')
    await bot.send_message(
        chat_id = 1194404057,
        text = f"ваше фио: {fio}\n ваш номер телефона: {phone}"
    )
    await state.set_state(None)
    await state.clear() #отчищает память
#redis - redis storage

