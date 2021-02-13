from aiogram import types
from aiogram.dispatcher.filters.builtin import Command

from utils.loader import dp, db


@dp.message_handler(Command('delete'))
async def bot_delete_table(message: types.Message):
    await db.delete_racers()
    await message.answer('Таблицы были удалены')
    print('Таблицы были удалены')
