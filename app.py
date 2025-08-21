import asyncio
from fastapi import FastAPI, Request
from bot import get_application, BOT_TOKEN
import nest_asyncio
import uvicorn

app = FastAPI()
application = get_application()

WEBHOOK_PATH = f"/webhook/{BOT_TOKEN}"
APP_URL = "https://telegram-webapp-template.onrender.com"
WEBHOOK_URL = f"{APP_URL}{WEBHOOK_PATH}"

# Start background task to process updates
@app.on_event("startup")
async def startup_event():
    asyncio.create_task(application.start())  # ✅ queue process চালু হচ্ছে
    await application.bot.set_webhook(WEBHOOK_URL)
    print(f"Webhook set to {WEBHOOK_URL}")

@app.post(WEBHOOK_PATH)
async def telegram_webhook(req: Request):
    data = await req.json()
    from telegram import Update
    update = Update.de_json(data, application.bot)
    await application.update_queue.put(update)
    return {"status": "ok"}

@app.get("/")
def root():
    return {"status": "Web App is running!"}
