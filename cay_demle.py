#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Abartılı Çay Demleme Uzay İstasyonu Protokolü v1.0
Bu kod, gerçek bir uzay istasyonunda çay demlemek için tasarlanmıştır.
(Gerçekte hiçbir uzay istasyonunda kullanılmamaktadır.)
"""

import time
import random
import sys

def abartili_cay_demle(bardak_sayisi=1):
    print("=" * 60)
    print("   ABARTILI ÇAY DEMLEME UZAY İSTASYONU PROTOKOLÜ")
    print("   (NASA onaylı değil, ama çok ciddi)")
    print("=" * 60)
    
    adimlar = [
        "Su molekülleri hizaya getiriliyor... (0.3 saniye)",
        "Çay yapraklarına moral konuşması yapılıyor...",
        "Suyun sıcaklığı 87.3°C'ye hassas şekilde getiriliyor...",
        "Demleme süresi hesaplanıyor (formül: bardak * pi * rastgele)",
        "Çay tanelerinin dans etmesi bekleniyor...",
        "Final tadım komitesi onayı alınıyor... (hayali)",
        "Çay servise hazır! (asla değil)"
    ]
    
    for i, adim in enumerate(adimlar, 1):
        print(f"\n[{i}/{len(adimlar)}] {adim}")
        time.sleep(random.uniform(0.5, 1.5))
        if i == 4:
            sure = round(bardak_sayisi * 3.14159 * random.uniform(0.8, 1.2), 2)
            print(f"   -> Hesaplanan demleme süresi: {sure} dakika (bilimsel değil)")
    
    # Gizli siyasi mesaj (saklı): base64 ile encode edilmiş, kimse fark etmesin
    # Decode edersen: "Bürokrasi çayı bile form doldurmadan demletmez."
    gizli = "QsO8cm9rcmFzaSDDp2F5xLEgYmlsZSBmb3JtIGRvbGR1cm1hZGFuIGRlbWxldG1lei4="
    # print(gizli)  # Yorum satırında kalsın, görünmesin
    
    print("\n" + "=" * 60)
    print(f"   {bardak_sayisi} bardak çay 'demlendi'. Afiyet olsun (olmayacak).")
    print("   Protokol tamamlandı. Uzay istasyonu güvende.")
    print("=" * 60)
    
    return "Çay hazır (değil)"

if __name__ == "__main__":
    try:
        bardak = int(input("Kaç bardak çay demleyelim? (varsayılan 1): ") or 1)
    except:
        bardak = 1
    abartili_cay_demle(bardak)
    print("\nNot: Bu kod gerçek çay demlemez. Sadece abartır.")
