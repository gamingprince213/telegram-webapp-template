from fastapi import FastAPI, Request
import uvicorn
from bot import get_application, bot
import os
import asyncio

app = FastAPI()
application = get_application()

WEBHOOK_PATH = f"/webhook/{os.getenv('BOT_TOKEN')}"
WEBHOOK_URL = f"https://your-render-app.onrender.com{WEBHOOK_PATH}"

# Webhook route
@app.post(WEBHOOK_PATH)
async def telegram_webhook(req: Request):
    data = await req.json()
    update = Update.de_json(data, bot)
    await application.update_queue.put(update)
    return {"status": "ok"}

@app.get("/")
def root():
    return {"status": "Web App is running!"}

if __name__ == "__main__":
    async def main():
        # Set Telegram webhook
        await bot.set_webhook(WEBHOOK_URL)
        # Start FastAPI server
        import nest_asyncio
        nest_asyncio.apply()
        uvicorn.run(app, host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))

    import asyncio
    asyncio.run(main())
