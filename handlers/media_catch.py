import random

from aiogram import types

from data.stickers import STIKERS, ne_slishno
from data.text_messages import audio_answer, ne_pishi
from loader import dp


@dp.message_handler(content_types=types.ContentType.STICKER)
async def catch_sticker(message: types.Message):
    await message.answer_sticker(sticker=random.choice(STIKERS))


@dp.message_handler(content_types=types.ContentType.VOICE)
async def catch_sticker(message: types.Message):
    await message.answer_sticker(sticker=random.choice(ne_slishno))
    await message.answer(text=random.choice(audio_answer))


@dp.message_handler(content_types=types.ContentType.TEXT)
async def catch_sticker(message: types.Message):
    await message.answer(text=random.choice(ne_pishi))
