from telegram import Updat
from telegram import InlineKeyboardButton, InlinekeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    buttons = [
        [
            InlineKeyboardButton('Toshkent', collback_data='region_1'),
            InlineKeyboardButton('Toshkent', collback_data='region_2')
        ],
    ]
    await update.message.reply_html(
        '😁ASALOMU AELKUM😁 <b> \n{update.effective_user.first_name}</b> \n \n<b>fdffgdgfgfgh</b>', replay_markup=InlinekeyboardMarkup(buttons))


app = ApplicationBuilder().token("5903874788:AAE2e6E_55wN2cuLhX7AojBihSTmPUV8ZH0").build()

app.add_handler(CommandHandler("start", start))

app.run_polling()
