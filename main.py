import logging
import sys

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
print(">>> Starting script...")

import os
import pandas as pd
import requests
from datetime import datetime, timedelta
import telegram

try:
    # Setup Telegram Bot
    BOT_TOKEN = os.getenv("BOT_TOKEN")
    CHAT_ID = os.getenv("CHAT_ID")

    print(f">>> BOT_TOKEN: {BOT_TOKEN}")
    print(f">>> CHAT_ID: {CHAT_ID}")

    bot = telegram.Bot(token=BOT_TOKEN)

    # Dummy sentiment message
    message = """
📊 *NSE Sentiment Report – {date}*

*Retail*: 🧑‍💼 Neutral  
*FII*: 🐻 Bearish  
*PRO*: 🐂 Bullish

🔥 *Trap Zones (OI based)*:  
• Put OI Max: 23500 🟢 (Support)  
• Call OI Max: 23800 🔴 (Resistance)  
⚠️ IV Spike > 10% at 23800

Stay alert! Institutions may trap near zones.
""".format(date=datetime.now().strftime('%d-%b-%Y'))

    bot.send_message(chat_id=CHAT_ID, text=message, parse_mode=telegram.constants.ParseMode.MARKDOWN)

except Exception as e:
    logging.exception("❌ An error occurred:")
