import os
import requests
import pandas as pd
from telegram import Bot, ParseMode
from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime

# === ENV Variables ===
BOT_TOKEN = os.getenv("BOT_TOKEN", "7481875754:AAFVurIEOgcftMw6H-xgp58lzCUPf28AR2g")
CHAT_ID = os.getenv("CHAT_ID", "5964132878")

bot = Bot(token=BOT_TOKEN)

# === Core Function ===
def send_sentiment_report():
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    message = f"*📊 NSE Sentiment Report*\n`{now}`\n\n"
    message += "🔹 Retail: Bullish\n🔸 FII: Bearish\n🔹 PRO: Neutral\n"
    message += "_Monitor support and resistance carefully._"

    bot.send_message(chat_id=CHAT_ID, text=message, parse_mode=ParseMode.MARKDOWN)

# === Scheduler ===
scheduler = BlockingScheduler()
scheduler.add_job(send_sentiment_report, trigger="interval", minutes=10)

# === Start ===
if __name__ == "__main__":
    print(">>> Starting script...")
    print(f">>> BOT_TOKEN: {BOT_TOKEN}")
    print(f">>> CHAT_ID: {CHAT_ID}")
    send_sentiment_report()  # optional initial run
    scheduler.start()
