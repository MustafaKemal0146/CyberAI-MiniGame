# Siber Kahraman Standı 2025

Bu oyun, çocuklara siber güvenlik bilinci kazandırmak için hazırlanmış, modern ve interaktif bir stand oyunudur.

## Özellikler
- 5 farklı istasyon: Parola Dedektifi, Kamera Canavarı, Bilgi Avcısı, Uygulama Dedektifi, Wi-Fi Tehlikesi
- Her istasyonda rastgele 3 soru (toplamda 21 soruluk havuzdan)
- Yanlış cevapta oyun hemen biter, tekrar deneme veya joker hakkı yoktur
- Puan ve rozet sistemi (Altın, Gümüş, Bronz, Teşekkür)
- Skor kaydı ve en iyi 10 skor tablosu
- PDF sertifika (Türkçe karakter destekli, otomatik oluşturulur)
- Modern, renkli, gradient arka planlı ve tam ekran arayüz
- Card/kutu stili, büyük oval butonlar, ikonlar, animasyonlar, yıldız/rozet efektleri
- Sonuçta konfeti/yıldız yağmuru animasyonu
- Tüm pencereler tam ekran açılır

## Kurulum
1. **Python 3.13** yüklü olmalı. (En sorunsuz deneyim için önerilen sürüm)
2. Terminalde şunu çalıştır:
   ```bash
   C:\Python313\python.exe -m pip install reportlab
   ```
3. Proje klasöründe `DejaVuSans.ttf` dosyası bulunmalı (Türkçe PDF için).

## Çalıştırma
Oyunu başlatmak için terminalde:
```bash
C:\Python313\python.exe main.py
```
Başka bir Python ile çalıştırırsanız PDF ve bazı özellikler çalışmayabilir.

## Kullanım
- Oyunu başlatınca tam ekranda isim girilir.
- Her istasyonda 3 soru gelir, yanlış cevapta oyun hemen biter ve "Kaybettin" ekranı çıkar.
- Tüm görevler bitince puan, rozet, sertifika ve skor tablosu gösterilir.
- Oyun sonunda PDF sertifika otomatik oluşturulur ve açılır.
- Oyun tamamen çevrimdışıdır, internet gerekmez.

## Notlar
- Çocuklar için güvenli ve eğlenceli olacak şekilde tasarlanmıştır.
- Her türlü geliştirme ve özelleştirme için kodu düzenleyebilirsiniz. 