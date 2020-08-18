from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

from FSM.Race_states import Race
from data.locations import points
from keyboards.inline_kb import got_the_point, cycling_admin
from keyboards.reply_kb import get_location_button
from loader import dp


# запрос локации на точке старта
@dp.callback_query_handler(state=Race.First_point)
async def get_location(call: CallbackQuery, state: FSMContext):
    await call.answer(cache_time=3)
    await call.message.delete()
    await call.message.answer('Отправь своё местоположение 🗺.\nКнопка снизу ⬇️',
                              reply_markup=get_location_button)
    await state.reset_state()


#уловитель локации и сортировка по самой локации
@dp.message_handler(content_types=types.ContentType.LOCATION)
async def selfie_query(message: types.Message):
    message.location["latitude"] = float(f'{message.location["latitude"]:.3f}')
    message.location["longitude"] = float(f'{message.location["longitude"]:.3f}')
    if dict(message.location) == points['Устьинский сквер, Памятник Пограничникам Отечества']:
        await message.answer('Ты на месте!\nДля подтверждения, отправь селфи')
        await Race.Christ_the_savior.set()
    elif dict(message.location) == points['Христа Спасителя']:
        await message.answer('Ты на месте!\nДля подтверждения, отправь селфи')
        await Race.Catholic_cathedral.set()
    elif dict(message.location) == points['Римско-католический Кафедральный собор Непорочного ' \
                                          'Зачатия Пресвятой Девы Марии']:
        await message.answer('Ты на месте!\nДля подтверждения, отправь селфи')
        await Race.Allaah.set()
    elif dict(message.location) == points['Московская соборная мечеть']:
        await message.answer('Ты на месте!\nДля подтверждения, отправь селфи')
        await Race.Seynagogue.set()
    elif dict(message.location) == points['Московская хоральная синагога']:
        await message.answer('Ты на месте!\nДля подтверждения, отправь селфи')
        await Race.Evangelical.set()
    elif dict(message.location) == points['Евангелическо-лютеранский кафедральный собор святых Петра и Павла']:
        await message.answer('Ты на месте!\nДля подтверждения, отправь селфи')
        await Race.Scientology.set()
    elif dict(message.location) == points['Московская саентологическая церковь']:
        await message.answer('Ты на месте!\nДля подтверждения, отправь селфи')
        await Race.Mosgorbike.set()
    elif dict(message.location) == points['Mosgorbike']:
        await message.answer('Ты на месте!\nДля подтверждения, отправь селфи')
        await Race.Finish.set()
    else:
        await message.answer('Ты далеко от точки, попробуй еще раз', reply_markup=get_location_button)
        print(dict(message.location))  # оставлю для тестов
        print(points['Устьинский сквер, Памятник Пограничникам Отечества'])  # оставлю для тестов


#подверждение фото со стейтами
@dp.message_handler(content_types=types.ContentType.PHOTO, state=Race.Christ_the_savior)
async def got_selfie_christ(message: types.Message, state: FSMContext):
    await state.reset_state()
    await message.answer(f'Отличная фотка, дуй на следующую точку:\n{points}',
                         reply_markup=got_the_point)


@dp.message_handler(content_types=types.ContentType.PHOTO, state=Race.Catholic_cathedral)
async def got_selfie_catholic(message: types.Message, state: FSMContext):
    await state.reset_state()
    await message.answer('А теперь представь, что ты админ цуклинга.\n'
                         'У тебя на стене оставили комментарий, что ты сделаешь?',
                         reply_markup=cycling_admin)


@dp.message_handler(text='ban')
@dp.message_handler(text='ban_too')
async def got_banned(message: types.Message):
    await message.answer('Все комментаторы забанены! Езжай на следующую точку:\n'
                         'Римско-католический Кафедральный собор Непорочного Зачатия Пресвятой Девы Марии',
                         reply_markup=got_the_point)


@dp.message_handler(content_types=types.ContentType.PHOTO, state=Race.Allaah)
async def got_selfie_allah(message: types.Message, state: FSMContext):
    await state.reset_state()
    await message.answer('Отличная фотка, дуй на следующую точку:\n'
                         'Московская соборная мечеть',
                         reply_markup=got_the_point)


@dp.message_handler(content_types=types.ContentType.PHOTO, state=Race.Seynagogue)
async def got_selfie_seynagogue(message: types.Message, state: FSMContext):
    await state.reset_state()
    await message.answer('Отличная фотка, дуй на следующую точку:\n'
                         'Московская хоральная синагога',
                         reply_markup=got_the_point)


@dp.message_handler(content_types=types.ContentType.PHOTO, state=Race.Evangelical)
async def got_selfie_evangelical(message: types.Message, state: FSMContext):
    await state.reset_state()
    await message.answer('Отличная фотка, дуй на следующую точку:\n'
                         'Евангелическо-лютеранский кафедральный собор святых Петра и Павла',
                         reply_markup=got_the_point)


@dp.message_handler(content_types=types.ContentType.PHOTO, state=Race.Scientology)
async def got_selfie_scientology(message: types.Message, state: FSMContext):
    await state.reset_state()
    await message.answer('Отличная фотка, дуй на следующую точку:\n'
                         'Московская саентологическая церковь',
                         reply_markup=got_the_point)


@dp.message_handler(content_types=types.ContentType.PHOTO, state=Race.Mosgorbike)
async def got_selfie_mosgorbike(message: types.Message, state: FSMContext):
    await state.reset_state()
    await message.answer('Отличная фотка, дуй на следующую точку:\n'
                         'Mosgorbike',
                         reply_markup=got_the_point)


@dp.message_handler(content_types=types.ContentType.PHOTO, state=Race.Finish)
async def got_selfie_finish(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer('Поздравляю, ты добрался до последней точки, готовься к награждению!')
    await message.answer_sticker(sticker='CAACAgIAAxkBAAEBNehfOYqypKm5tQW7ighPme49OflY7gACaAADq8pZIY2MuYKiZ0KSGgQ')


#запрос локации
@dp.callback_query_handler(text='got_the_point')
async def get_location(call: CallbackQuery, state: FSMContext):
    await call.answer(cache_time=3)
    await call.message.delete()
    await call.message.answer('Отправь своё местоположение 🗺\nКнопка снизу ⬇️',
                              reply_markup=get_location_button)
