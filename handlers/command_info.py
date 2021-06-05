from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import Command

from FSM.Registation_states import Registration_form
from constants.text_messages import START_INFO
from keyboards.inline_kb import are_you_ready, gender
from utils.config import admins
from utils.loader import dp, db


@dp.message_handler(Command('send_all'), user_id=admins)
async def send_all(message: types.Message):
    racers = await db.select_all_racers()
    mess = message.text[9:]
    if len(mess) < 1:
        await message.answer("Слишком короткое сообщение.")
    else:
        if len(racers) > 0:
            for racer in racers:
                try:
                    await dp.bot.send_message(racer['id'], mess)
                except:
                    pass
        else:
            await message.answer("Пока никто не зарегистрировался.")


@dp.message_handler(Command('start_race'), user_id=admins)
async def start_race(message: types.Message):

    racers = await db.select_all_racers()
    if len(racers) > 0:
        for racer in racers:
            try:
                await dp.bot.send_message(racer['id'], 'Мы начинаем!\nТы готов к гонке?', reply_markup=are_you_ready)
            except:
                pass
    else:
        await message.answer("Пока никто не зарегистрировался.")


@dp.message_handler(Command('info'))
async def send_info(message: types.Message):
    await message.answer(START_INFO)


@dp.message_handler(Command('change'))
async def change_reg_info(message: types.Message, state: FSMContext):
    await state.reset_data()
    await state.reset_state()
    await message.answer('Укажи еще раз свой пол:', reply_markup=gender)
    await Registration_form.Sex.set()
