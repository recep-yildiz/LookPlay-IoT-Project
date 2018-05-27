# LookPlay-IoT-Project
Kocaeli Üniversitesi Bilişim Sistemleri Mühendisliği 3. Sınıf - Nesnelerin İnterneti dersi projesidir.

# Türkçe

## Proje Ne Yapar?
* Proje hala geliştirme aşamasında olup özetle yüz tanıma ile kişiye özel müzik listesi çalar.
* Picamera ile kullanıcının yüzü tanımlanıp bu yüz verisi eğitilerek yüze ilişkin müzik listesi bulutta veya yerelde tutulabilir.
* Program tanılama arayüzünde kayıtlı kullanıcılardan birini tanıladığı an o kişiye ilişkin müzik listesini devreye sokar.
* Kullanıcının metin tabanlı verileri bulut üzerinde (Dropbox) tutulur. 
* Buluta kayıt işlemi: Metin veri proje dizininde önce bir metin dosyasına kaydedilir. Bu dosya yazdığımız bir cronjob (Bash Script) ile belirli aralıklarda kontrol edilir. 
Kontrol işleminde dosyanın kayıt sürelerine bakılır, iki kayıt arasında zaman farkı varsa (dosya değişmiştir) buluta kayıt işlemi gerçekleşir.

## Projenin Tamamlanmamış Fonksiyonları
* Dropbox üzerinde müzik çaldırma işlemi
* Tanılama arayüzünde optimizasyon
* Veritabanı. Projede kullanıcılar ve müzikler demo olarak sunulmaktadır. Kullanıcı kaydı esnasında her yeni yüz için face_id bir artırılarak yeni kullanıcı yüzü datasete eklenir.
Tanılama ekranında basit bir if sorgusuyla face_id'si mevcut olan kullanıcının yüzünü çerçeveye alır ve bu if sorgusu altında bir müzik verisi varsa bunu çalar.
* Kameradan görüntü alınan pencerenin kapanmasıyla ilgili sorun mevcut.

## Projede Ne Kullandık? Ne Kurmalı?
* Görüntü işleme için -> OpenCV2 - [Rehber](https://www.pyimagesearch.com/2016/04/18/install-guide-raspberry-pi-3-raspbian-jessie-opencv-3/)
* Görüntü almak için -> Picamera 
* Bulut Hizmeti -> Dropbox - [Public Project File](https://www.dropbox.com/developers/apps/info/kqchkl1olkzsxec)
* PyQt5 arayüz kütüphanesi
* Crontab oluşturmak için 'uploadToDbox_yedek.sh' bash betiğini <code>sudo crontab -e</code> ile yeni bir göreve atayabilirsiniz.
Crontab işlemi ile sorun yaşandığı takdirde betik, proje dizininde <code>sudo ./uploadToDbox.sh</code> komutu ile çalıştırılabilir. Komutun çalıştığı satırda başka bir işlem yapmamanız gerekir.
* Proje raporu: [Rapor](https://www.dropbox.com/s/1ml2f2jsa9y1wru/iotrapor_lookplay.pdf?dl=0)

## Özet Olarak İşleyiş
* look_play.py -> Ana program, içerisinden kayıt eklenir, varsa kayıtlar tanınabilir.
* userInfoForCloud.txt -> Kullanıcı metin verilerini tutar.
* cloud_dropbox.py -> Metin verilerinin buluta nasıl kaydedileceğini belirten betik.
* uploadToDbox.sh -> Metin verilerinin kaydedilme sürelerini kontrol ederek buluta upload eden bash script.
(Bu betik cloud_dropbox.py betiğini çağırır)
* training.py -> Ana program içerisinden kayıt sırasında elde edilen yüz verisi /dataset altında tutulur. training.py ise bu dizindeki görüntüler ile sinir OpenCV sinir ağlarını eğitir.


# English
## To be added later.
