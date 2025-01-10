from pyrogram import Client, filters

# Botni sozlash uchun ma'lumotlar
API_ID = "25627284"          # Telegram API ID
API_HASH = "130ab352ec938aa4d51c0a9637e85b47"
BOT_TOKEN = "7927199641:AAG5VGjqeyDw48XGUprALt92czavueKdT5E"    # BotFather orqali olingan token
CHANNEL_USERNAME = "@avtoBazor_uzb"  # Kanal username'ini kiriting

# Bot mijozini sozlash
app = Client("my_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# Kanal postlariga ishlov berish
@app.on_message(filters.channel & filters.text & filters.chat(CHANNEL_USERNAME))
def add_footer(client, message):
    # Post ostiga matn qo‘shish
    footer = "\n\n𝕂𝕒𝕟𝕒𝕝𝕚𝕞𝕚𝕫𝕘𝕒 𝕆𝕓𝕦𝕟𝕒 𝔹𝕠’𝕝𝕚𝕟𝕘👇\n️\n\n [Instagram](https://instagram.com/inomarkabozor)"  "  |[Telegram](https://t.me/inomarkabozor)" " | [Avtobozor24_7](https://t.me/avtoelon_avtobozor_inomarkabozor)"
    if footer not in message.text:
        new_text = message.text + footer
        client.edit_message_text(
            chat_id=message.chat.id,
            message_id=message.id,
            text=new_text
        )

# Botni ishga tushirish
app.run()
