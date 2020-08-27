import asyncio

from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery
from time import time, ctime
import datetime

from FSM.Race_states import Race
from FSM.Registation_states import Registration_form
from keyboards.inline_kb import bicycle_type, gender, apply_registration, check_reg_answer, are_you_ready
from loader import dp, db



rule = '''
Нельзя ехать на машине
Можно ехать на велосипеде и тд\n
Для быстрого копирования названия точки ты можешь просто нажать на текст и он скопируется, как на этом примере:\n
<code>Улица Пушкина, дом Колотушкина</code>\n
Таким образом, ты можешь быстро копировать название точки и вставлять его в поисковике на картах.\n
Для подверждения, нужно будет отправлять селфи  или фото твоего велосипеда с объектом на заднем фоне.\n
Cогласен с условиями и готов к регистрации.
'''


# нажатие кнопки правила
@dp.callback_query_handler(text='rules')
async def rules(call: CallbackQuery):
    await call.answer(cache_time=55)
    await call.message.edit_text(f'{rule}', reply_markup=apply_registration)



# нажатие кнопки "Регистрация"
@dp.callback_query_handler(text='start_reg')
async def reg(call: CallbackQuery):
    await call.message.edit_text(f'Привет {call.from_user.full_name}, укажи свой пол:',
                                 reply_markup=gender)
    await Registration_form.Sex.set()  # добавить имя пользоваиеля и @name в бд


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
    await db.update_racer_bicycle(bicycle=answer, id=call.from_user.id)#добавление в бд
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
    print(f'Получил всех пользователей: {racers}')#проверка данных в бд


# исправление ошибок при регистрации
@dp.callback_query_handler(text='data_not_ok')
async def pravki(call: CallbackQuery, state: FSMContext):
    await call.answer(cache_time=1)
    await state.reset_data()
    await state.reset_state()
    await call.message.edit_text('Укажи еще раз свой пол:', reply_markup=gender)
    await Registration_form.Sex.set()


# информация о месте старта
info = '''
<code>Устьинский сквер, Памятник Пограничникам Отечества</code>\n
Сбор 01.01.2020 в 12.00, начало гонки в 12.10.
Перед стартом, тебе придет сообщение от бота, так что <b>не выключай</b> оповещения.
'''
@dp.callback_query_handler(text='data_ok')
async def waiting_start(call: CallbackQuery, state: FSMContext):
    await call.message.edit_text(text='Отлично, место старта гонки:\n' + info)

    # while ctime() != 'Sat Aug 22 09:35:00 2020':
    #     await asyncio.sleep(1)
    # else:
    # count = await db.count_racers()
    # await call.message.answer(f'Регистрация окончена, всего зарегистрировано: {count} человек(а).')

    # while ctime() != 'Sat Aug 22 12:10:00 2020':
    #     await asyncio.sleep(1)
    # else:
    await call.message.answer('Ты готов к гонке?', reply_markup=are_you_ready)
    await Race.First_point.set()


