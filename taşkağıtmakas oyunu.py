import random 

secenek = ("taş", "kağıt", "makas")


print("oyuna hoşgediniz, oyundan çıkmak istediğiniz zaman q'ya basabilirsiniz")

while True:
    secim = input("taş, kağıt, makas ?: ")
    bil_secim = random.choice(secenek)
    
    if secim == "taş":
        if bil_secim == "taş":
            print(f"bilgisayarın seçimi:{bil_secim}, oyun berabere")
        elif bil_secim == "kağıt":
            print(f"bilgisayarın seçimi: {bil_secim}, oyunu kaybettiniz")
        else:
            print(f"bilgisayarın seçimi: {bil_secim}, oyunu kazandınız")
    elif secim == "kağıt":
        if bil_secim == "taş":
            print(f"bilgisayarın seçimi: {bil_secim}, oyunu kazandınız")
        elif bil_secim == "kağıt":
            print(f"bilgisayarın seçimi: {bil_secim}, oyun berabere")
        else:
            print(f"bilgisayarın seçimi: {bil_secim}, oyunu kaybettiniz")
    elif secim == "q":
        print("oyundan çıkılıyor...")
        break
    
    elif secim == "makas":
        if bil_secim == "taş":
            print(f"bilgisayarın seçimi: {bil_secim}, oyunu kaybettiniz")
        elif bil_secim == "kağıt":
            print(f"bilgisayarın seçimi: {bil_secim}, oyunu kazandınız")
        else:
            print(f"bilgisayarın seçimi: {bil_secim}, oyun berabere")
    else:
        print("seçim anlaşılamadı, tekrar giriniz.")
        