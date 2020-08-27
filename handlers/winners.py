import re

from aiogram.dispatcher.filters.builtin import Command
from data.config import admins
from aiogram import types, Dispatcher

from loader import dp, db

'''н'''
@dp.message_handler(Command('winner_fixie_men'))
async def get_winners(message: types.Message):
    male_winners = str(await db.male_fixie_winners())
    print(male_winners)
    male_winners = male_winners.replace("<Record name='", '')
    male_winners = male_winners.replace(""time='")
    male_winners = male_winners.split('_')
    print(male_winners)

    # await message.answer(winners)
    # for admin in admins:
    # await message.reply(f'Победители фиксы, мужской зачет: {male_winners}')

    #     print() По команде/winner список всех победителей во всех зачетах