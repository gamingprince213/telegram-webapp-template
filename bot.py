from telegram import Update, Bot
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters
import os

TOKEN = os.getenv("BOT_TOKEN")
if not TOKEN:
    raise ValueError("BOT_TOKEN environment variable নেই!")

bot = Bot(TOKEN)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    webapp_url = "https://your-webapp-url.onrender.com"
    await update.message.reply_text(f"Welcome! Open Web App here: {webapp_url}")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"You said: {update.message.text}")

def get_application():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    return app
