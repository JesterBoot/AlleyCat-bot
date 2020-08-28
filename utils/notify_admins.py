import logging

from aiogram import Dispatcher


async def on_startup_notify(dp: Dispatcher):
    try:
        await dp.bot.send_message(chat_id=412112889, text='Бот Запущен')

    except Exception as err:
        logging.exception(err)
