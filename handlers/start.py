from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from constants.text_messages import WELCOME_MESSAGE, RESTART_RACE
from keyboards.inline_kb import read_the_rules, change_reg_data
from utils.loader import dp, db


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(WELCOME_MESSAGE,
                         reply_markup=read_the_rules,
                         parse_mode=types.ParseMode.HTML,
                         disable_web_page_preview=True
                         )
    name = message.from_user.full_name
    await db.add_racer(id=message.from_user.id, name=name)


async def restart_race(message: types.Message):
    racers = await db.select_all_racers()
    if len(racers) > 0:
        for racer in racers:
            try:
                await dp.bot.send_message(racer['id'], RESTART_RACE, reply_markup=change_reg_data)
            except:
                pass
    else:
        await message.answer("Пока никто не зарегистрировался.")
