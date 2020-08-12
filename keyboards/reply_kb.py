from aiogram.types.reply_keyboard import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, \
    KeyboardButtonPollType

get_location = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Отправь свою локацию 🗺', request_location=True)]],
                                   resize_keyboard=True)
