import logging

from aiogram import Dispatcher

from constants.text_messages import FOR_ADMINS
from utils.config import admins


async def on_startup_notify(dp: Dispatcher):
    try:
        for admin in admins:
            await dp.bot.send_message(chat_id=admin, text=FOR_ADMINS)
    except Exception as err:
        logging.exception(err)
