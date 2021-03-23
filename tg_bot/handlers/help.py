from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from utils.loader import dp


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    await message.answer('Никак не можешь отправить правильную локацию?\n'
                         'Пиши в лс @GeorgeBi')
