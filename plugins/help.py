from pyrogram import Client, Filters


@Client.on_message(Filters.command(["help"]))
async def start(client, message):
    helptxt = f"I'm a Yt-dlp supported bot. Powered by @ZauTe_Km"
    await message.reply_text(helptxt)
