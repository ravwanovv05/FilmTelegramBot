import os
from dotenv import load_dotenv

load_dotenv()

ADMIN_ID = int(os.getenv('ADMIN_ID'))
CHANNEL_ID = int(os.getenv('CHANNEL_ID'))
BOT_TOKEN = os.getenv('BOT_TOKEN')