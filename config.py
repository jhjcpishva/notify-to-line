import os
from os.path import join, dirname
from dotenv import load_dotenv


load_dotenv(verbose=True)

dotenv_path = join(dirname(__file__), os.getenv("DOTENV", '.env'))
load_dotenv(dotenv_path)

LINE_CHANNEL_ACCESS_TOKEN = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", "")
LINE_CHANNEL_SECRET = os.getenv("LINE_CHANNEL_SECRET", "")
LINE_USER_ID = os.getenv("LINE_USER_ID", "")
LLMS_HOST = os.getenv("LLMS_HOST", "")
CONFIG_FILE = os.getenv("CONFIG_FILE", "_config.json")

PORT = int(os.getenv("PORT", "8001"))
