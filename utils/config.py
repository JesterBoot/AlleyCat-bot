import os

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = str(os.getenv('BOT_TOKEN'))
DB_USER = str(os.getenv('PGUSER'))
DB_PASSWORD = str(os.getenv('PGPASSWORD'))
DB_NAME = str(os.getenv('DATABASE_NAME'))
DB_HOST = str(os.getenv('DATABASE_HOST'))

admins = [
    412112889,  # My
    # 139148302,  # Oleg
    # 108554,  # Nikita
]
