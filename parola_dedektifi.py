import tkinter as tk
from tkinter import messagebox
import random

def parola_dedektifi_oyna(parent=None, kullanici_adi=None, puan=None):
    sabit_sorular = [
        ("Sence en güvenli parola hangisi?", ["123456", "kedi123", "Xb@7Tu9K!rT"], "Xb@7Tu9K!rT"),
        ("Parolanda hangisi olmalı?", ["Büyük/küçük harf, rakam, sembol", "Sadece harf ve rakam", "Sadece harf"], "Büyük/küçük harf, rakam, sembol"),
        ("Parolanı kimlerle paylaşabilirsin?", ["Kimseyle", "Ailenle ve arkadaşlarınla", "Güvendiğin kişilerle"], "Kimseyle"),
        ("Aşağıdakilerden hangisi zayıf bir parola?", ["123456", "Klm2024!", "Klm2024"], "123456"),
        ("Parolanı unutmamak için ne yapmalısın?", ["Bir parola yöneticisi kullanmak", "Parolayı e-posta ile göndermek", "Parolayı bilgisayarın masaüstüne yazmak"], "Bir parola yöneticisi kullanmak"),
        ("Aşağıdakilerden hangisi parola değildir?", ["doğum tarihi", "EvcilHayvanAdi2023", "Parola123!"], "Parola123!"),
        ("Parolanı ne sıklıkla değiştirmelisin?", ["Düzenli olarak", "Sadece unutunca", "Her girişte"], "Düzenli olarak"),
        ("Parolanı not almak için en güvenli yer?", ["Parola yöneticisi", "Telefonun notlar uygulaması", "E-posta taslağı"], "Parola yöneticisi"),
        ("Aşağıdakilerden hangisi parola güvenliğini artırır?", ["İki faktörlü kimlik doğrulama", "Parolayı sık sık paylaşmak", "Aynı parolayı her yerde kullanmak"], "İki faktörlü kimlik doğrulama"),
        ("Parolanı unutursan ne yapmalısın?", ["Şifre sıfırlama seçeneğini kullanmak", "Arkadaşına sormak", "Tahmin etmeye çalışmak"], "Şifre sıfırlama seçeneğini kullanmak"),
        ("Parolanı oluştururken ne yapmamalısın?", ["Kişisel bilgi kullanmak", "Rakam ve sembol eklemek", "Büyük/küçük harf kullanmak"], "Kişisel bilgi kullanmak"),
        ("Aşağıdakilerden hangisi parola güvenliği için yanlıştır?", ["Parolayı kimseyle paylaşmamak", "Parolayı e-posta ile göndermek", "Güçlü parola kullanmak"], "Parolayı e-posta ile göndermek"),
        ("Parolanı bir yere yazacaksan nereye yazmalısın?", ["Parola yöneticisi", "Defter", "E-posta taslağı"], "Parola yöneticisi"),
        ("Aşağıdakilerden hangisi parola güvenliğini azaltır?", ["Aynı parolayı birden fazla yerde kullanmak", "Güçlü parola oluşturmak", "Parolayı sık sık değiştirmek"], "Aynı parolayı birden fazla yerde kullanmak"),
        ("Parolanı oluştururken hangisi en iyisidir?", ["Uzun ve karmaşık", "Kısa ve basit", "Sadece harf ve rakam"], "Uzun ve karmaşık"),
        ("Parolanı kimseyle paylaşmaman gerektiğini biliyor musun?", ["Evet", "Hayır", "Bazen, güvendiğim kişilerle"], "Evet"),
        ("Aşağıdakilerden hangisi parola güvenliği için doğrudur?", ["Parolayı sık sık değiştirmek", "Parolayı başkasıyla paylaşmak", "Parolayı unutmamak için not almak"], "Parolayı sık sık değiştirmek"),
        ("Parolanı oluştururken hangisi yanlış?", ["Kişisel bilgi kullanmak", "Rakam ve sembol eklemek", "Büyük/küçük harf kullanmak"], "Kişisel bilgi kullanmak"),
        ("Aşağıdakilerden hangisi parola güvenliğini artırır?", ["Uzun ve karmaşık parola", "Kısa ve basit parola", "Sadece rakam"], "Uzun ve karmaşık parola"),
        ("Parolanı bir başkasıyla paylaşmak güvenli midir?", ["Hayır", "Evet, güvendiğim kişilerle", "Bazen"], "Hayır"),
    ]
    # Şıklarında kullanıcı adı geçen soru
    guclu_parola_soru = ("Aşağıdakilerden hangisi güçlü bir parola örneğidir?", None, "G9!kLm#2")
    sorular = []
    for soru, secenekler, dogru in sabit_sorular:
        sorular.append((soru, secenekler, dogru))
    # Kullanıcı adı varsa, ilgili soruyu dinamik ekle
    if kullanici_adi:
        ad = str(kullanici_adi).strip()
        secenekler = [f"{ad.lower()}1234!", f"{ad.capitalize()}2023", "G9!kLm#2"]
        sorular.append((guclu_parola_soru[0], secenekler, guclu_parola_soru[2]))
    else:
        sorular.append((guclu_parola_soru[0], ["mustafa2023", "Mustafa2023", "G9!kLm#2"], guclu_parola_soru[2]))
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
        win.title('Parola Dedektifi')
        win.state('zoomed')
        if kullanici_adi is not None and puan is not None:
            profil = tk.Frame(win, bg="#1e355e", bd=0, highlightthickness=0)
            profil.place(relx=0.5, rely=0.08, anchor="center", width=320, height=40)
            tk.Label(profil, text=f"👤 {kullanici_adi}   ⭐ Puan: {puan}", font=("Segoe UI", 13, "bold"), bg="#1e355e", fg="white").pack()
        card = tk.Frame(win, bg="white", bd=0, highlightthickness=0)
        card.place(relx=0.5, rely=0.5, anchor="center", width=900, height=700)
        icon = tk.Label(card, text="🔑", font=("Segoe UI", 38), bg="white")
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
    parola_dedektifi_oyna() 