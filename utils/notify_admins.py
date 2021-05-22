import logging
import os

from aiogram import Dispatcher

from utils.config import admins


async def on_startup_notify(dp: Dispatcher):
    try:
        for admin in admins:
            await dp.bot.send_message(chat_id=admin, text='Бот Запущен')

    except Exception as err:
        logging.exception(err)
