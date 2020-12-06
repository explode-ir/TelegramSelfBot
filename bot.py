'''
--------------------Instructions for use---------------------
1. Create a folder and name it whatever you want
2. Transfer this file to the previously created folder
3. Transfer to the site https://my.telegram.org/ and register there. After registration, go to https://my.telegram.org/apps and create a new application
4. Copy the App api_id item
and App api_hash:
5. In the previously created folder, create a config.ini file
6. Write in it
[pyrogram]
api_id = {your api_id without {}}
api_hash = {your api_hash without {}}
7. Save. Open the .py file in which you are reading this instruction and change the parameters in it to the ones you need. Change the contents of only 1-1 lines and only the one in quotes, save it.
8. First, we must download python. Go to https://www.python.org/downloads/ and click the "Download Python 3.9" button, then you will figure it out
9. Open the command line and write pip install Pyrogram there (to install the module)
10. Run the command line. And enter there python {path to the .py file without {}}
11. Confirm the phone number
12. Enter the sent code
13. aaaaaand we have prayed, my congratulations!
'''
#-----------SETTINGS--------------
STRING_HACK = '👮‍ Your phone is being hacked now ...' #the first message of the command .hack
STRING_HACK_2 = '🤖 The phone was hacked!' #the second message of the command .hack
STRING_HACK_3 = '🤖 A nuclear bomb is launched from your phone ...' #the third message of the command .hack
STRING_HACK_4 = '🤖 Virus software has been successfully installed on your phone!' #fourth command message .hack
SYMBOL = '🌀' #the character to replace in .type
#---------------------------------


from pyrogram import Client, filters
from pyrogram.errors import FloodWait
 
from pyrogram.types import ChatPermissions
 
import time
from time import sleep
import random
 
app = Client("my_account")
 
# Команда type
@app.on_message(filters.command("type", prefixes=".") & filters.me)
def type(_, msg):
    orig_text = msg.text.split(".type ", maxsplit=1)[1]
    text = orig_text
    tbp = "" # to be printed
    typing_symbol = SYMBOL
 
    while(tbp != orig_text):
        try:
            msg.edit(tbp + typing_symbol)
            sleep(0.05) # 50 ms
 
            tbp = tbp + text[0]
            text = text[1:]
 
            msg.edit(tbp)
            sleep(0.05)
 
        except FloodWait as e:
            sleep(e.x)
 
# Команда взлома пентагона
@app.on_message(filters.command("hack", prefixes=".") & filters.me)
def hack(_, msg):
    perc = 0
 
    while(perc < 100):
        try:
            text = STRING_HACK + str(perc) + "%"
            msg.edit(text)
 
            perc += random.randint(1, 3)
            sleep(0.1)
 
        except FloodWait as e:
            sleep(e.x)
 
    msg.edit(STRING_HACK_2)
    sleep(3)
 
    msg.edit(STRING_HACK_3)
    perc = 0
 
    while(perc < 100):
        try:
            text = STRING_HACK_3 + str(perc) + "%"
            msg.edit(text)
 
            perc += random.randint(1, 5)
            sleep(0.15)
 
        except FloodWait as e:
            sleep(e.x)
 
    msg.edit(STRING_HACK_4)
 
@app.on_message(filters.command("thanos", prefixes=".") & filters.me)
def thanos(_, msg):
    chat = msg.text.split(".thanos ", maxsplit=1)[1]
 
    members = [
        x
        for x in app.iter_chat_members(chat)
        if x.status not in ("administrator", "creator")
    ]
 
    random.shuffle(members)
 
    app.send_message(chat, "Щелчок Таноса ... *щёлк*")
 
    for i in range(len(members) // 2):
        try:
            app.restrict_chat_member(
                chat_id=chat,
                user_id=members[i].user.id,
                permissions=ChatPermissions(),
                until_date=int(time.time() + 86400),
            )
            app.send_message(chat, "Исчез " + members[i].user.first_name)
        except FloodWait as e:
            print("> waiting", e.x, "seconds.")
            time.sleep(e.x)
 
    app.send_message(chat, "Но какой ценой?")
 
app.run()