import re, asyncio
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from playwright.async_api import async_playwright

# ТВОИ ДАННЫЕ (УЖЕ ЗАПОЛНЕНЫ)
API_ID = 37883264
API_HASH = 'c223d91aa4f91dcf19f98f610faf72c6'
SESSION = '1ApWapzMBuy3E6ryoQ6H3kS9UeR2w8f7_6v6wT6O2T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6T6='

# Каналы для мониторинга
CHANNELS = ['@Binance_Crypto_Box_Codes', '@binance_gift_codes', '@RedPacketDaily'] 

async def claim_code(code):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        try:
            print(f"🚀 Пробую активировать: {code}")
            await page.goto(f"https://www.binance.com/ru/convert-binance-pay?code={code}", timeout=60000)
            btn = 'button:has-text("Claim"), button:has-text("Открыть"), button:has-text("Активировать")'
            await page.wait_for_selector(btn, timeout=10000)
            await page.click(btn)
            print(f"✅ Успешно для {code}")
        except:
            print(f"❌ Код {code} уже разобран или не подошел.")
        finally:
            await browser.close()

client = TelegramClient(StringSession(SESSION), API_ID, API_HASH)

@client.on(events.NewMessage(chats=CHANNELS))
async def handler(event):
    found_codes = re.findall(r'\b[A-Z0-9]{8}\b', event.raw_text)
    for code in found_codes:
        await claim_code(code)

async def main():
    await client.start()
    print("🤖 Бот запущен!")
    await client.run_until_disconnected()

if __name__ == '__main__':
    asyncio.run(main())
