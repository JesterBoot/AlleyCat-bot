from aiogram import types

from aiogram import Dispatcher
from aiogram.dispatcher.filters.builtin import Command

from data.config import admins
from loader import dp, db

#победители фиксы
@dp.message_handler(Command('winners_fixie'))
async def winners_fixie(dp: Dispatcher):
    male_result = ''
    female_result = ''
    try:
        male_winners = dict(await db.male_fixie_winners())
        for key, value in male_winners.items():
            male_result += key + ' - '
            male_result += value + '\n'
    except:
        male_result = 'Никто не приехал'
    try:
        female_winners = dict(await db.female_fixie_winners())
        for key, value in female_winners.items():
            female_result += key + ' - '
            female_result += value + '\n'
    except:
        female_result = 'Никто не приехал'

    for admin in admins:
        await dp.bot.send_message(admin, text=f'Победители фиксы, мужской зачет:\n{male_result}')
        await dp.bot.send_message(admin, text=f'Победители фиксы, женский зачет:\n{female_result}')


#победители мульти/сингл спид
@dp.message_handler(Command('winners_multi'))
async def winners_multispeed(dp: Dispatcher):
    male_result = ''
    female_result = ''
    try:
        male_winners = dict(await db.male_multispeed_winners())
        for key, value in male_winners.items():
            male_result += key + ' - '
            male_result += value + '\n'
    except:
        male_result = 'Никто не приехал'
    try:
        female_winners = dict(await db.female_multispeed_winners())
        for key, value in female_winners.items():
            female_result += key + ' - '
            female_result += value + '\n'
    except:
        female_result = 'Никто не приехал'

    for admin in admins:
        await dp.bot.send_message(admin, text=f'Победители мультиспид/синглы, мужской зачет:\n{male_result}')
        await dp.bot.send_message(admin, text=f'Победители мультиспид/синглы, женский зачет:\n{female_result}')


# общий зачет гонки
@dp.message_handler(Command('results'))
async def racers_time(message: types.Message):
    result = ''
    place = 0
    try:
        racers_time = dict(await db.all_racers_time())
        for key, value in racers_time.items():
            result += key + ' - '
            result += value + '\n'
            place += 1
        await message.answer(f'Общий зачет:\n\n{place} - {result}')
    except:
        await message.answer(f'Пока никто не финишировал')
