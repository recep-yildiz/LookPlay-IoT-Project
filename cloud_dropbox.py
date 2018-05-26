import dropbox
import sys

args = sys.argv
args_count = len(args)

if(args_count != 3):
    print('Dogru sekilde giriniz: # python %s fileLocal /dropboxFileName' % args[0])
    quit()

f = open(args[1])

#dropbox object
dbx = dropbox.Dropbox('R-D-HxqzEmAAAAAAAAAAKE-aorfW4dTe0P9p6shv2OgESNAHoBjKje3VflmuN87l')

with open("/home/pi/LookPlayIoTProject/userInfoForCloud.txt", "rb") as f:
    dbx.files_upload(f.read(), args[2], mute = True)

#dbx.files_upload(f, '/uploaded.txt')

f.close()
