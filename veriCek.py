from dropbox import *
import sys
import datetime
import os
from pygame import mixer
"""
app_key = 'kqchkl1olkzsxec'
app_secret = 'lrxsqe4c04od5uo'

flow = dropbox.client.DropboxOAuth2FlowNoRedirect(app_key, app_secret)
"""
now = datetime.datetime.now()

print("Şu an: ")
print(str(now))
print("\n without ms: ")
print(now.strftime("%Y-%m-%d %H:%M"))

xd = os.path.splitext("/musics/(caz)BOB  ACRI - Sleep Away.mp3")[0]
print(xd)

mixer.init()
mixer.music.load('/home/pi/LookPlayIoTProject/musics/(pop)Aleyna Tilki - Sen Olsan Bari.mp3')
mixer.music.play()
