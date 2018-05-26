# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
import cv2
import os
import numpy as np
import time
import datetime
from pygame import mixer

#pi kamera aktif
os.system('sudo modprobe bcm2835-v4l2')

#this line should be crontab -> crontab doesn't work on this device(tried all ways)
#os.system('sudo ./uploadToDbox.sh')

#from PyQt4.pyqtconfig import Configuration (4:5)
#print("Qt version:", QT_VERSION_STR)
#Qt version : 5.10.1

#dataset.py degiskenleri
face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#global face_id


#face_recognition degiskenleri
recognizer = cv2.face.createLBPHFaceRecognizer()
recognizer.load('trainer/trainer.yml')
cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath);
font = cv2.FONT_HERSHEY_SIMPLEX

#training.py degiskenleri

class OtherWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.inits()
        
    def inits(self):
        fbox = QFormLayout()
        
        l1 = QLabel("Ad")
        global nm
        nm = QLineEdit()
        fbox.addRow(l1,nm)
            
        l2 = QLabel("Soyad")
        global add1
        add1 = QLineEdit()
        fbox.addRow(l2, add1)
            
        l3 = QLabel("ID")
        global user_no
        user_no = QLineEdit()
        fbox.addRow(l3, user_no)
            
        l4 = QLabel("Müzik Türü")
        vbox = QVBoxLayout()
            
        global cb
        cb = QComboBox()
        cb.addItems(["Türk Halk Müziği", "Pop", "Caz", "Rap", "Country"])
        fbox.addRow(l4, cb)
        vbox.addWidget(cb)

        vbox.addWidget(add1)

        blank = QLabel("")
        fbox.addRow(blank)

        yuz_tanila_btn = QPushButton('Yüzü Tanımla', self)
        yuz_tanila_btn.setGeometry(50, 50, 120, 30)
        yuz_tanila_btn.clicked.connect(self.detectFace)
        fbox.addRow(yuz_tanila_btn)
        
        onayla_btn = QPushButton('Onayla', self)
        onayla_btn.clicked.connect(self.onaylaMethod)
        
        iptal_btn = QPushButton('Çıkış',self)
        iptal_btn.clicked.connect(self.iptalMethod)
        
        fbox.addRow(onayla_btn, iptal_btn)

        self.widget = QWidget()
        self.widget.setLayout(fbox)
        self.setCentralWidget(self.widget)
            
        self.setWindowTitle("Kullanıcı Ekle")
        self.setGeometry(300, 150, 350, 300)

    def detectFace(self):

        #text dosyasi satir sayisi (initial:0)
        num_lines = sum(1 for line in open('userInfoForCloud.txt'))
        face_id = num_lines + 1
        cap = cv2.VideoCapture(0)
        count = 0
        while(True):
            # Capture frame-by-frame
            ret, frame = cap.read()

            # Our operations on the frame come here
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            faces = face_detector.detectMultiScale(gray, 1.3, 5)

            for (x,y,w,h) in faces:

                # Crop the image frame into rectangle
                cv2.rectangle(frame, (x,y), (x+w,y+h), (255,0,0), 2)
                
                # Increment sample face image
                count += 1

                # Save the captured image into the datasets folder
                cv2.imwrite("dataset/User." + str(face_id) + '.' + str(count) + ".jpg", gray[y:y+h,x:x+w])


            cv2.imshow('frame', frame)
            # Display the resulting frame
            if cv2.waitKey(100) & 0xFF == ord('q'):
                break

            elif count>50:
                break
        cap.release()
        cv2.destroyAllWindows()
            
    #Onayla -> textFile olustur -> upload to cloud
    def onaylaMethod(self):
        user_name = nm.text()
        user_sName = add1.text()
        user_id = user_no.text()
        user_music_type = cb.currentText()
        sign_up_date = datetime.datetime.now() 

        # write permission : append(a) -> dosyanin ustune yazar
        cloud_content = user_name + "\t\t" + user_sName + "\t\t" + user_id + "\t\t" + user_music_type + "\t\t" + sign_up_date.strftime("%Y-%m-%d %H:%M") + "\n"
        cloudFile = open("userInfoForCloud.txt", "a")
        cloudFile.write(cloud_content)
        
        reply = QMessageBox.question(self, 'Message', "Kayıt Eklendi", QMessageBox.Ok)

        """ -> bu blok crontab haline gelecek -> update every 1min
        time.sleep(1)
        #upload to dbox
        os.system('python cloud_dropbox.py userInfoForCloud.txt /droptest.txt')
        """
        
    def iptalMethod(self):
        reply = QMessageBox.question(self, 'Message', "gibi gibi", QMessageBox.Ok)

class mainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.initUI()

    def initUI(self):

        kayitolustur_b = QPushButton('Kayıt Olustur', self)
        kayitolustur_b.setGeometry(50, 50, 120, 30)
        kayitolustur_b.setStyleSheet("QPushButton {  position: absolute; width:8%; top: 40%; left: 50%; background-color: #ffcccc; border-radius: 10px; border: 1px solid black;}")
        kayitolustur_b.clicked.connect(self.newWindow) #button act

        kayitlar_b = QPushButton('Yuz Algıla', self)
        kayitlar_b.setGeometry(50, 90, 120, 30)
        kayitlar_b.setStyleSheet("QPushButton { position: absolute; width : 8%; top: 40%; left: 50%; height:auto; background-color: #ffcccc; border-radius: 10px; border: 1px solid black;}")

        kayitsil_b = QPushButton('Yuz Tanımla', self)
        kayitsil_b.setGeometry(50, 130, 120, 30)
        kayitsil_b.setStyleSheet("QPushButton { position: absolute; width : 8%; top: 40%; left: 50%; height:auto; background-color: #ffcccc; border-radius: 10px; border: 1px solid black;}")

        calmalistesi_b = QPushButton('Egit', self)
        calmalistesi_b.setGeometry(50, 210, 120, 30)
        calmalistesi_b.setStyleSheet("QPushButton { position: absolute; width : 8%; top: 40%; left: 50%; height:auto; background-color: #ffcccc; border-radius: 10px; border: 1px solid black;}")

        kayitolustur_b.clicked.connect(self.kayitolusturBtn)
        kayitlar_b.clicked.connect(self.kayitlarBtn)
        kayitsil_b.clicked.connect(self.kayitsilBtn)
        calmalistesi_b.clicked.connect(self.calmalistesiBtn)


        self.square = QFrame(self)
        self.square.setGeometry(200, 50, 535, 350)
        self.square.setStyleSheet("QFrame {  background-image: url('logo.jpeg'); position: absolute; width: 20%; height:auto; border: 1px solid black; }")

        self.setGeometry(500, 350, 750, 500)
        self.setWindowTitle('LookPlay')
        self.setWindowIcon(QIcon('logo.jpeg'))
        self.setStyleSheet("QWidget { position: absolute; width: 100%; height:auto; background-color: #ccccff}")

        self.show()

    #button method
    def newWindow(self):
        self.yeni = OtherWindow()
        self.yeni.show()

    def kayitolusturBtn(self):

        """reply = QMessageBox.question(self, 'Message', "LookPlay sizi görecek, yüzünüzü sabit tutun. Arada bir çok hafif sağa sola bakın.", QMessageBox.Ok)
        """
    def kayitlarBtn(self):

        #reply = QMessageBox.question(self, 'Message', "LookPlay sizi görecek, yüzünüzü sabit tutun. Arada bir çok hafif sağa sola bakın.", QMessageBox.Ok)
        cam = cv2.VideoCapture(0)
        while True:
            # Read the video frame
            ret, im =cam.read()

            # Convert the captured frame into grayscale
            gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)

            # Get all face from the video frame
            faces = faceCascade.detectMultiScale(gray, 1.2,5)

            # For each face in faces
            for(x,y,w,h) in faces:

                # Create rectangle around the face
                cv2.rectangle(im, (x-20,y-20), (x+w+20,y+h+20), (0,255,0), 4)

                # Recognize the face belongs to which ID
                Id,conf = recognizer.predict(gray[y:y+h,x:x+w])

                # Check the ID if exist 
                if(Id == 4):
                    Id = "Yusuf"
                    path_name = os.path.splitext("/musics/(caz)BOB  ACRI - Sleep Away.mp3")[0]
                    #reply = QMessageBox.question(self, 'Message', "͔͔͔♪♫♬ Çalma Listesinden ♪♫♬ ͕͕͕ " + path_name, QMessageBox.Ok)
                    #time.sleep(2)
                    mixer.init()
                    mixer.music.load('/home/pi/LookPlayIoTProject/musics/(pop)Aleyna Tilki - Sen Olsan Bari.mp3')
                    mixer.music.set_volume(1.0)
                    mixer.music.play()
                elif(Id == 2):
                    Id = "Hüseyin"
                elif(Id == 3):
                    Id = "Recep"
                elif(Id == 5):
                    Id = "Kayhan"
                #If not exist, then it is Unknown
                else:
                    Id = "Unknown"
                    
                # Put text describe who is in the picture
                cv2.rectangle(im, (x-22,y-90), (x+w+22, y-22), (0,255,0), -1)
                cv2.putText(im, str(Id), (x,y-40), font, 2, (255,255,255), 3)

            # Display the video frame with the bounded rectangle
            cv2.imshow('im',im) 

            # If 'q' is pressed, close program
            if cv2.waitKey(10) & 0xFF == ord('q'):
                break

    def kayitsilBtn(self):

        cap = cv2.VideoCapture(0)
        count = 0
        while(True):
            # Capture frame-by-frame
            ret, frame = cap.read()

            # Our operations on the frame come here
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            faces = face_detector.detectMultiScale(gray, 1.3, 5)

            for (x,y,w,h) in faces:

                # Crop the image frame into rectangle
                cv2.rectangle(frame, (x,y), (x+w,y+h), (255,0,0), 2)
                
                # Increment sample face image
                count += 1

                # Save the captured image into the datasets folder
                cv2.imwrite("dataset/User." + str(face_id) + '.' + str(count) + ".jpg", gray[y:y+h,x:x+w])


            cv2.imshow('frame', frame)
            # Display the resulting frame
            if cv2.waitKey(100) & 0xFF == ord('q'):
                break

            elif count>50:
                break

    def calmalistesiBtn(self):
        
        reply = QMessageBox.question(self, 'Message', "LookPlay sizi görecek, yüzünüzü sabit tutun. Arada bir çok hafif sağa sola bakın.", QMessageBox.Ok)
        
    def closeEvent(self, event):

        reply = QMessageBox.question(self, 'Message', "Çıkmak istediğinize emin misiniz?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()




if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = mainWindow()
    sys.exit(app.exec_())
