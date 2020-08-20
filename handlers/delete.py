from aiogram import types
from aiogram.dispatcher.filters.builtin import Command

from loader import dp, db


@dp.message_handler(Command('delete'))
async def bot_help(message: types.Message):
    await db.delete_table()
    await message.answer('Таблица была удалена')
    print('Таблица была удалена')
