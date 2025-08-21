import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

BOT_TOKEN = os.getenv("BOT_TOKEN")
if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN environment variable নেই!")

# Start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Option 1", callback_data="opt1")],
        [InlineKeyboardButton("Option 2", callback_data="opt2")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "হ্যালো! Menu থেকে Option বেছে নিন:",
        reply_markup=reply_markup
    )

# Callback query handler
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    if query.data == "opt1":
        await query.edit_message_text(text="আপনি Option 1 বেছে নিয়েছেন।")
    elif query.data == "opt2":
        await query.edit_message_text(text="আপনি Option 2 বেছে নিয়েছেন।")

def get_application():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))
    return app
