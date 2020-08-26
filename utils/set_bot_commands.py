from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands([
        types.BotCommand("help", "Помощь"),
        types.BotCommand('delete', 'Удалить таблицу'),
        types.BotCommand('winner_fixie_men', 'победитель фиксы М')
    ])
