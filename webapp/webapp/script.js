const tg = window.Telegram.WebApp;


// Echo Feature
document.getElementById("sendMessage").addEventListener("click", async () => {
const msg = document.getElementById("userMessage").value;
if(!msg) return alert("Please type a message!");
const payload = { type: "echo", message: msg };
const res = await fetch("/data", {
method: "POST",
headers: { "Content-Type": "application/json" },
body: JSON.stringify(payload)
});
const result = await res.json();
alert("Bot replied: " + result.reply);
});


// Menu Buttons
document.querySelectorAll(".menuBtn").forEach(btn => {
btn.addEventListener("click", async () => {
const action = btn.dataset.action;
const payload = { type: action };
const res = await fetch("/data", {
method: "POST",
headers: { "Content-Type": "application/json" },
body: JSON.stringify(payload)
});
const result = await res.json();
alert("Bot replied: " + result.reply);
});
});
