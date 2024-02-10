from pyrogram import filters, Client
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

START_MSG = """**Hi {}, Welcome to Media Editor bot
You can edit/relace the documents,videos,gifs,audios,photos etc… Of Your Channels easily By Using Me

For more info on Uuage hit - /help"""


HELP_MSG = """
**Follow these steps**

1.First send me a media that you need to Edit/Replace with the other one.
2.Send the link of the media that you wanted to be Replaced/Edited with.

**<u>Note</u>:- Note both you & the bot must be an admin in the targert channel.**"""



@Client.on_message(filters.command('start') & filters.private)
async def start(client, message):
    await message.reply_text(
        text=START_MSG.format(message.from_user.mention),
        reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton("Check Repository", url="https://github.com/ANIDIVE/Media-Editor-Bot")]]),
        quote=True
    )    

@Client.on_message(filters.command('help') & filters.private)
async def help(client, message):
    await message.reply_text(text=HELP_MSG)   
