import tkinter as tk
from tkinter import messagebox
import random

def uygulama_dedektifi_oyna(parent=None, kullanici_adi=None, puan=None):
    sorular = [
        ("Bir uygulama hangi izinleri istemeli?", ["Sadece gerçekten gerekli izinler", "Tüm izinleri isteyebilir çünkü daha fazla özellik sunar", "Kullanıcıya sormadan arka planda izin almalı"], "Sadece gerçekten gerekli izinler"),
        ("Bir uygulama neden kamera izni ister?", ["Fotoğraf çekmek için", "Kullanıcıyı izlemek ve veri toplamak için", "Kamera açıkken reklam göstermek için"], "Fotoğraf çekmek için"),
        ("Bir uygulama neden mikrofon izni ister?", ["Ses kaydı için", "Arka planda ortam dinlemesi yapmak için", "Telefonun sesini analiz etmek için"], "Ses kaydı için"),
        ("Bir uygulama neden konum izni ister?", ["Harita için", "Kullanıcıyı sürekli takip etmek için", "Yakındaki cihazlara otomatik bağlanmak için"], "Harita için"),
        ("Bir uygulama neden rehber izni ister?", ["Arkadaş eklemek için", "Rehberdeki kişilere reklam göndermek için", "Kişisel verileri üçüncü partiyle paylaşmak için"], "Arkadaş eklemek için"),
        ("Bir uygulama neden bildirim izni ister?", ["Sana haber vermek için", "Bildirimlerle kişisel veri toplamak için", "Bildirimleri kullanarak zararlı yazılım yaymak için"], "Sana haber vermek için"),
        ("Bir uygulama neden depolama izni ister?", ["Dosya kaydetmek için", "Kişisel dosyaları izinsiz kopyalamak için", "Telefonun hafızasını doldurmak için"], "Dosya kaydetmek için"),
        ("Bir uygulama neden SMS izni ister?", ["Kod göndermek için", "Kullanıcı adına SMS gönderip dolandırıcılık yapmak için", "SMS'leri izinsiz yedeklemek için"], "Kod göndermek için"),
        ("Bir uygulama neden telefon izni ister?", ["Arama yapmak için", "Kullanıcıyı izinsiz aramak için", "Telefonu uzaktan kapatmak için"], "Arama yapmak için"),
        ("Bir uygulama neden takvim izni ister?", ["Etkinlik eklemek için", "Takvimdeki etkinlikleri silmek için", "Takvim verilerini reklam şirketleriyle paylaşmak için"], "Etkinlik eklemek için"),
        ("Bir uygulama neden sensör izni ister?", ["Adım saymak için", "Sensör verilerini üçüncü partiye satmak için", "Telefonun hareketlerini izlemek için"], "Adım saymak için"),
        ("Bir uygulama neden internet izni ister?", ["Veri almak için", "Kullanıcı verilerini izinsiz göndermek için", "Arka planda zararlı yazılım indirmek için"], "Veri almak için"),
        ("Bir uygulama neden Bluetooth izni ister?", ["Cihaz bağlamak için", "Yakındaki cihazlara izinsiz veri göndermek için", "Bluetooth'u kullanarak konum takibi yapmak için"], "Cihaz bağlamak için"),
        ("Bir uygulama neden arka planda çalışma izni ister?", ["Bildirim göndermek için", "Arka planda veri toplamak için", "Telefonun pilini hızlıca bitirmek için"], "Bildirim göndermek için"),
        ("Bir uygulama neden fotoğraf galerisi izni ister?", ["Fotoğraf yüklemek için", "Galeriye izinsiz erişip fotoğrafları kopyalamak için", "Galeriye reklam eklemek için"], "Fotoğraf yüklemek için"),
        ("Bir uygulama neden hareket izni ister?", ["Adım saymak için", "Kullanıcının hareketlerini izlemek için", "Telefonun konumunu sürekli güncellemek için"], "Adım saymak için"),
        ("Bir uygulama neden ekran kaydı izni ister?", ["Ekran videosu almak için", "Kullanıcı izni olmadan ekranı kaydetmek için", "Ekran görüntülerini üçüncü partiye göndermek için"], "Ekran videosu almak için"),
        ("Bir uygulama neden arama kaydı izni ister?", ["Arama geçmişi için", "Arama kayıtlarını izinsiz paylaşmak için", "Arama geçmişini silmek için"], "Arama geçmişi için"),
        ("Bir uygulama neden uygulama içi satın alma izni ister?", ["Satın alma yapmak için", "Kullanıcıdan izinsiz ödeme almak için", "Satın alma verilerini üçüncü partiyle paylaşmak için"], "Satın alma yapmak için"),
        ("Bir uygulama neden sağlık verisi izni ister?", ["Adım saymak için", "Sağlık verilerini izinsiz toplamak için", "Sağlık verilerini reklam amaçlı kullanmak için"], "Adım saymak için"),
        ("Bir uygulama neden bildirim izni ister?", ["Sana haber vermek için", "Bildirimlerle kişisel veri toplamak için", "Bildirimleri kullanarak zararlı yazılım yaymak için"], "Sana haber vermek için"),
    ]
    dogru_sayisi = 0
    kullanilan_sorular = set()
    for _ in range(3):
        kalan_sorular = [s for i, s in enumerate(sorular) if i not in kullanilan_sorular]
        secilen = random.choice(kalan_sorular)
        secilen_idx = sorular.index(secilen)
        kullanilan_sorular.add(secilen_idx)
        soru, secenekler, dogru = secilen
        def yeni_soru():
            nonlocal soru, secenekler, dogru, secilen_idx
            kalan = [s for i, s in enumerate(sorular) if i not in kullanilan_sorular]
            if kalan:
                yeni = random.choice(kalan)
                yeni_idx = sorular.index(yeni)
                kullanilan_sorular.remove(secilen_idx)
                kullanilan_sorular.add(yeni_idx)
                return yeni
            return secilen
        def kontrol(secim):
            if secim == dogru:
                messagebox.showinfo('Doğru!', 'Tebrikler, doğru cevap!')
                nonlocal dogru_sayisi
                dogru_sayisi += 1
                win.destroy()
            else:
                win.destroy()
                return -1
        win = tk.Toplevel(parent) if parent else tk.Tk()
        win.title('Uygulama Dedektifi')
        win.state('zoomed')
        if kullanici_adi is not None and puan is not None:
            profil = tk.Frame(win, bg="#1e355e", bd=0, highlightthickness=0)
            profil.place(relx=0.5, rely=0.08, anchor="center", width=320, height=40)
            tk.Label(profil, text=f"👤 {kullanici_adi}   ⭐ Puan: {puan}", font=("Segoe UI", 13, "bold"), bg="#1e355e", fg="white").pack()
        card = tk.Frame(win, bg="white", bd=0, highlightthickness=0)
        card.place(relx=0.5, rely=0.5, anchor="center", width=900, height=700)
        icon = tk.Label(card, text="📱", font=("Segoe UI", 38), bg="white")
        icon.pack(pady=(18,0))
        lbl = tk.Label(card, text=soru, font=("Segoe UI", 24, "bold"), bg="white", fg="#1e355e", wraplength=800)
        lbl.pack(pady=(18,18))
        for sec in secenekler:
            btn = tk.Button(card, text=sec, font=("Segoe UI", 20), bg="#f0f6ff", fg="#1e355e", activebackground="#b3d1ff", activeforeground="#1e355e", relief="flat", bd=0, highlightthickness=0, padx=8, pady=8, cursor="hand2", command=lambda s=sec: kontrol(s))
            btn.pack(pady=8, ipadx=8, ipady=4, fill="x", expand=True)
        if parent:
            parent.wait_window(win)
        else:
            win.mainloop()
    if 'dogru_sayisi' in locals():
        return dogru_sayisi

if __name__ == '__main__':
    uygulama_dedektifi_oyna() 