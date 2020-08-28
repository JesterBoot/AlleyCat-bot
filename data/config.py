import os

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = '1147769031:AAEvnrrHXuBwAaO71nE3LO4ojSKpAGFIuqA'
PGUSER='postgres'
PGPASSWORD='Pipiski987'
ip = os.getenv("ip")

'''id: Мой, Олега'''
admins = [412112889,
          139148302,]



# BOT_TOKEN = str(os.getenv("BOT_TOKEN"))
# PGUSER = str(os.getenv("PGUSER"))
# PGPASSWORD = str(os.getenv("PGPASSWORD"))
# DATABASE = str(os.getenv("DATABASE"))


# aiogram_redis = {
#     'host': ip,
# }
#
# redis = {
#     'address': (ip, 6379),
#     'encoding': 'utf8'
# }
#
# POSTGRES_URI = f"postgresql://{PGUSER}:{PGPASSWORD}@{ip}/{DATABASE}"
