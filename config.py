import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('TOKEN')
WEATHER_API = os.getenv('WEATHER_API')
PRAYER_API = os.getenv('PRAYER_API')
OPENIA_API = os.getenv('OPENIA_API')
ADMIN_ID = int(os.getenv('ADMIN_ID'))