'''Хендлер при нажатии команды /help'''
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp

'''Написать что-то дельное'''


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    await message.answer('Если ты потерялся совсем, то блблабла')
