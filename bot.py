from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters
import os

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "به ربات رسانه مولانا خوش آمدید.\n\nیک ویدئو برای من ارسال کنید."
    )

async def get_video_id(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.video:
        file_id = update.message.video.file_id

        print("=" * 50)
        print("VIDEO FILE ID:")
        print(file_id)
        print("=" * 50)

        await update.message.reply_text(
            f"Video ID:\n{file_id}"
        )

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.VIDEO, get_video_id))

app.run_polling()
