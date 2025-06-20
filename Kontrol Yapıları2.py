# Kullanıcıdan gizli sayıyı tahmin etmesini isteyen bir mini oyun.
# While döngüsü, koşul ifadeleri, break ve pass kullanılmıştır.

gizli_sayi = 7
hak = 5

print("1 ile 10 arasında bir sayı tahmin edin. Toplam", hak, "hakkınız var.")

while hak > 0:
    tahmin = int(input("Tahmininiz: "))

    if tahmin < 1 or tahmin > 10:
        print("Lütfen 1 ile 10 arasında bir sayı girin.")
        pass  # Hatalı giriş ama döngü devam etsin
    elif tahmin == gizli_sayi:
        print("Tebrikler! Doğru tahmin.")
        break  # Doğru tahmin edilince döngüden çık
    elif tahmin < gizli_sayi:
        print("Daha büyük bir sayı deneyin.")
    else:
        print("Daha küçük bir sayı deneyin.")

    hak -= 1

if hak == 0:
    print("Tahmin hakkınız bitti. Doğru sayı:", gizli_sayi)
