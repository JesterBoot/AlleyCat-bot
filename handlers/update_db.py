from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import Command

from loader import dp, db
'''Осталось от урока sqlite'''

@dp.message_handler(Command("email"))
async def bot_start(message: types.Message, state: FSMContext):
    await message.answer("Пришли мне свой имейл")
    await state.set_state("email")


@dp.message_handler(state="email")
async def enter_email(message: types.Message, state: FSMContext):
    email = message.text
    db.update_user_email(email=email, id=message.from_user.id)
    racer = db.select_racer(id=message.from_user.id)
    await message.answer(f"Данные обновлены. Запись в БД: {racer}")
    await state.finish()
