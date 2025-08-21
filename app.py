from contextlib import asynccontextmanager
import asyncio
from fastapi import FastAPI, Request
from bot import get_application, BOT_TOKEN
import uvicorn

application = get_application()
WEBHOOK_PATH = f"/webhook/{BOT_TOKEN}"
APP_URL = "https://telegram-webapp-template.onrender.com"
WEBHOOK_URL = f"{APP_URL}{WEBHOOK_PATH}"

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup code
    await application.bot.set_webhook(WEBHOOK_URL)
    asyncio.create_task(application.start())  # background task চালু
    print(f"Webhook set to {WEBHOOK_URL}")
    yield
    # Shutdown code (optional)
    await application.stop()
    await application.bot.delete_webhook()

app = FastAPI(lifespan=lifespan)

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
