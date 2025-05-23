import tkinter as tk
from tkinter import messagebox

class SiberKahramanOyun:
    def __init__(self, root):
        self.root = root
        self.root.title('Siber Kahraman Görevleri')
        self.root.geometry('500x400')
        self.puan = 0
        self.istasyon = 0
        self.istasyonlar = [
            self.istasyon1_parola_dedektifi,
            self.istasyon2_kamera_canavari,
            self.istasyon3_bilgi_avcisi,
            self.istasyon4_uygulama_dedektifi,
            self.istasyon5_wifi_tehlikesi
        ]
        self.ana_menu()

    def ana_menu(self):
        self.temizle_ekran()
        baslik = tk.Label(self.root, text='Siber Kahraman Görevleri', font=('Arial', 20, 'bold'))
        baslik.pack(pady=30)
        basla_btn = tk.Button(self.root, text='Oyuna Başla', font=('Arial', 14), command=self.oyunu_baslat)
        basla_btn.pack(pady=10)
        kurallar_btn = tk.Button(self.root, text='Kuralları Gör', font=('Arial', 14), command=self.kurallari_goster)
        kurallar_btn.pack(pady=10)
        cikis_btn = tk.Button(self.root, text='Çıkış', font=('Arial', 14), command=self.root.quit)
        cikis_btn.pack(pady=10)

    def kurallari_goster(self):
        messagebox.showinfo('Kurallar', 'Her istasyonda bir görev seni bekliyor!\nDoğru seçimlerle Siber Kahraman Rozeti ve Sertifikası kazan!')

    def oyunu_baslat(self):
        self.puan = 0
        self.istasyon = 0
        self.istasyonlar[self.istasyon]()

    def temizle_ekran(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def sonraki_istasyon(self):
        self.istasyon += 1
        if self.istasyon < len(self.istasyonlar):
            self.istasyonlar[self.istasyon]()
        else:
            self.final_ekrani()

    # --- İstasyonlar ---
    def istasyon1_parola_dedektifi(self):
        self.temizle_ekran()
        soru = tk.Label(self.root, text='Parola Dedektifi\n\nSence en güvenli parola hangisi?', font=('Arial', 16))
        soru.pack(pady=20)
        parolalar = ['123456', 'kedi123', 'Xb@7Tu9K!rT']
        for parola in parolalar:
            btn = tk.Button(self.root, text=parola, font=('Arial', 14), width=20,
                            command=lambda p=parola: self.kontrol_parola(p))
            btn.pack(pady=5)

    def kontrol_parola(self, secim):
        if secim == 'Xb@7Tu9K!rT':
            self.puan += 1
            messagebox.showinfo('Doğru!', 'Tebrikler, en güvenli parolayı seçtin!')
        else:
            messagebox.showinfo('Yanlış', 'Bu parola çok kolay tahmin edilebilir!')
        self.sonraki_istasyon()

    def istasyon2_kamera_canavari(self):
        self.temizle_ekran()
        soru = tk.Label(self.root, text='Kamera Canavarı\n\nKameranı açmadan önce ne yapmalısın?', font=('Arial', 16))
        soru.pack(pady=20)
        secenekler = [
            'Düşünmeden açarım',
            'Önce etrafa bakarım ve gerekliyse açarım',
            'Her zaman açık bırakırım'
        ]
        for secenek in secenekler:
            btn = tk.Button(self.root, text=secenek, font=('Arial', 14), width=40,
                            command=lambda s=secenek: self.kontrol_kamera(s))
            btn.pack(pady=5)

    def kontrol_kamera(self, secim):
        if secim == 'Önce etrafa bakarım ve gerekliyse açarım':
            self.puan += 1
            messagebox.showinfo('Doğru!', 'Harika! Kameranı açmadan önce düşünmelisin.')
        else:
            messagebox.showinfo('Yanlış', 'Kameranı açmadan önce düşünmelisin!')
        self.sonraki_istasyon()

    def istasyon3_bilgi_avcisi(self):
        self.temizle_ekran()
        soru = tk.Label(self.root, text='Bilgi Avcısı\n\nAşağıdakilerden hangisi gizli bilgidir?', font=('Arial', 16))
        soru.pack(pady=20)
        secenekler = [
            'Adın, yaşın ve okulun',
            'En sevdiğin renk',
            'En sevdiğin yemek'
        ]
        for secenek in secenekler:
            btn = tk.Button(self.root, text=secenek, font=('Arial', 14), width=40,
                            command=lambda s=secenek: self.kontrol_bilgi(s))
            btn.pack(pady=5)

    def kontrol_bilgi(self, secim):
        if secim == 'Adın, yaşın ve okulun':
            self.puan += 1
            messagebox.showinfo('Doğru!', 'Tebrikler, gizli bilgiyi doğru seçtin!')
        else:
            messagebox.showinfo('Yanlış', 'Bu bilgi gizli değildir!')
        self.sonraki_istasyon()

    def istasyon4_uygulama_dedektifi(self):
        self.temizle_ekran()
        soru = tk.Label(self.root, text='Uygulama Dedektifi\n\nBir uygulama hangi izinleri istemeli?', font=('Arial', 16))
        soru.pack(pady=20)
        secenekler = [
            'Sadece gerçekten gerekli izinler',
            'Tüm izinler',
            'Hiç izin istememeli'
        ]
        for secenek in secenekler:
            btn = tk.Button(self.root, text=secenek, font=('Arial', 14), width=40,
                            command=lambda s=secenek: self.kontrol_uygulama(s))
            btn.pack(pady=5)

    def kontrol_uygulama(self, secim):
        if secim == 'Sadece gerçekten gerekli izinler':
            self.puan += 1
            messagebox.showinfo('Doğru!', 'Doğru! Gereksiz izinlere dikkat etmelisin.')
        else:
            messagebox.showinfo('Yanlış', 'Tüm izinleri vermek güvenli değildir!')
        self.sonraki_istasyon()

    def istasyon5_wifi_tehlikesi(self):
        self.temizle_ekran()
        soru = tk.Label(self.root, text='Wi-Fi Tehlikesi\n\nAşağıdaki Wi-Fi ağlarından hangisi daha güvenlidir?', font=('Arial', 16))
        soru.pack(pady=20)
        secenekler = [
            'Okul_WiFi_Guvenli',
            'ÜcretsizWiFi_HemenTıkla'
        ]
        for secenek in secenekler:
            btn = tk.Button(self.root, text=secenek, font=('Arial', 14), width=40,
                            command=lambda s=secenek: self.kontrol_wifi(s))
            btn.pack(pady=5)

    def kontrol_wifi(self, secim):
        if secim == 'Okul_WiFi_Guvenli':
            self.puan += 1
            messagebox.showinfo('Doğru!', 'Tebrikler, güvenli Wi-Fi ağını seçtin!')
        else:
            messagebox.showinfo('Yanlış', 'Açık Wi-Fi ağları tehlikeli olabilir!')
        self.sonraki_istasyon()

    def final_ekrani(self):
        self.temizle_ekran()
        if self.puan == 5:
            sonuc = 'Tebrikler! Tüm görevleri başarıyla tamamladın!\nSiber Kahraman Rozeti ve Sertifikası kazandın!'
        else:
            sonuc = f'{self.puan}/5 görev doğru! Yine de harika bir iş çıkardın!'
        label = tk.Label(self.root, text=sonuc, font=('Arial', 16), wraplength=400)
        label.pack(pady=30)
        ana_menu_btn = tk.Button(self.root, text='Ana Menüye Dön', font=('Arial', 14), command=self.ana_menu)
        ana_menu_btn.pack(pady=10)
        cikis_btn = tk.Button(self.root, text='Çıkış', font=('Arial', 14), command=self.root.quit)
        cikis_btn.pack(pady=10)

if __name__ == '__main__':
    root = tk.Tk()
    root.state('zoomed')
    app = SiberKahramanOyun(root)
    root.mainloop() 