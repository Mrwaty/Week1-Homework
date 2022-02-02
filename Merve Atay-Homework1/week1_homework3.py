#Beden Kitle Indeksi

kilo= float(input("Kilonuzu giriniz/kg: "))
boy= float(input("Boyunuzu giriniz/m: "))

BMI= kilo / (boy**2) #BMI:Body Mass Index

if BMI < 25:
    print("Normal")

elif 25 <= BMI < 30:
    print("Fazla Kilolu")

elif 30 <= BMI < 40:
    print("Obez")

elif 40 <= BMI:
    print("Asiri Sisman")

else:
    print("Bilgilerinizi kontrol edip tekrar deneyiniz.")