from fastapi import FastAPI, Request
import uvicorn
from bot import get_application, bot
import os
import asyncio
import nest_asyncio

app = FastAPI()
application = get_application()

BOT_TOKEN = os.getenv("BOT_TOKEN")
if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN environment variable নেই!")

WEBHOOK_PATH = f"/webhook/{BOT_TOKEN}"
APP_URL = "https://telegram-webapp-template.onrender.com"
WEBHOOK_URL = f"{APP_URL}{WEBHOOK_PATH}"

# POST endpoint for Telegram
@app.post(WEBHOOK_PATH)
async def telegram_webhook(req: Request):
    data = await req.json()
    from telegram import Update
    update = Update.de_json(data, bot)
    await application.update_queue.put(update)
    return {"status": "ok"}

# GET endpoint for testing in browser
@app.get(WEBHOOK_PATH)
def webhook_test():
    return {"status": "Webhook endpoint is alive!"}

@app.get("/")
def root():
    return {"status": "Web App is running!"}

if __name__ == "__main__":
    async def main():
        # Set webhook automatically on startup
        await bot.set_webhook(WEBHOOK_URL)
        print(f"Webhook automatically set to {WEBHOOK_URL}")

        nest_asyncio.apply()
        uvicorn.run(app, host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))

    asyncio.run(main())
