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

## Projenin Tamamlanmamış Eksiklikleri
* Dropbox üzerinde müzik çaldırma işlemi
* Tanılama arayüzünde optimizasyon
* Veritabanı. Projede kullanıcılar ve müzikler demo olarak sunulmaktadır. Kullanıcı kaydı esnasında her yeni yüz için face_id bir artırılarak yeni kullanıcı yüzü datasete eklenir.
Tanılama ekranında basit bir if sorgusuyla face_id'si mevcut olan kullanıcının yüzünü çerçeveye alır ve bu if sorgusu altında bir müzik verisi varsa bunu çalar.

## Projede Ne Kullandık?
* Görüntü işleme için -> OpenCV2 - [Rehber](https://www.pyimagesearch.com/2016/04/18/install-guide-raspberry-pi-3-raspbian-jessie-opencv-3/)
* Görüntü almak için -> Picamera 
* Bulut Hizmeti -> Dropbox - [Public Project File](https://www.dropbox.com/developers/apps/info/kqchkl1olkzsxec)
* PyQt5 arayüz kütüphanesi
*

# English
## To be added later.
