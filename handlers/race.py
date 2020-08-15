from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

from FSM.Race_states import Race
from data.locations import MY_HOME
from keyboards.inline_kb import got_the_point
from keyboards.reply_kb import get_location_button
from loader import dp

# Ты админ цуклинга. Две кнопки "забанить" , "забанить"
'''расставить стейкты и разобраться с локацией'''
@dp.callback_query_handler(state=Race.First_point)
async def get_location(call: CallbackQuery, state: FSMContext):
    await call.answer(cache_time=55)
    await call.message.delete()
    await call.message.answer('Отправь своё местоположение 🗺.\nКнопка снизу ⬇️',
                              reply_markup=get_location_button)
    await state.finish()

'''не понимаю как распаковать дикт и как это внести '''
@dp.message_handler(content_types=types.ContentType.LOCATION)
async def selfie_query(message: types.Message, state: FSMContext):
    print(message.location)
    # print('{:.2f}'.format(message.location.latitude))
    # print('{:.3f}'.format(message.location.longitude))
    # print(MY_HOME[0])
    # print(MY_HOME[1])
    # if '{:.2f}'.format(message.location.latitude) == MY_HOME[0] and '{:.3f}'.format(message.location.longitude) == MY_HOME[1]:
    #     await message.answer('Ты на месте!\nДля подтверждения, отправь селфи')
    # else:
    #     await message.answer('Ты далеко от точки, попробуй еще раз', reply_markup=get_location_button)


@dp.message_handler(content_types=types.ContentType.PHOTO)
async def get_selfie(message: types.Message, state: FSMContext):
    point = 'Храм Христа Спасителя'
    # if state.get_state()=='blabla':
    #     pass
    await message.answer(f'Отличная фотка, дуй на следующую точку {point}',
                         reply_markup=got_the_point)


