from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("চ্যানেল", url="https://t.me/EducationalCourse")],
        [InlineKeyboardButton(
            "প্রস্তুতকারী", url="https://t.me/SimplifiedExtremist")]
    ])
    welcomed = f"হাই! <b>{message.from_user.first_name}</b>\n/help কমান্ড দিয়ে বিস্তারিত জেনে নিন 😊 "
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
