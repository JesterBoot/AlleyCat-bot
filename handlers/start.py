'''Хендлер при нажатии команды /start'''
import asyncpg
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from keyboards.inline_kb import read_the_rules
from loader import dp, db

welcome_message = '''Добро пожаловать на CyberAlleycat!
Блаблабла пару слов про гонку
Перед началом регистрации прочитай правила гонки.'''


# @dp.message_handler(CommandStart())
# async def bot_help(message: types.Message):#добавить date и регистрация до вечера пятницы
#     await message.answer(welcome_message, reply_markup=read_the_rules)


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    name = message.from_user.full_name
    try:
        await db.add_user(id=message.from_user.id,
                          name=name)
    except asyncpg.exceptions.UniqueViolationError:
        pass
    count = await db.count_users()
    await message.answer(
        "\n".join(
            [
                f'Привет, {message.from_user.full_name}!',
                f'Ты был занесен в базу',
                f'В базе <b>{count}</b> пользователей',
            ]))
