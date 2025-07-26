import pandas as pd
import requests
import logging
from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime
import pytz
from telegram import Bot

# === CONFIG ===
BOT_TOKEN = '7481875754:AAFVurIEOgcftMw6H-xgp58lzCUPf28AR2g'
CHAT_ID = '5964132878'

# === LOGGER ===
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# === TELEGRAM BOT ===
bot = Bot(token=BOT_TOKEN)

# === FUNCTION TO SEND REPORT ===
def send_sentiment_report():
    try:
        message = "*📊 Daily Sentiment Update - NSE Options Participants*\n\n"

        # Simulated example (you will replace this with file read or API data)
        message += "👥 *Retail*: Bullish\n"
        message += "🏢 *FII*: Bearish\n"
        message += "💼 *PRO*: Neutral\n"
        message += "\n🔄 Auto-updated every 10 minutes."

        bot.send_message(chat_id=CHAT_ID, text=message, parse_mode='Markdown')
        logging.info("✅ Sentiment report sent.")
    except Exception as e:
        logging.error(f"❌ Failed to send sentiment report: {e}")

# === SCHEDULER ===
if __name__ == "__main__":
    logging.info("🚀 Starting script...")

    # Use India timezone
    ist = pytz.timezone("Asia/Kolkata")

    scheduler = BlockingScheduler(timezone=ist)
    scheduler.add_job(send_sentiment_report, trigger="interval", minutes=10)

    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        logging.info("🛑 Script stopped manually.")
