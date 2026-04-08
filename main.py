from config import BOT_TOKEN
from aiogram.filters import Command
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, callback_query
from aiogram import Bot, Dispatcher,F
import asyncio

async def main():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()




    start_test_btn = KeyboardButtoon(
        text = 'Начать тест'
    )

    menu_buttons = ReplyKeyboardMarkup(
        keyboard=[[start_test_btn]],
    )

    questions = [
        {'Какое из этих семи чудес света находилось в Египте и сохранилось  до нашей дней?':
             {
              'Пирамида Хеопса': True,
              "Висячие сады Семирамиды": False,
              "Колосс Родосский": False
             }
        },
        {'Как звали французскую  героиню, ставшую символлом  освобождения во время  столетней  войны?': 'Жанна д Арк'},
        {'Какой мореплаватель  возглавил первую  в истории  экспедицию,  совершившую  круглосветное  путешествие?': ' фернан магеллан'}
    ]

    @dp.message(Command(commands=['start']))
    async def start_handler(message: Message):
        await message.answer(
                             'Начинаем тест, нажмите начать тест',
                             reply_markup=menu_buttons
        )

    @dp.message(F.text == ' Начать тест')
    async def start_test_handler(message: Message):
        await message.answer('кнопка 1')

        counter = 0
        answ = list(questions([counter].keys()))
        text = list(questions[0].values())[0]
        answ_1_btn =  InlineKeyboardButton(
            text = key,
            callback_data = 'question_1'

        )

        answ_keyboard = [[answ_1_btn]]

        await message.answer(
            answ[0],
            reply_markup=answ_keyboard
        )


        @dp.callback_query(F.data.startswith == 'question_1')
        async def answ_handler(callback : CallbackQuery)

         nonlocal counter, user_answ
         data = callback.data
         num = int(data.split('_')[1])
         user_answ.append(num)
         counter += 1
         if counter == 3:
             await callback.message.answer('')
         else:
            answ  = list(questions[0].keys())
            text = list(questions[0].values())[0]

            answ_1_btn = InlineKeyboardButton(
                text = text,
                callback_data = 'question_2'
        )

            answ_keyboard = InlineKeyboardMarkup(
                inline_keyboard=[[answ_1_btn]]
        )

            await callback.answer( text = answ,
                reply_markup = answ_keyboard
        )



    counter = 0

    async def get_answ_btns(btns:dict):
        s = []
        for i, (key,value) in btns.items():
            btn = InlineKeyboardButton()
            s.append(i)
        answ_1_btn = InlineKeyboardButton(
            test = text,
            callback_data = 'question'
        )

    @dp.message(Command(commands='start'))
    async def start_handler(message: Message):
        await message.answer(
            'Начинаем тест, нажмите начать тест',
            reply_markup = menu_buttons
        )

    @dp.message(F.text == 'Начать тест')
    async def start_test_handler(message: Message):
        answ = list (questions[0].keys())
        test = list(questions[0].values())[0]

        answ_1_btn = InlineKeyboardButton(
            test = text,
            callback_data = 'question'

        )
        answ_keyboard = InlineKeyboardMarkup(
            inline_keyboard=[answ_1_btn]
        )

        await message.answer(
            answ[0],
            reply_markup = answ_keyboard
        )

    await dp.start_polling(bot)



print(f'[LOG] Бот запущен')
asyncio.run(main()) # запускает цикл событий (dp)