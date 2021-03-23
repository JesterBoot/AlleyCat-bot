import os

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = str(os.getenv('BOT_TOKEN'))
DJANGO_SECRET_KEY = str(os.getenv('DJANGO_SECRET_KEY'))

DATABASE = str(os.getenv('DATABASE_NAME'))
PGUSER = str(os.getenv('PGUSER'))
PGPASSWORD = str(os.getenv('PGPASSWORD'))
ip = os.getenv('ip')

admins = int(os.getenv('ADMINS'))

aiogram_redis = {
    'host': ip,
}

redis = {
    'address': (ip, 6379),
    'encoding': 'utf8'
}

# POSTGRES_URI = f"postgresql://{PGUSER}:{PGPASSWORD}@{ip}/{DATABASE}"