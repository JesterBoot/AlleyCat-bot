from utils.set_bot_commands import set_default_commands
# from loader import db


async def on_startup(dp):
    from utils.notify_admins import on_startup_notify
    # try:
    #     db.create_table_racers()
    # except Exception as e:
    #     print('err')
    # db.delete_racers()
    # print(db.select_all_racers())

    await on_startup_notify(dp)
    await set_default_commands(dp)




if __name__ == '__main__':
    from aiogram import executor
    from handlers import dp

    executor.start_polling(dp, on_startup=on_startup)
