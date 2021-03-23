import random

from aiogram import types

from constants.stickers import STIKERS, cant_hear_you
from constants.text_messages import audio_answer, dont_write_to_me
from utils.loader import dp


@dp.message_handler(content_types=types.ContentType.STICKER)
async def catch_sticker(message: types.Message):
    await message.answer_sticker(sticker=random.choice(STIKERS))


@dp.message_handler(content_types=types.ContentType.VOICE)
async def catch_sticker(message: types.Message):
    await message.answer_sticker(sticker=random.choice(cant_hear_you))
    await message.answer(text=random.choice(audio_answer))


@dp.message_handler(content_types=types.ContentType.TEXT)
async def catch_sticker(message: types.Message):
    await message.answer(text=random.choice(dont_write_to_me))
