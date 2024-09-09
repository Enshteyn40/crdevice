from telethon.sync import TelegramClient
from telethon.sessions import StringSession
import csv, os, sys
from telethon.tl.functions.messages import ImportChatInviteRequest, SendMessageRequest
from telethon import types, utils, errors
import random
from telethon.tl.functions.channels import LeaveChannelRequest
import time, requests
with open('phone.csv', 'r') as f:
    global phlist
    phlist = [row[0] for row in csv.reader(f)]
print('\n\n\n\033[93m\nJami: ' + str(len(phlist)) + " ta Raqamlar mavjud\033[0m\n\n\n")
