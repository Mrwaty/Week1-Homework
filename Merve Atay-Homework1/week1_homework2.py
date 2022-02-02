#Kullanıcıdan Adi, Soyadi, Ogrenci Numarasi, 4 ders adi, bu derslerin Vize ve Final notlari istenecektir.
#Vize notunun % 40′ı ile Final Notunun %60′ınin toplamı yil sonu ortalamasini verecektir.
#Ortalama 50‘den küçükse ekranda “KALDI“, 50 ve üstüyse ekranda “GEÇTİ” yazdırılacaktır.
#Bu yazdirma islemi 4 ders icinde yapilacak ve dersler alt alta yazdirilacaktir.

ad = input("Adiniz: ")
soyad = input("Soyadiniz: ")
no = input("Ögrenci no: ")

ders1 = input("1.Dersi giriniz: ")
vize1 = int(input(f"{ders1} dersinin vize notunu giriniz: "))
final1 = int(input(f"{ders1} dersinin final notunu giriniz: "))

ortalama1 = int((vize1 * 40 / 100) + (final1 * 60 / 100))

if 0 <= ortalama1 < 50:
    print(f"{ders1} dersinden kaldiniz.")

elif 50 <= ortalama1 <= 100:
    print(f"{ders1} dersinden gectiniz.")

else:
    print("Girdiginiz bilgileri kontrol edip tekrar deneyiniz.")

ders2 = input("2.Dersi giriniz: ")
vize2 = int(input(f"{ders2} dersinin vize notunu giriniz: "))
final2 = int(input(f"{ders2} dersinin final notunu giriniz: "))

ortalama2 = int((vize2 * 40 / 100) + (final2 * 60 / 100))

if 0 <= ortalama2 < 50:
    print(f"{ders2} dersinden kaldiniz.")

elif 50 <= ortalama2 <= 100:
    print(f"{ders2} dersinden gectiniz.")

else:
    print("Girdiginiz bilgileri kontrol edip tekrar deneyiniz.")

ders3 = input("3.Dersi giriniz: ")
vize3 = int(input(f"{ders3} dersinin vize notunu giriniz: "))
final3 = int(input(f"{ders3} dersinin final notunu giriniz: "))

ortalama3 = int((vize3 * 40 / 100) + (final3 * 60 / 100))

if 0 <= ortalama3 < 50:
    print(f"{ders3} dersinden kaldiniz.")

elif 50 <= ortalama3 <= 100:
    print(f"{ders3} dersinden gectiniz.")

else:
    print("Girdiginiz bilgileri kontrol edip tekrar deneyiniz.")

ders4 = input("4.Dersi giriniz: ")
vize4 = int(input(f"{ders4} dersinin vize notunu giriniz: "))
final4 = int(input(f"{ders4} dersinin final notunu giriniz: "))

ortalama4 = int((vize4 * 40 / 100) + (final4 * 60 / 100))

if 0 <= ortalama4 < 50:
    print(f"{ders4} dersinden kaldiniz.")

elif 50 <= ortalama4 <= 100:
    print(f"{ders4} dersinden gectiniz.")

else:
    print("Girdiginiz bilgileri kontrol edip tekrar deneyiniz.")