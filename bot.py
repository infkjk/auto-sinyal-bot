import requests
from datetime import datetime

# Link CSV Sheet (sinyal otomatis)
sheet_url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTV76H_sWxGmeI9OSD5fh9_oaZ7nhhn5rfh7boZb7txvlz9VIk-jt52nUo0Skg_NYk9Pq6g97pMzXh6/pub?output=csv"

# Link Webhook Google Apps Script (untuk push sinyal otomatis)
webhook_url = "https://script.google.com/macros/s/AKfycbyzBF0Iy6cq4gtnIMvLj8EQoW7P5yYs67PRVfin5rC3dOp_C_EO1isyXJind-i3OF1t/exec"

def push_sinyal(pair, arah, entry, sl, tp):
    params = {
        "pair": pair,
        "arah": arah,
        "entry": entry,
        "sl": sl,
        "tp": tp,
        "status": "PENDING"
    }
    try:
        r = requests.get(webhook_url, params=params)
        if r.status_code == 200:
            print("✅ Sinyal dikirim:", params)
        else:
            print("❌ Gagal kirim sinyal:", r.status_code)
    except Exception as e:
        print("❌ Error:", str(e))

if __name__ == "__main__":
    now = datetime.now()
    jam = now.hour
    if 6 <= jam <= 17:
        # Contoh sinyal dummy (akan diganti otomatis nanti oleh sistem)
        push_sinyal("XAUUSD", "BUY", 2325.0, 2319.0, 2335.0)
    else:
        print("⏳ Di luar jam operasional (06:00–17:00)")
