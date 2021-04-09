from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from constants.text_messages import WELCOME_MESSAGE
from keyboards.inline_kb import read_the_rules
from utils.db.db_commands import add_racer
from utils.loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(WELCOME_MESSAGE,
                         reply_markup=read_the_rules,
                         parse_mode=types.ParseMode.HTML,
                         disable_web_page_preview=True
                         )
    user = await add_racer(telegram_id=message.from_user.id,
                           fullname=message.from_user.full_name,
                           username=message.from_user.username)
    print(user)
