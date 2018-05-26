import os

#her reboot isleminden sonra picamera'yi aktif eden komut (crontab)
os.system('sudo modprobe bcm2835-v4l2')


