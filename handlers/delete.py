from aiogram import types
from aiogram.dispatcher.filters.builtin import Command

from loader import dp, db


@dp.message_handler(Command('delete'))
async def bot_help(message: types.Message):
    await db.delete_racers()
    await message.answer('Данные из таблицы были удалены')
    print('Данные из таблицы были удалены')
    racers = await db.select_all_racers()
    print(f'Получил всех пользователей: {racers}')