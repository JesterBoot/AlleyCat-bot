'''Хендлер при нажатии команды /help'''
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    await message.answer('Список команд: \n'
                         '/help - Получить справку\n')
