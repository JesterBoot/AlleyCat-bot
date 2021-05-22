import asyncio
from datetime import datetime

from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

from FSM.Race_states import Race
from FSM.Registation_states import Registration_form
from constants.start_time import FINISH_REGISTRATION_TIME, START_RACE_TIME
from constants.text_messages import RULES, START_INFO
from keyboards.inline_kb import bicycle_type, gender, apply_registration, check_reg_answer, are_you_ready
from utils.loader import dp, db


# нажатие кнопки правила
@dp.callback_query_handler(text='rules')
async def rules(call: CallbackQuery):
    await call.answer(cache_time=55)
    await call.message.edit_text(f'{RULES}', reply_markup=apply_registration)


# нажатие кнопки "Регистрация"
@dp.callback_query_handler(text='start_reg')
async def reg(call: CallbackQuery):
    await call.message.edit_text(f'Привет {call.from_user.full_name}, укажи свой пол:',
                                 reply_markup=gender)
    await Registration_form.Sex.set()


# выбор пола и кнопка выбора велосипеда
@dp.callback_query_handler(state=Registration_form.Sex)
async def choose_sex(call: CallbackQuery, state: FSMContext):
    await call.answer(cache_time=1)
    answer = call.data
    await state.update_data(sex=answer)
    await db.update_racer_gender(gender=answer, id=call.from_user.id)
    await call.message.edit_text(f'В какой категории участвуешь?', reply_markup=bicycle_type)
    await Registration_form.next()


# выбор категории велосипеда кнопки выбора проверки ответов
@dp.callback_query_handler(state=Registration_form.Bicycle_type)
async def choose_bicycle_type(call: CallbackQuery, state: FSMContext):
    await call.answer(cache_time=1)
    answer = call.data
    await db.update_racer_bicycle(bicycle=answer, id=call.from_user.id)  # добавление в бд
    await state.update_data(bicycle_type=answer)
    data = await state.get_data()
    if data.get('sex') == 'male':
        sex = 'Ты выбрал'
    elif data.get('sex') == 'female':
        sex = 'Ты выбрала'
    else:
        sex = 'Ты еще не определился с полом (участвуешь вне зачета) и выбрал'

    if call.data == 'fixie':
        bicycle = 'фиксы 🚲'
    else:
        bicycle = 'мульти/синглспид 🚴'
    await call.message.edit_text(f'{sex} категорию: {bicycle}', reply_markup=check_reg_answer)
    await state.reset_state(with_data=False)
    racers = await db.select_all_racers()
    print(f'У нас новый гонщик! А вот все рейсеры: {racers}')  # проверка данных в бд


# исправление ошибок при регистрации
@dp.callback_query_handler(text='data_not_ok')
async def correcting(call: CallbackQuery, state: FSMContext):
    await call.answer(cache_time=1)
    await state.reset_data()
    await state.reset_state()
    await call.message.edit_text('Укажи еще раз свой пол:', reply_markup=gender)
    await Registration_form.Sex.set()


# информация о месте старта.
@dp.callback_query_handler(text='data_ok')
async def waiting_start(call: CallbackQuery):
    now = datetime.now().strftime('%d/%m/%y %H:%M:%S')
    if now < FINISH_REGISTRATION_TIME:
        await call.message.edit_text(text=START_INFO)
        while True:
            now_in_while = datetime.now().strftime('%d/%m/%y %H:%M:%S')
            if now_in_while < FINISH_REGISTRATION_TIME:
                await asyncio.sleep(1)
            else:
                count = await db.count_racers()
                await call.message.answer(f'Регистрация окончена, всего зарегистрировано: '
                                          f' {count} человек(а).\n\n'
                                          f'Сбор в 13:30 тут: <code>Устьинский сквер, Памятник Пограничникам Отечества</code>\n'
                                          f'Старт гонки оттуда же ровно в 14:00.')
                break
        while True:
            now_in_while_2 = datetime.now().strftime('%d/%m/%y %H:%M:%S')
            if now_in_while_2 >= START_RACE_TIME:
                await call.message.answer('Ты готов к гонке?', reply_markup=are_you_ready)
                await Race.FIRST_POINT.set()
                break
            else:
                await asyncio.sleep(1)

    else:
        await call.message.edit_text(
            text=f"Регистрация уже закрыта, следующий анонс будет <a href='vk.com/petushkislabachki'>тут</a>")
