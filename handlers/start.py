'''Хендлер при нажатии команды /start'''
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from constants.text_messages import welcome_message
from keyboards.inline_kb import read_the_rules
from alleycat_bot.loader import dp, db


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(welcome_message, reply_markup=read_the_rules, parse_mode=types.ParseMode.HTML,
                         disable_web_page_preview=True)
    name = message.from_user.full_name
    await db.add_racer(id=message.from_user.id, name=name)
