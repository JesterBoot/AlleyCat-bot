from aiogram import types, Dispatcher
from aiogram.dispatcher.filters.builtin import Command

from data.config import admins
from loader import dp, db

'''Победители фиксы, мужской зачет'''
@dp.message_handler(Command('winner_fixie_men'))
async def get_winners(dp: Dispatcher):
    result = ''
    male_winners = dict(await db.male_fixie_winners())
    for key, value in male_winners.items():
        result += key + ' - '
        result += value + '\n'
    for admin in admins:
        await dp.bot.send_message(admin, text=f'Победители фиксы, мужской зачет:\n{result}')
