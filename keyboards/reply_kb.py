from aiogram.types.reply_keyboard import ReplyKeyboardMarkup, KeyboardButton

get_location_button = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Отправь своё местоположение 🗺',
                                                             request_location=True)]], resize_keyboard=True)

