from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

from FSM.Registation_states import Registration_form
from keyboards.inline_kb import bicycle_type, gender, apply_registration, check_reg_answer, what_is_incorrect

from loader import dp

'''Создать хендлеры группу коллбэков для каждого состояния'''

pravila = '''Нельзя ехать на машине
Можно ехать на велосипеде
и тд\n
Я согласен с условиями и готов регистрироваться'''


@dp.callback_query_handler(text='rules')  # нажатие кнопки правила
async def rules(call: CallbackQuery):
    await call.answer(cache_time=55)
    await call.message.edit_text(f'{pravila}', reply_markup=apply_registration)


@dp.callback_query_handler(text='start_reg')  # нажатие кнопки "Регистрация"
async def reg(call: CallbackQuery):
    await call.answer(cache_time=55)
    await call.message.edit_text(f'Привет {call.from_user.full_name}, укажи свой пол:',
                                 reply_markup=gender)
    await Registration_form.Sex.set()  # добавить имя пользоваиеля и @name в бд


@dp.callback_query_handler(state=Registration_form.Sex)  # выбор пола
# @dp.callback_query_handler(text='bicycle_type')
async def choose_sex(call: CallbackQuery, state: FSMContext):
    await call.answer(cache_time=55)
    answer = call.data
    await state.update_data(sex=answer)
    await call.message.edit_text(f'В какой категории участвуешь?', reply_markup=bicycle_type)
    await Registration_form.next()  # добавть пол в бд


# @dp.callback_query_handler(text='bicycle_type')
# async def reg(call: CallbackQuery):
#     await call.answer(cache_time=55)
#     await call.message.edit_text(f'{call.from_user.full_name}, укажи еще раз свой пол:',
#                                  reply_markup=gender)



@dp.callback_query_handler(state=Registration_form.Bicycle_type)  # выбор категории велосипеда
async def choose_bicycle_type(call: CallbackQuery, state: FSMContext):
    await call.answer(cache_time=55)
    data = await state.get_data()
    if data.get('sex') == 'male':
        sex = 'Ты выбрал'
    elif data.get('sex') == 'female':
        sex = 'Ты выбрала'
    else:
        sex = 'Ты еще не определился с полом (участвуешь вне зачета) и выбрал'

    if call.data == 'fixie':
        bicycle_type = 'фиксы 🚲'
    else:
        bicycle_type = 'мульти/синглспид 🚴'

    await call.message.edit_text(f'{sex} категорию: {bicycle_type}',
                                 reply_markup=check_reg_answer)
    await state.reset_state(with_data=False)  # занести все в бд


@dp.callback_query_handler(text='data_ok')  # информация о месте старта
async def waiting_start(call: CallbackQuery):
    await call.answer(cache_time=55)
    await call.message.edit_text('Отлично, старт гонки - Изваринская ул, дом 1.\n'
                                 'Начало гонки 1го сентября в 12.10.\n'
                                 'Перед стартом, тебе придет сообщение от бота, так что не выключай оповещения.\n'
                                 'Не приезжай на точку старта слишком рано и пользуйся санитайзером.')


@dp.callback_query_handler(text='data_not_ok')  # исправление ошибок при регистрации
async def pravki(call: CallbackQuery):
    await call.answer(cache_time=55)
    await call.message.edit_text('Что нужно изменить?',
                                 reply_markup=what_is_incorrect)  # добавить клавиши с состояниями для правок



