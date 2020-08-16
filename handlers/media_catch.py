'''Написать хендлеры на ловлю стикеров, тескта и остального'''
from aiogram import types
import random

from loader import dp
'''подобрать и добавить стикеры'''
STIKERS = ['CAACAgIAAxkBAAEBFIFfFy53DFJBAt0eGSwZEMzv8fQkfwAC6QcAAvoLtgiG3er2ahNmXxoE',
           'CAACAgIAAxkBAAEBFH1fFy4kIQABI73GGIz9fnx3AU7V1BAAAgsAA2v--RKeNMHpSoi6LRoE',
           'CAACAgIAAxkBAAEBNcNfOVbjRewriKHkhVmSr8t7sU-xVAACBwADFgqsEA7M9oZNeed8GgQ',]

@dp.message_handler(content_types=types.ContentType.STICKER)
async def catch_sticker(message: types.Message):
    await message.answer_sticker(sticker=random.choice(STIKERS))



