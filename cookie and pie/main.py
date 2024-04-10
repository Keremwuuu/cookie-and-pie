import sys
import time
import random
secondlist = [10, 13, 16]
secondseçimi = random.choice(secondlist)

print("pie social media tools v1.0 2024.1 CC0 licence")
isim = input("isminizi giriniz: ")
print("merhaba", isim, "hoş geldin")
yaş = int(input("merhaba " + isim + ", yaşını girebilir misin: "))


if yaş > 8:
    print("panele girebilirsin", isim)
    print("#####################################################")
    uygulama = input("""
    1.youtube kanal puanlama "1"
    2.youtube bot basma tespiti "2"
    3.youtube izlenme hilesi 🔒
    4.facebook bot basma tespiti "4"
    5.facebook hesap puanlama "5"
    6.instagram bot tespiti "6"
    7.instagram hesap puanlama 🔒
    8.github profil puanlama 🔒
    9.intagram izlenme hilesi 🔒
    """)
    print("#####################################################")

    if uygulama == '1':
        print("youtube kanal puanlama paneline hoş geldin", isim)
        subscribers = int(input("youtube kanalınızın kaç abonesi var: "))
        izlenme = int(input("kanalınızın toplam izlenme sayısı: "))
        like = int(input("son iki videonuzdan gelen toplam like: "))
        dislike = int(input("son iki videonuzdaki toplam dislike: "))
        sonuç = subscribers / izlenme * like - dislike
        print("kanalınızın sevilme oranı: %", sonuç)
    elif uygulama == '2':
        print("youtube bot basma testine hoş geldiniz")
        abone = int(input("abone sayısı: "))
        izlenmeb = int(input("kanalın toplam izlenmesi: "))
        likeb = int(input("kanalın son videosunun likesi: "))
        sonuçbc = print("wait"+" ",secondseçimi," "+"seconds")
        time.sleep(secondseçimi)
        if izlenmeb < abone:
            print("BU KANALA BOT BASILMIŞ")
        else:
            print("bu kanala bot basılmamış tespit edilen bot 0")
    elif uygulama == '4':  
        print("facebook bot basma testine hoş geldiniz")
        tcpp = int(input("takipçi sayısı: "))
        izlenmebp = int(input("hesabın toplam izlenmesi: "))
        likebp = int(input("hesabın son gönderisinin likesi: "))
        sonuçbcp = print("wait"+" ",secondseçimi," "+"seconds")
        time.sleep(secondseçimi)
        if izlenmebp < tcpp:
            print("BU HESABA BOT BASILMIŞ O KİŞİYİ REPORT EDİN!")
        else:
            print("bu hesaba bot basılmamış :) emeğe saygı")
    elif uygulama == '5': 
        print("facebook hesap puanlama paneline hoş geldin", isim)
        subscriberstcpp = int(input("facebook hesabınızın kaç abonesi var: "))
        izlenmetcpp = int(input("hesabınızın toplam izlenme sayısı: "))
        liketcpp = int(input("son iki gönderinizden gelen toplam like: "))
        disliketcpp = int(input("son iki gönderinizdeki toplam dislike: "))
        sonuçtppc = subscriberstcpp / izlenmetcpp * liketcpp - disliketcpp
        print("hesabınızn sevilme oranı: %", sonuçtppc)
    elif uygulama == "6":
        print("instagram bot basma testine hoş geldiniz")
        tcpppp = int(input("takipçi sayısı: "))
        izlenmebpp = int(input("hesabın toplam izlenmesi: "))
        likebpp = int(input("hesabın son gönderisinin likesi: "))
        sonuçbcpp = print("wait"+" ",secondseçimi," "+"seconds")
        time.sleep(secondseçimi)
        if izlenmebpp < tcpppp:
            print("BU HESABA BOT BASILMIŞ O KİŞİYİ REPORT EDİN!")
        else:
            print("bu hesaba bot basılmamış :) emeğe saygı")
    else:
        print("Seçilen uygulama henüz desteklenmemektedir.")

else:
    print("8 yaşını doldurunca bu programı kullanabilirsin, sosyal medya küçüklere göre bir yer değil :(")
    sys.exit()
