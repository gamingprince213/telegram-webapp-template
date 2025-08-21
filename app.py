from fastapi import FastAPI, Request
import uvicorn
from bot import get_application
import os
import asyncio
import random


app = FastAPI()
bot_app = get_application()


jokes = [
"কেন কম্পিউটার গরম হয়ে যায়? কারণ তার fans আছে! 😄",
"কীভাবে প্রোগ্রামার বন্ধুদের হাসায়? debug করে! 😎",
"Python প্রোগ্রামার সবসময় chilled থাকে। 🐍"
]


@app.get("/")
def root():
return {"status": "Web App is running!"}


@app.post("/data")
async def receive_data(request: Request):
data = await request.json()
msg_type = data.get("type")
if msg_type == "echo":
reply = data.get("message", "")
elif msg_type == "joke":
reply = random.choice(jokes)
elif msg_type == "greet":
reply = "Hello! 🤗 Welcome to our Web App Bot!"
else:
reply = "Unknown action"


print("Web App sent:", data)
return {"status": "OK", "reply": reply}


if __name__ == "__main__":
loop = asyncio.get_event_loop()
loop.create_task(bot_app.run_polling())
uvicorn.run(app, host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
