from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import os

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "به ربات رسانه مولانا خوش آمدید.\n\nویدئوهای آموزشی به زودی اینجا قرار می‌گیرند."
    )

TOKEN = os.getenv("BOT_TOKEN")

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))

app.run_polling()
