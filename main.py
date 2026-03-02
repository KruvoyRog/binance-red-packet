import re, asyncio, os
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from binance.spot import Spot as Client

# ДАННЫЕ TELEGRAM
API_ID = 37883264
API_HASH = 'c223d91aa4f91dcf19f98b6378e9f984'
SESSION = '1ApWapzMBuy3E6ryoQ6H3kS9UeR2w8f7_6v6wT6O2T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6='

# ДАННЫЕ BINANCE (ВСТАВИЛ ТВОИ НОВЫЕ КЛЮЧИ)
BINANCE_API_KEY = 'mEKN6ScC8u4b315F5QGNKLGqeJ2snSYvepAo536rMlmOrggeM8JRnmGPNgfEMEYK'
BINANCE_SECRET_KEY = 'mysKnKgFN5KhRxun5y5AOPEnrQwPy2cB0nvj64zmT7Z950bKW9YukLiCspDrwJg'

CHANNELS = ['@Binance_Crypto_Box_Codes_New', '@crypto_box_daily', '@binance_box_codes']

# Подключаемся к Binance
binance_client = Client(BINANCE_API_KEY, BINANCE_SECRET_KEY)

# Исправление сессии
clean_session = SESSION.strip()
while len(clean_session) % 4 != 0: clean_session += '='
client = TelegramClient(StringSession(clean_session), API_ID, API_HASH)

@client.on(events.NewMessage(chats=CHANNELS))
async def my_event_handler(event):
    text = event.raw_text
    # Ищем коды из 8 символов (заглавные буквы и цифры)
    codes = re.findall(r'\b[A-Z0-9]{8}\b', text)
    for code in codes:
        print(f"🚀 Пойман код: {code}. Пробую активировать в Binance...")
        try:
            # Попытка активации через API (метод для Gift Card / Red Packet)
            result = binance_client.gift_card_redeem_code(code)
            print(f"✅ УСПЕХ! Ответ Binance: {result}")
        except Exception as e:
            # Если код уже занят или ошибка API
            print(f"❌ Ошибка для {code}: {e}")

async def main():
    print("🤖 Бот-автомат запущен! Мониторим каналы...")
    await client.start()
    await client.run_until_disconnected()

if __name__ == '__main__':
    # Запуск фейк-сервера для Render (чтобы статус был Live)
    import subprocess
    port = os.environ.get("PORT", "10000")
    subprocess.Popen(["python", "-m", "http.server", port])
    asyncio.run(main())
    
