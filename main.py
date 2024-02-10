import os
from pyromod import listen
from config import Config
from pyrogram import Client

# the logging things
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

DOWNLOAD_LOCATION = "/downloads"

if __name__ == "__main__" :
    
    plugins = dict(
        root="plugins"
    )
    app = Client(
        "Media-Editor-Bot",
        bot_token=Config.BOT_TOKEN,
        api_id=Config.APP_ID,
        api_hash=Config.API_HASH,
        plugins=plugins
    )


    app.run()
