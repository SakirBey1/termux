from telethon.sync import TelegramClient
from telethon import functions, types
from colorama import init, Fore
import os
import sys
import time
import random
from datetime import datetime
from os import execl
import asyncio
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.tl.functions.account import UpdateProfileRequest
#from Config import STRING, SUDO, BIO_MESSAGE, API_ID, API_HASH, STRING2, STRING3, STRING4 ,STRING5, STRING6, STRING7, STRING8 ,STRING9, STRING10, STRING11
from telethon.tl.types import InputPhoto, MessageMediaPhoto
from telethon.tl.functions.photos import UploadProfilePhotoRequest
import telethon.utils
from telethon.tl import functions
import html
import os
from telethon.tl.functions.photos import GetUserPhotosRequest
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import MessageEntityMentionName
from telethon.utils import get_input_location
from telethon.tl import functions
from telethon.tl.functions.channels import JoinChannelRequest, LeaveChannelRequest
from telethon.tl.functions.messages import ImportChatInviteRequest
from telethon.tl.types import InputPhoto, MessageMediaPhoto, User, Chat, Channel
from colorama import Fore, Back, Style, init

API_ID = 1761415
API_HASH = "e989d7ca9dfbfe3da8ffb39e283dd9ce"

aaa = API_ID
bbb = API_HASH

alfa = 5432155018

msj = ["Nerdesin ki 🥺", 
       "Sende gel eksik kalmayalım 👉👈❣️",
       "Rica etsem aktif olur musunn?🥰",
       "Baksana canımın içi"]


aq = random.choice(msj)

with TelegramClient('+15129754386', aaa, bbb) as client:
    alf = 0
    for i in client.iter_participants("KadimTayfa"):
        if alf == 5000:
            break
        alf += 1
        client.send_message("KadimTayfa", "[{}](tg://user?id={}) {}".format(i.first_name, i.id, aq))
        time.sleep(1.9)

