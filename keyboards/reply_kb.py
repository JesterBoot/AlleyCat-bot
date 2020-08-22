from aiogram.types.reply_keyboard import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

get_location_button = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Отправь своё местоположение 🗺',
                                                                    request_location=True)]], resize_keyboard=True,
                                          one_time_keyboard=True)

remove_keyboard = ReplyKeyboardRemove()
