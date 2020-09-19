
#!/usr/bin/env python3

import telegram
from time import sleep
import glob
import os

TOKEN_FILE = "./TOKEN"
CHATS_FILE = "./CHATS"
MSG_DIR = "./msg"

with open(TOKEN_FILE, "r") as file:
    TOKEN = file.readline()

with open(CHATS_FILE, "r") as file:
    CHATS = file.readlines()
    CHATS = [x.strip() for x in CHATS]

def update(bot):
    for fname in glob.iglob(MSG_DIR + "/*"):

        with open(fname, "r") as f:
            content = f.read()

        msg = fname.split("/")[-1]

        print("Sending:", msg, "Content:", content)
        send(bot, msg + "\n------------------\n" + content)
        os.remove(fname)

def main():
    print("Starting")

    bot = telegram.Bot(TOKEN)

    while True:
        update(bot)
        sleep(30)


def send(bot, msg):
    for chat in CHATS:
        bot.sendMessage(chat, msg)

if __name__ == "__main__":
    main()
