from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes
import os

TOKEN = os.getenv("BOT_TOKEN")

VIDEOS = {
    "v1": ("دست گرفتن خودکار", "BAACAgQAAxkBAAMSahxutM9RQ_kOO7fezboYddDtGYwAAgQHAAJ19glTMTudwx6OHf07BA"),
    "v2": ("ضخامت و ظرافت به روش فشار دست", "BAACAgQAAxkBAAMTahxutIAjYN4mqwABQbTnAmJriUJOAAIlBwACGX6AU21l02LpcMTROwQ"),
    "v3": ("تناسبات در خوشنویسی با خودکار", "BAACAgQAAxkBAAMUahxutKvhvqKkveHZ69LOPGNz80sAAk0HAAJ19hFThdLmrHMNP7Y7BA"),
    "v4": ("سطر نویسی و دو سطر نویسی", "BAACAgQAAxkBAAMVahxutCUEUL_k0JBQx0PLc8LMa3AAAngJAAI6bSBTGseQlHtawfA7BA"),
    "v5": ("توضیحات کتابت نثر", "BAACAgQAAxkBAAMWahxutORAEv7DtzFzzYgY52p7Ch4AAnwJAAI6bSBTsaMThhiutak7BA"),
    "v6": ("توضیحات کتابت نظم", "BAACAgQAAxkBAAMXahxutCXKvslfi-0std0o3TauNtoAAn4JAAI6bSBT5tW4FXQvIno7BA"),
    "v7": ("توضیحات کتابت نثر و نظم", "BAACAgQAAxkBAAMYahxutGklt5fQXu2lgscJ2cJ9Qb4AAoAJAAI6bSBT81y7mGga_cc7BA"),
}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = []

    for key, (title, _) in VIDEOS.items():
        keyboard.append([InlineKeyboardButton(title, callback_data=key)])

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "📚 لطفاً ویدئوی مورد نظر را انتخاب کنید:",
        reply_markup=reply_markup,
    )

async def send_video(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    title, file_id = VIDEOS[query.data]

    await query.message.reply_video(
        video=file_id,
        caption=title,
    )
async def myid(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        f"Your ID: {update.effective_user.id}"
    )
app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(send_video))
app.add_handler(CommandHandler("myid", myid))
app.run_polling()
