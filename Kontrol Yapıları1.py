# Bir öğrencinin notlarını değerlendirip başarı durumu belirleniyor.
# if-elif-else, karşılaştırma ve mantıksal operatörler ile döngü yapıları kullanılmıştır.

notlar = [85, 92, 58, 73, 45, 100, 67]

for not_ in notlar:
    if not_ < 0 or not_ > 100:
        print("Geçersiz not:", not_)
        continue  # Geçersiz not varsa atla

    if not_ >= 90:
        print(not_, "→ Mükemmel! (AA)")
    elif not_ >= 80:
        print(not_, "→ Çok iyi (BA)")
    elif not_ >= 70:
        print(not_, "→ İyi (BB)")
    elif not_ >= 60:
        print(not_, "→ Orta (CB)")
    elif not_ >= 50:
        print(not_, "→ Geçer (CC)")
    else:
        print(not_, "→ Başarısız (FF)")
