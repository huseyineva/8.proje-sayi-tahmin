import random
import time


class sayiTahminOyunu():

    def __init__(self):
        self.bilgi()


    def bilgi(self):
        print("0 ile 100 arasında bir sayı tuttum. Bakalım bulabilecek misin?")
        print("Çıkmak için rakam dışında bir tuşa basınız...")
        print("")
        self.tahmin()

    def sayiUret(self):
        return random.randint(0,101)
    
    def tahmin(self):
        sayi = self.sayiUret()
        tahminSayisi = 0

        while True:
            
            try:
                istek = int(input("Tahmin ettiğiniz sayıyı giriniz: "))
                tahminSayisi += 1
                
                if istek == sayi:
                    print("Doğru tahmin yaptınız, tebrikler!")
                    print("")
                    print("Yeni bir sayı tuttum. Bakalım bunu da tahmin edebilecek misin? ***Çıkmak için rakam dışında bir tuşa basınız...***")
                    sayi = self.sayiUret()
                    tahminSayisi = 0

                elif sayi < 0 and sayi > 100:
                    print("Girdiğiniz sayi 0 ile 100 arasında değildir. Lütfen tekrar deneyiniz!")
                    print("")

                elif istek < sayi:
                    print("Tahmininiz, sayıdan küçüktür. Tekrar deneyiniz!")
                    print("")

                elif istek > sayi:
                    print("Tahmininiz, sayıdan büyüktür. Tekrar deneyiniz!")
                    print("")

            except:
                print("Oyundan çıkış yapılıyor...")
                break

if __name__ == "__main__":
    b = sayiTahminOyunu()
    b.tahmin
    print("Çıkış yapılıyor...")
    time.sleep(2)
             

        

