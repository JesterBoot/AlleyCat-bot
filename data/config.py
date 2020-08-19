import os

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = str(os.getenv("BOT_TOKEN"))
PGUSER='postgres'
PGPASSWORD='Pipiski987'
admins = [412112889]

ip = os.getenv("ip")
