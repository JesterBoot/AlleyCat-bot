from aiogram.dispatcher.filters.builtin import Command
from data.config import admins
from aiogram import types, Dispatcher

from loader import dp, db, bot

'''не запихивается в строку(((('''
@dp.message_handler(Command('winner_fixie_men'))
async def got_selfie_catholic(message: types.Message):

    male_winners = str(await db.male_fixie_winners())
    print(male_winners)
    # for admin in admins:
    # await message.answer(f'Победители фиксы, мужской зачет: {male_winners}')
    # except:
    #     print('pipiski')