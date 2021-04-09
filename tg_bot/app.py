import os
import sys

import django

from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands

# sys.path.append(r'/home/g/python/AlleyCat-bot/')
from web.core import settings
# print(settings.ALLOWED_HOSTS)


def create_sys_path():
    """ Удаляем tg-bot из /home/g/python/AlleyCat-bot/tg-bot. """

    print(sys.path[0])
    path = sys.path[0]
    path_length = len(sys.path[0])
    new_path = path[:path_length - len('tg_bot')]
    return sys.path.append(new_path)


async def on_startup(dp):
    # try:
    #     await db.create_table_racers()
    # except:
    #     pass

    await on_startup_notify(dp)
    await set_default_commands(dp)


def setup_django():
    os.environ.setdefault(
        'DJANGO_SETTINGS_MODULE',
        'web.core.settings'
    )
    os.environ.update({'DJANGO_ALLOW_ASYNC_UNSAFE': 'True'})
    django.setup()


if __name__ == '__main__':
    create_sys_path()
    setup_django()
    from aiogram import executor
    from handlers import dp

    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)
    print('ok')
