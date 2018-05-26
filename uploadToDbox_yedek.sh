#!/bin/bash

### dosya initial time
### LTIME/ATIME farki ile dosya upload eder

LTIME=`stat -c %Z /home/pi/LookPlayIoTProject/userInfoForCloud.txt`

while true    
do
   ATIME=`stat -c %Z /home/pi/LookPlayIoTProject/userInfoForCloud.txt`

   if [[ "$ATIME" != "$LTIME" ]]
   then    	
       echo "cloud uploading... " 
       python cloud_dropbox.py userInfoForCloud.txt /droptest.txt
       echo "cloud uploaded"	
       LTIME=$ATIME
   fi
   sleep 5
done