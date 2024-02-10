import os

class Config(object):
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    APP_ID = int(os.environ.get("APP_ID", ""))
    API_HASH = os.environ.get("API_HASH", "")
    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "").split())
