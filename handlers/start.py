'''Хендлер при нажатии команды /start'''
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from keyboards.inline_kb import read_the_rules
from loader import dp, db

welcome_message = '''
Добро пожаловать на CyberAlleycat!
Блаблабла пару слов про гонку
Для начала - пройди регистрацию'''


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    # if message.from_user.id !=
    await message.answer(welcome_message, reply_markup=read_the_rules)
    name = message.from_user.full_name
    await db.add_racer(id=message.from_user.id, name=name)
    racers = await db.select_all_racers()
    print(f'Получил всех пользователей: {racers}')



