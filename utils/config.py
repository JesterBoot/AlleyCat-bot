import os

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = str(os.getenv('BOT_TOKEN'))
DB_USER = str(os.getenv('PGUSER'))
DB_PASSWORD = str(os.getenv('PGPASSWORD'))
DB_NAME = str(os.getenv('DATABASE_NAME'))
DB_HOST = str(os.getenv('DATABASE_HOST'))



# ip = os.getenv('ip')
admins = int(os.getenv('ADMINS'))

# aiogram_redis = {
#     'host': ip,
# }
#
# redis = {
#     'address': (ip, 6379),
#     'encoding': 'utf8'
# }

# POSTGRES_URI = f"postgresql://{PGUSER}:{PGPASSWORD}@{ip}/{DATABASE}"
