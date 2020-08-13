'''Хендлер при нажатии команды /start'''
import sqlite3

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from keyboards.inline_kb import read_the_rules
from loader import dp, db

welcome_message = '''Добро пожаловать на CyberAlleycat!
Блаблабла пару слов про гонку
Перед началом регистрации прочитай правила гонки.'''


@dp.message_handler(CommandStart())
async def bot_help(message: types.Message):#добавить date и регистрация до вечера пятницы
    await message.answer(welcome_message, reply_markup=read_the_rules)

    # name = message.from_user.first_name
    # second_name = message.from_user.last_name
    '''Добавляет юзера в базу данных при \старт'''
    # try:
    #     db.add_racer(id=message.from_user.id, name=name, second_name=second_name)
    # except sqlite3.IntegrityError as err:
    #     print(err)
    #
    # count_racers = db.count_users()[0]
    # await message.answer(
    #     '\n'.join([
    #         f'<b>{count_racers}</b> in database',
    #     ])
    # )
