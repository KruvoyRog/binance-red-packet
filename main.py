import re, asyncio
from telethon import TelegramClient, events
from telethon.sessions import StringSession

# ТВОИ ДАННЫЕ
API_ID = 37883264
API_HASH = 'c223d91aa4f91dcf19f98b6378e9f984'
SESSION = '1ApWapzMBuy3E6ryoQ6H3kS9UeR2w8f7_6v6wT6O2T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6='

CHANNELS = ['@Binance_Crypto_Box_Codes_New', '@crypto_box_daily', '@binance_box_codes']

client = TelegramClient(StringSession(SESSION), API_ID, API_HASH)

@client.on(events.NewMessage(chats=CHANNELS))
async def my_event_handler(event):
    text = event.raw_text
    codes = re.findall(r'\b[A-Z0-9]{8}\b', text)
    for code in codes:
        print(f"🚀 Пойман код: {code}")

async def main():
    print("🤖 Бот запущен и ждёт коды в облаке...")
    await client.start()
    await client.run_until_disconnected()

if __name__ == '__main__':
    asyncio.run(main())

