import random

from aiogram import types

from loader import dp

#может добавить еще несколько стикеров, в целом все ок
STIKERS = ['CAACAgIAAxkBAAEBFIFfFy53DFJBAt0eGSwZEMzv8fQkfwAC6QcAAvoLtgiG3er2ahNmXxoE',
           'CAACAgIAAxkBAAEBFH1fFy4kIQABI73GGIz9fnx3AU7V1BAAAgsAA2v--RKeNMHpSoi6LRoE',
           'CAACAgIAAxkBAAEBNcNfOVbjRewriKHkhVmSr8t7sU-xVAACBwADFgqsEA7M9oZNeed8GgQ',
           'CAACAgIAAxkBAAEBNd5fOYpJcy1g5X9jBPcSTJ3prlc2MAACWgADq8pZIb4PS42uN-U_GgQ',
           'CAACAgIAAxkBAAEBNe5fOYrgly-koyAmA-2Y_032gc4uJAACMgADq8pZIf-utREdSfLYGgQ',
           'CAACAgIAAxkBAAEBNfhfOYu2O_47vRA7Q7NjiPvgpC_AFQACQQADq8pZIR5qydh5tpkbGgQ',]


@dp.message_handler(content_types=types.ContentType.STICKER)
async def catch_sticker(message: types.Message):
    await message.answer_sticker(sticker=random.choice(STIKERS))

ne_pishi = ['''
— Привет, я подсяду? Спасибо.
— Почему у меня велосипед без тормозов? Ну, просто мне понравился парень.
— Поддерживаю ли я МГБТ? Да.
— Да, я являюсь частью сообщества. А почему ты спрашиваешь?
— В смысле навязываю тебе что-то? Так ты же сам спросил. Ладно.
— Хочу ли я свою подругу? Боже, нет, конечно. Почему я должен её хотеть?
— В смысле всех? Нет, постой, это не так работает немножко. Тебе объяснить?
— Не надо пропагандировать? Я не пропагандирую, ты просто сам спросил у меня… 
- Ясно, я сумасшедший. Как и все. Ладно, извини, что потревожил. Я отсяду.
''',
'Не пиши мне больше!']


@dp.message_handler(content_types=types.ContentType.TEXT)
async def catch_sticker(message: types.Message):
    await message.answer(text=random.choice(ne_pishi))


audio_answer = ['Я без наушников, лучше напиши',
                'Пожалуйства, повтори еще раз',
                'Тебя не слышно, говори громче', ]



ne_slishno = ['CAACAgIAAxkBAAEBNf5fOYvSU3-z12_NdfsdyWNXLg1megACNgADq8pZIRE8LKnNnjwnGgQ',
              'CAACAgIAAxkBAAEBNfBfOYrw2ovs8wh0QqgHlLs-VkICDwACNQADq8pZIepTmAUSKLd2GgQ']
@dp.message_handler(content_types=types.ContentType.VOICE)
async def catch_sticker(message: types.Message):
    await message.answer(text=random.choice(audio_answer))
    await message.answer_sticker(sticker=random.choice(ne_slishno))
