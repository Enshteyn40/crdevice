from telethon.sync import TelegramClient
from telethon.sessions import StringSession
import csv
import os
import sys
from telethon.tl.functions.messages import ImportChatInviteRequest, SendMessageRequest
from telethon import types, utils, errors
import random
from telethon.tl.functions.channels import LeaveChannelRequest
import time
import requests

# Foydalanuvchidan phone.csv joylashgan katalogga yo'lni so'raymiz
input_path = input("Iltimos, phone.csv joylashgan katalogga to'liq yo'lni kiriting: ")

# Kirtilgan yo'lning mavjudligini tekshiramiz
if not os.path.exists(input_path):
    print(f"Kiritilgan yo'l mavjud emas: {input_path}")
    sys.exit()

# phone.csv fayliga to'liq yo'l yaratamiz
csv_file_path = os.path.join(input_path, 'phone.csv')

# phone.csv faylining mavjudligini tekshiramiz va faylni o'qiymiz
if os.path.exists(csv_file_path):
    with open(csv_file_path, 'r') as f:
        phlist = [row[0] for row in csv.reader(f)]
        print(f"Topilgan telefonlar soni: {len(phlist)}")
else:
    print(f"phone.csv fayli topilmadi kiritilgan yo'lda: {csv_file_path}")
