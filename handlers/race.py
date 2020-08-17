from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

from FSM.Race_states import Race
from data.locations import START_POINT, CHRIST_THE_SAVIOR, CATHOLIC_CATHEDRAL, ALLAAH, SEYNAGOUE, \
    EVANGELICAL_LUTHERAN_CATHEDRAL, SCIENTOLOGY, MOSGORBIKE
from keyboards.inline_kb import got_the_point
from keyboards.reply_kb import get_location_button
from loader import dp

# Ты админ цуклинга. Две кнопки "забанить" , "забанить"
'''расставить стейкты и разобраться с локацией'''


@dp.callback_query_handler(state=Race.First_point)
async def get_location(call: CallbackQuery, state: FSMContext):
    await call.answer(cache_time=3)
    await call.message.delete()
    await call.message.answer('Отправь своё местоположение 🗺.\nКнопка снизу ⬇️',
                              reply_markup=get_location_button)
    await state.reset_state()


'''все сделал в locations 
нужно теперь переделалть стейты'''


@dp.message_handler(content_types=types.ContentType.LOCATION)
async def selfie_query(message: types.Message):
    print(message.location)
    latitute = float('{:.2f}'.format(message.location.latitude))
    longitude = float('{:.2f}'.format(message.location.longitude))
    print(float('{:.2f}'.format(message.location.latitude)), START_POINT[0])
    print(float('{:.2f}'.format(message.location.longitude)), START_POINT[1])
    if latitute == START_POINT[0] and longitude == START_POINT[1]:
        await message.answer('Ты на месте!\nДля подтверждения, отправь селфи')
        await Race.Christ_the_savior.set()
    elif latitute == CHRIST_THE_SAVIOR[0] and longitude == CHRIST_THE_SAVIOR[1]:
        await message.answer('Ты на месте!\nДля подтверждения, отправь селфи')
        await Race.Catholic_cathedral.set()
    elif latitute == CATHOLIC_CATHEDRAL[0] and longitude == CATHOLIC_CATHEDRAL[1]:
        await message.answer('Ты на месте!\nДля подтверждения, отправь селфи')
        await Race.Allaah.set()
    elif latitute == ALLAAH[0] and longitude == ALLAAH[1]:
        await message.answer('Ты на месте!\nДля подтверждения, отправь селфи')
        await Race.Allaah.set()
    elif latitute == ALLAAH[0] and longitude == ALLAAH[1]:
        await message.answer('Ты на месте!\nДля подтверждения, отправь селфи')
        await Race.Seynagogue.set()
    elif latitute == SEYNAGOUE[0] and longitude == SEYNAGOUE[1]:
        await message.answer('Ты на месте!\nДля подтверждения, отправь селфи')
        await Race.Evangelical.set()
    elif latitute == EVANGELICAL_LUTHERAN_CATHEDRAL[0] and longitude == EVANGELICAL_LUTHERAN_CATHEDRAL[1]:
        await message.answer('Ты на месте!\nДля подтверждения, отправь селфи')
        await Race.Scientology.set()
    elif latitute == SCIENTOLOGY[0] and longitude == SCIENTOLOGY[1]:
        await message.answer('Ты на месте!\nДля подтверждения, отправь селфи')
        await Race.Mosgorbike.set()
    elif latitute == MOSGORBIKE[0] and longitude == MOSGORBIKE[1]:
        await message.answer('Ты на месте!\nДля подтверждения, отправь селфи')
        await Race.Finish.set()
    else:
        await message.answer('Ты далеко от точки, попробуй еще раз', reply_markup=get_location_button)


@dp.message_handler(content_types=types.ContentType.PHOTO, state=Race.Christ_the_savior)
async def got_selfie_christ(message: types.Message, state: FSMContext):
    await state.reset_state()
    await message.answer(f'Отличная фотка, дуй на следующую точку:\nХрам Христа Спасителя',
                         reply_markup=got_the_point)


@dp.message_handler(content_types=types.ContentType.PHOTO, state=Race.Catholic_cathedral)
async def got_selfie_catholic(message: types.Message, state: FSMContext):
    await state.reset_state()
    await message.answer('Отличная фотка, дуй на следующую точку:\n'
                         'Римско-католический Кафедральный собор Непорочного Зачатия Пресвятой Девы Марии',
                         reply_markup=got_the_point)


@dp.message_handler(content_types=types.ContentType.PHOTO, state=Race.Allaah)
async def got_selfie_allah(message: types.Message, state: FSMContext):
    await state.reset_state()
    await message.answer('Отличная фотка, дуй на следующую точку:\n'
                         'Московская соборная мечеть',
                         reply_markup=got_the_point)


@dp.message_handler(content_types=types.ContentType.PHOTO, state=Race.Seynagogue)
async def got_selfie_allah(message: types.Message, state: FSMContext):
    await state.reset_state()
    await message.answer('Отличная фотка, дуй на следующую точку:\n'
                         'Московская хоральная синагога',
                         reply_markup=got_the_point)


@dp.message_handler(content_types=types.ContentType.PHOTO, state=Race.Evangelical)
async def got_selfie_allah(message: types.Message, state: FSMContext):
    await state.reset_state()
    await message.answer('Отличная фотка, дуй на следующую точку:\n'
                         'Евангелическо-лютеранский кафедральный собор святых Петра и Павла',
                         reply_markup=got_the_point)


@dp.message_handler(content_types=types.ContentType.PHOTO, state=Race.Scientology)
async def got_selfie_allah(message: types.Message, state: FSMContext):
    await state.reset_state()
    await message.answer('Отличная фотка, дуй на следующую точку:\n'
                         'Московская саентологическая церковь',
                         reply_markup=got_the_point)


@dp.message_handler(content_types=types.ContentType.PHOTO, state=Race.Mosgorbike)
async def got_selfie_allah(message: types.Message, state: FSMContext):
    await state.reset_state()
    await message.answer('Отличная фотка, дуй на следующую точку:\n'
                         'Mosgorbike',
                         reply_markup=got_the_point)


@dp.message_handler(content_types=types.ContentType.PHOTO, state=Race.Finish)
async def got_selfie_allah(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer('Поздравляю, ты добрался до последней точки, готовься к награждению')
    await message.answer_sticker(sticker='CAACAgIAAxkBAAEBNehfOYqypKm5tQW7ighPme49OflY7gACaAADq8pZIY2MuYKiZ0KSGgQ')


@dp.callback_query_handler(text='got_the_point')
async def get_location(call: CallbackQuery, state: FSMContext):
    await call.answer(cache_time=3)
    await call.message.delete()
    await call.message.answer('Отправь своё местоположение 🗺.\nКнопка снизу ⬇️',
                              reply_markup=get_location_button)
    print(await state.get_state())
