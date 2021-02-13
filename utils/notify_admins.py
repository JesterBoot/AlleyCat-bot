import logging
import os

from aiogram import Dispatcher


async def on_startup_notify(dp: Dispatcher):
    try:
        await dp.bot.send_message(chat_id=os.getenv('ADMINS'), text='Бот Запущен')

    except Exception as err:
        logging.exception(err)
