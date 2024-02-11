from pyrogram import Client, filters, enums
from pyrogram.errors import UserNotParticipant
from pyrogram.types import InputMediaPhoto, InputMediaDocument, InputMediaVideo, InputMediaAnimation, InputMediaAudio
from config import Config
from pyromod.exceptions.listener_timeout import ListenerTimeout

PACK = filters.animation | filters.document | filters.video | filters.audio | filters.photo

@Client.on_message(PACK & filters.private)
async def media(client, message):
    if message.chat.id not in Config.AUTH_USERS:
        return
    if message.photo:
        file_id = message.photo.file_id
        mid = InputMediaPhoto(file_id, caption=message.caption and message.caption.html)

    elif message.document:
        file_id = message.document.file_id
        mid = InputMediaDocument(file_id, caption=message.caption and message.caption.html)

    elif message.video:
        file_id = message.video.file_id
        mid = InputMediaVideo(file_id, caption=message.caption and message.caption.html)

    elif message.animation:
        file_id = message.animation.file_id
        mid = InputMediaAnimation(file_id, caption=message.caption and message.caption.html)

    elif message.audio:
        file_id = message.audio.file_id
        mid = InputMediaAudio(file_id, caption=message.caption and message.caption.html)
    else:
      return
      
    try:
        a = await client.ask(message.chat.id, 'Now send me the link of the message of the channel that you need to edit.\nTimeout: 60s',
                             filters=filters.text, timeout=60)

    except ListenerTimeout:
        await message.reply_text("*__Session Timed Out. Resend the file to Start again__!",
            quote=True
        )
        return
    link = a.text
    a = "-100"
    try:
        id = link.split('/')[4]
        msg_id = link.split('/')[5]
        cd = a + str(id)
        chid = int(cd)

    except:
        chid = link.split('/')[3]
        msg_id = link.split('/')[4]
    try:
        is_admin = await client.get_chat_member(chat_id=chid, user_id=message.from_user.id)
    except UserNotParticipant:
        await message.reply("It seems you are not a member of this channel and hence you can't do this action.")
        return

    if (
                is_admin.status != enums.ChatMemberStatus.ADMINISTRATOR
                and is_admin.status != enums.ChatMemberStatus.OWNER
        ):
        await message.reply_text("**You don't have enough permissions to edit messages in this channel.**")
        return

    try:
        await client.edit_message_media(
            chat_id=chid,
            message_id=int(msg_id),
            media=mid
        )
    except Exception as e:
        await message.reply_text(e)
        return
    await message.reply_text("**Successfully edited the media in channel.**",
                             quote=True)
