from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands([
        types.BotCommand('help', 'Жми, если не можешь отправить локацию'),
        types.BotCommand('results', 'Посмотреть общий зачет гонки')
    ])
