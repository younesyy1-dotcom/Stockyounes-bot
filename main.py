import time
import requests
import pandas as pd
import yfinance as yf

TOKEN = "8994385721:AAgbv_F-28ygwrf3Yfax_aoban2hJhREDb4"
CHAT_ID = "8931160328"

def send_telegram_alert(message_text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": message_text, "parse_mode": "Markdown"}
    try:
        requests.post(url, data=payload)
    except Exception as e:
        print(e)

stocks_watchlist = ['1120.SR']

def check_market():
    for symbol in stocks_watchlist:
        try:
            data = yf.download(symbol, period="5d", interval="1d", progress=False)
            if not data.empty:
                pass
        except Exception as e:
            print(e)

if __name__ == "__main__":
    send_telegram_alert("🚀 تم تفعيل بوت فحص الانفجار السعودي بنجاح على السحابة...")
    while True:
        check_market()
        time.sleep(300)
