from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes



async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_html(f'alalalalallalaa <b>{update.effective_user.first_name}</b> \n \n<b>fdffgdgfgfgh</b> ')


app = ApplicationBuilder().token("5903874788:AAE2e6E_55wN2cuLhX7AojBihSTmPUV8ZH0").build()

app.add_handler(CommandHandler("start", start))

app.run_polling()
