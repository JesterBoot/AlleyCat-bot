from handlers.command_info import send_mechanic, send_postponed_post
from utils.loader import db
from utils.set_bot_commands import set_default_commands
from utils.notify_admins import on_startup_notify
from aiogram import types


async def on_startup(dp):
    try:
        await db.create_table_racers()
    except:
        pass

    await on_startup_notify(dp)
    await set_default_commands(dp)
    await send_mechanic(types.Message)


if __name__ == '__main__':
    from aiogram import executor
    from handlers import dp

    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)
