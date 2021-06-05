import logging

from aiogram import Dispatcher

from constants.text_messages import FOR_ADMINS


async def on_startup_notify(dp: Dispatcher):
    try:
        await dp.bot.send_message(chat_id=412112889, text=FOR_ADMINS)
    except Exception as err:
        logging.exception(err)
