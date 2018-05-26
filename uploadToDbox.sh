#!/bin/bash

### dosya initial time
### LTIME/ATIME farki ile dosya upload eder

LTIME=`stat -c %Z /home/pi/LookPlayIoTProject/userInfoForCloud.txt`

#naming for filename
fileDefaultName="droptest"
a=0

while true    
do
   ATIME=`stat -c %Z /home/pi/LookPlayIoTProject/userInfoForCloud.txt`

   if [[ "$ATIME" != "$LTIME" ]]
   then
       ((a++))	    	
       echo "cloud uploading... " 
       python cloud_dropbox.py userInfoForCloud.txt /$fileDefaultName$a.txt
       echo "cloud uploaded"	
       LTIME=$ATIME
   fi
   sleep 5
done