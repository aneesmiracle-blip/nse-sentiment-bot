# main.py
# main.py

import logging
import sys

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
print(">>> Starting script...")  # helps Render log show something before error

import os
import pandas as pd
import requests
from datetime import datetime, timedelta
import telegram

import os
import pandas as pd
import requests
from datetime import datetime, timedelta
import telegram

# Setup Telegram Bot
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")
bot = telegram.Bot(token=BOT_TOKEN)

# Dummy sentiment message (replace with actual analysis logic)
message = """
📊 *NSE Sentiment Report – {date}*

🔸 *Retail*: ⚖️ Neutral
🔸 *FII*: 📉 Bearish
🔸 *PRO*: 📈 Bullish

🔥 *Trap Zones (OI based)*:
• Put OI Max: 23500 🟢 (Support)
• Call OI Max: 23800 🔴 (Resistance)
• ⚠️ IV Spike > 10% at 23800

Stay alert! Institutions may trap near zones.
""".format(date=datetime.now().strftime('%d-%b-%Y'))

bot.send_message(chat_id=CHAT_ID, text=message, parse_mode=telegram.ParseMode.MARKDOWN)
