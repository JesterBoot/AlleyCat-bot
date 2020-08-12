from aiogram.types.inline_keyboard import InlineKeyboardMarkup, InlineKeyboardButton

read_the_rules = InlineKeyboardMarkup(row_width=2,
                                      inline_keyboard=[
                                          [InlineKeyboardButton('Правила гонки ℹ️', callback_data='rules')]
                                      ])

send_to_friend = 'Регистрируйся на CyberAlleycat от MOSGORBIKE TEAM'

apply_registration = InlineKeyboardMarkup(row_width=2,
                                          inline_keyboard=[
                                              [InlineKeyboardButton('Регистрация ✔️', callback_data='start_reg'),
                                               InlineKeyboardButton('Пригласи друга на гонку',
                                                                    switch_inline_query=send_to_friend)]
                                          ])

bicycle_type = InlineKeyboardMarkup(row_width=2,
                                    inline_keyboard=[[InlineKeyboardButton('Фиксы 🚲', callback_data='fixie'),
                                                      InlineKeyboardButton('Мультиспид, синглы 🚴',
                                                                           callback_data='multispeed')]])

gender = InlineKeyboardMarkup(row_width=2,
                              inline_keyboard=[
                                  [InlineKeyboardButton('Мужской 🙎‍♂️', callback_data='male'),
                                   InlineKeyboardButton('Женский 🙎‍♀️', callback_data='female')],
                                  [InlineKeyboardButton('Еще не выбрал🏳️‍🌈(вне зачета) ', callback_data='trap')]
                              ])

check_reg_answer = InlineKeyboardMarkup(row_width=2,
                                        inline_keyboard=[
                                            [InlineKeyboardButton(text='Всё верно', callback_data='data_ok'),
                                             InlineKeyboardButton(text='Изменить данные',
                                                                  callback_data='data_not_ok')]
                                        ])

what_is_incorrect = InlineKeyboardMarkup(row_width=2,
                                         inline_keyboard=[
                                             [InlineKeyboardButton('Пол', callback_data='gender'),
                                              InlineKeyboardButton('Тип велосипеда', callback_data='bicycle_type')]
                                         ])
