import re, asyncio, os, threading
from http.server import HTTPServer, BaseHTTPRequestHandler
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from binance.spot import Spot as Client

API_ID = 37883264
API_HASH = 'c223d91aa4f91dcf19f98b6378e9f984'
SESSION = '1ApWapzMBuy3E6ryoQ6H3H9pGq_Hq-fR8T3M_vS0iY_MIn5V6p_7Y0U_YpX1p8pX_YpX1p8pX_YpX1p8pX_YpX1p8pX_YpX1p8pX_YpX1p8pX_YpX1p8pX_YpX1p8pX_YpX1p8pX_YpX1p8pX_YpX1p8pX_YpX1p8pX_YpX1p8pX_YpX1p8pX_YpX1p8pX_Y'
BINANCE_KEY = 'abfnxgygeeYDtkaZEgjJNbtbo50gz1CHoeuoHQpbADxkxvHXAPMFFWXrZXybQ702'
BINANCE_SECRET = 'zESBDriAJhUNGRzigALE6wMV1tEfPcbmWlJH7jkigF5ydB7o0AAeOa0w9J92Jo7g'
CHANNELS = ['@Binance_Crypto_Box_Codes_New', 'crypto_box_daily', 'binance_box_codes']

b_client = Client(BINANCE_KEY, BINANCE_SECRET)
t_client = TelegramClient(StringSession(SESSION), API_ID, API_HASH)

class HealthCheck(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"OK")

def run_web():
    port = int(os.environ.get("PORT", 10000))
    HTTPServer(('0.0.0.0', port), HealthCheck).serve_forever()

@t_client.on(events.NewMessage(chats=CHANNELS))
async def handler(event):
    codes = re.findall(r'\b[A-Z0-9](8)\b', event.raw_text)
    for code in codes:
        try:
            res = b_client.crypto_box_redeem(code)
            print(f"SUCCESS: (code) - (res)")
        except Exception as e)
            print(f"FAIL: (code) - (e)")

async def start():
    await t_client.start()
    await t_client.run_until_disconnected()

if __name__ == '__main__':
    threading.Thread(target=run_web, daemon=True).start()
    asyncio.run(start())
