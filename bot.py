from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import os


TOKEN = os.getenv("BOT_TOKEN")
if not TOKEN:
raise ValueError("BOT_TOKEN environment variable নেই!")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
webapp_url = "https://your-webapp-url.onrender.com"
await update.message.reply_text(
f"Welcome! Open Web App here: {webapp_url}"
)


def get_application():
app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
return app
