#Oyuncularin adlarini alip tas - kagit - makas oyunu oynatiniz. 10 el sonunda kazanan belli olsun. Skor sonucta gorunsun.

oyuncu1=input("Birinci oyuncu adinizi giriniz:")
oyuncu2=input("ikinci oyuncu adinizi giriniz:")

secim= ["tas", "kagit", "makas"]
puan1=0
puan2=0
i=0
while i<10:
    i+=1

    o1_secim = input(f"{oyuncu1} tas ise 't' makas ise 'm' kagit ise 'k' harfini giriniz: ")
    o2_secim = input(f"{oyuncu2} tas ise 't' makas ise 'm' kagit ise 'k' harfini giriniz: ")

    if ((o1_secim == 't' and o2_secim == 'm') or (o1_secim == 'k' and o2_secim == 't') or (o1_secim == 'm' and o2_secim == 'k')):
        puan1+=1
        print(f"{oyuncu1} puani: {puan1}\n{oyuncu2} puani: {puan2}")

    elif ((o1_secim == 'm' and o2_secim == 't') or (o1_secim == 't' and o2_secim == 'k') or (o1_secim == 'k' and o2_secim == 'm')):
        puan2+=1
        print(f"{oyuncu1} puani: {puan1}\n{oyuncu2} puani: {puan2}")

    elif ((o1_secim == 'm' and o2_secim == 'm') or (o1_secim == 't' and o2_secim == 't') or (o1_secim == 'k' and o2_secim == 'k')):
        print(f"{oyuncu1} puani: {puan1}\n{oyuncu2} puani: {puan2}")

    else:
        print("Gecerli bir harf giriniz.")

if puan1 < puan2:
    print(f"Kazanan:{oyuncu2}\nSkor: {puan2} - {puan1}")

elif puan1 > puan2:
    print(f"Kazanan:{oyuncu1}\nSkor: {puan1} - {puan2}")

else:
    print(f"Berabere kaldiniz.\nSkor: {puan2} - {puan1}")