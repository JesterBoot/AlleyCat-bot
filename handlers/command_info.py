from aiogram import types
from aiogram.dispatcher.filters.builtin import Command

from FSM.Race_states import Race
from constants.text_messages import RACE_MECHANIC
from keyboards.inline_kb import are_you_ready, confirm_participation
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
                await dp.bot.send_message(racer['id'], mess)
        else:
            await message.answer("Пока никто не зарегистрировался.")


@dp.message_handler(Command('send'), user_id=admins)
async def send_mechanic(message: types.Message):
    racers = await db.select_all_racers()
    if len(racers) > 0:
        for racer in racers:
            await dp.bot.send_message(racer['id'], text=RACE_MECHANIC,
                                      reply_markup=confirm_participation)
    else:
        await message.answer("Пока никто не зарегистрировался.")


@dp.message_handler(Command('fail'), user_id=admins)
async def fail(message: types.Message):
    """ Жми команду, если ничего не сработает автоматически. """

    racers = await db.select_all_racers()
    if len(racers) > 0:
        for racer in racers:
            await dp.bot.send_message(racer['id'], 'Ты готов к гонке?', reply_markup=are_you_ready)
            await Race.FIRST_POINT.set()
    else:
        await message.answer("Пока никто не зарегистрировался.")
