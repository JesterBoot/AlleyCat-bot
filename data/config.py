BOT_TOKEN = '1147769031:AAEvnrrHXuBwAaO71nE3LO4ojSKpAGFIuqA'
PGUSER='postgres'
PGPASSWORD='Pipiski987'
import os

from dotenv import load_dotenv

load_dotenv()

# BOT_TOKEN = str(os.getenv("BOT_TOKEN"))
# PGUSER = str(os.getenv("PGUSER"))
# PGPASSWORD = str(os.getenv("PGPASSWORD"))
# DATABASE = str(os.getenv("DATABASE"))
ip = os.getenv("ip")
admins = [412112889]

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
