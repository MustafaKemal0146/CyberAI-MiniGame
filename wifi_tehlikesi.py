import tkinter as tk
from tkinter import messagebox
import random

def wifi_tehlikesi_oyna(parent=None, kullanici_adi=None, puan=None):
    sorular = [
        ("Aşağıdaki Wi-Fi ağlarından hangisi daha güvenlidir?", ["Okul_WiFi_Guvenli", "Kafe_WiFi_Guvenli_Gibi", "Free_Public_WiFi_5G"], "Okul_WiFi_Guvenli"),
        ("Açık Wi-Fi ağlarında ne yapmalısın?", ["Kişisel bilgi girmemeliyim", "Sadece sosyal medya hesaplarımı kullanırım", "Online alışveriş yapabilirim"], "Kişisel bilgi girmemeliyim"),
        ("Wi-Fi ağına bağlanırken neye dikkat etmelisin?", ["Güvenli ve bilinen ağ olmalı", "Sinyal gücü en yüksek olanı seçerim", "Ağ adında 'güvenli' yazıyorsa seçerim"], "Güvenli ve bilinen ağ olmalı"),
        ("Aşağıdakilerden hangisi tehlikelidir?", ["Free_Public_WiFi_5G", "Ev_WiFi_Guvenli", "Okul_WiFi_Guvenli"], "Free_Public_WiFi_5G"),
        ("Wi-Fi ağına bağlanmadan önce ne yapmalısın?", ["Ağın adını kontrol etmeliyim", "Ağda çok kişi varsa bağlanmam", "Ağ şifresi kolaysa bağlanırım"], "Ağın adını kontrol etmeliyim"),
        ("Aşağıdakilerden hangisi güvenli Wi-Fi kullanımı için doğrudur?", ["Şifreli ağa bağlanmak", "Ağda VPN varsa bağlanmak", "Ağ adında 'güvenli' yazıyorsa bağlanmak"], "Şifreli ağa bağlanmak"),
        ("Aşağıdakilerden hangisi Wi-Fi tehlikesidir?", ["Açık ve şifresiz ağlar", "Evdeki modem", "Şifreli okul ağı"], "Açık ve şifresiz ağlar"),
        ("Wi-Fi ağına bağlanırken neye dikkat etmelisin?", ["Ağın adının doğru olduğuna", "Ağda çok kişi olup olmadığına", "Ağda internetin hızlı olup olmadığına"], "Ağın adının doğru olduğuna"),
        ("Aşağıdakilerden hangisi güvenli değildir?", ["Herkese açık Wi-Fi", "Evdeki Wi-Fi", "Şifreli okul Wi-Fi"], "Herkese açık Wi-Fi"),
        ("Wi-Fi ağına bağlanırken ne yapmamalısın?", ["Kişisel bilgilerini paylaşmak", "Sadece video izlemek", "Ağ adını başkasıyla paylaşmak"], "Kişisel bilgilerini paylaşmak"),
        ("Aşağıdakilerden hangisi güvenli Wi-Fi kullanımı için yanlıştır?", ["Şifresiz ağa bağlanmak", "Şifreli ağa bağlanmak", "Evdeki Wi-Fi'yi kullanmak"], "Şifresiz ağa bağlanmak"),
        ("Aşağıdakilerden hangisi Wi-Fi tehlikesidir?", ["Açık ve şifresiz ağlar", "Evdeki modem", "Şifreli okul ağı"], "Açık ve şifresiz ağlar"),
        ("Wi-Fi ağına bağlanırken neye dikkat etmelisin?", ["Ağın adının doğru olduğuna", "Ağda çok kişi olup olmadığına", "Ağda internetin hızlı olup olmadığına"], "Ağın adının doğru olduğuna"),
        ("Aşağıdakilerden hangisi güvenli değildir?", ["Herkese açık Wi-Fi", "Evdeki Wi-Fi", "Şifreli okul Wi-Fi"], "Herkese açık Wi-Fi"),
        ("Wi-Fi ağına bağlanırken ne yapmamalısın?", ["Kişisel bilgilerini paylaşmak", "Sadece video izlemek", "Ağ adını başkasıyla paylaşmak"], "Kişisel bilgilerini paylaşmak"),
        ("Aşağıdakilerden hangisi güvenli Wi-Fi kullanımı için yanlıştır?", ["Şifresiz ağa bağlanmak", "Şifreli ağa bağlanmak", "Evdeki Wi-Fi'yi kullanmak"], "Şifresiz ağa bağlanmak"),
        ("Aşağıdakilerden hangisi Wi-Fi tehlikesidir?", ["Açık ve şifresiz ağlar", "Evdeki modem", "Şifreli okul ağı"], "Açık ve şifresiz ağlar"),
        ("Wi-Fi ağına bağlanırken neye dikkat etmelisin?", ["Ağın adının doğru olduğuna", "Ağda çok kişi olup olmadığına", "Ağda internetin hızlı olup olmadığına"], "Ağın adının doğru olduğuna"),
        ("Aşağıdakilerden hangisi güvenli değildir?", ["Herkese açık Wi-Fi", "Evdeki Wi-Fi", "Şifreli okul Wi-Fi"], "Herkese açık Wi-Fi"),
        ("Wi-Fi ağına bağlanırken ne yapmamalısın?", ["Kişisel bilgilerini paylaşmak", "Sadece video izlemek", "Ağ adını başkasıyla paylaşmak"], "Kişisel bilgilerini paylaşmak"),
        ("Aşağıdakilerden hangisi güvenli Wi-Fi kullanımı için yanlıştır?", ["Şifresiz ağa bağlanmak", "Şifreli ağa bağlanmak", "Evdeki Wi-Fi'yi kullanmak"], "Şifresiz ağa bağlanmak"),
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
        win.title('Wi-Fi Tehlikesi')
        win.state('zoomed')
        if kullanici_adi is not None and puan is not None:
            profil = tk.Frame(win, bg="#1e355e", bd=0, highlightthickness=0)
            profil.place(relx=0.5, rely=0.08, anchor="center", width=320, height=40)
            tk.Label(profil, text=f"👤 {kullanici_adi}   ⭐ Puan: {puan}", font=("Segoe UI", 13, "bold"), bg="#1e355e", fg="white").pack()
        card = tk.Frame(win, bg="white", bd=0, highlightthickness=0)
        card.place(relx=0.5, rely=0.5, anchor="center", width=900, height=700)
        icon = tk.Label(card, text="📶", font=("Segoe UI", 38), bg="white")
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
    wifi_tehlikesi_oyna() 