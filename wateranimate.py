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

# Joriy faylning katalogini topamiz
current_dir = os.path.dirname(os.path.abspath(__file__))

# Bitta yuqoridagi katalogni olamiz
parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))

# Yuqoridagi katalogdagi phone.csv fayliga yo'l yaratamiz
csv_file_path = os.path.join(parent_dir, 'phone.csv')

# phone.csv faylining mavjudligini tekshiramiz va faylni o'qiymiz
if os.path.exists(csv_file_path):
    with open(csv_file_path, 'r') as f:
        phlist = [row[0] for row in csv.reader(f)]
        print(f"Topilgan telefonlar soni: {len(phlist)}")
else:
    print("phone.csv fayli topilmadi.")
