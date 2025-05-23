import tkinter as tk
from tkinter import messagebox
import random

def bilgi_avcisi_oyna(parent=None, kullanici_adi=None, puan=None):
    sorular = [
        ("Aşağıdakilerden hangisi gizli bilgidir?", ["Adın, yaşın ve okulun", "Okulun adı ve adresi", "En sevdiğin renk"], "Adın, yaşın ve okulun"),
        ("Aşağıdakilerden hangisi kişisel bilgi değildir?", ["Okulun adı", "En sevdiğin hayvan", "Telefon numaran"], "En sevdiğin hayvan"),
        ("Aşağıdakilerden hangisi başkalarıyla paylaşılmamalı?", ["Adresin", "Okulun adresi", "En sevdiğin ders"], "Adresin"),
        ("Aşağıdakilerden hangisi gizli bilgi değildir?", ["En sevdiğin renk", "Telefon numaran", "Doğum tarihin"], "En sevdiğin renk"),
        ("Aşağıdakilerden hangisi gizli bilgi?", ["TC kimlik numaran", "Okulun adı", "En sevdiğin spor"], "TC kimlik numaran"),
        ("Aşağıdakilerden hangisi başkalarıyla paylaşılabilir?", ["En sevdiğin kitap", "Adresin", "Telefon numaran"], "En sevdiğin kitap"),
        ("Aşağıdakilerden hangisi gizli bilgi?", ["E-posta şifren", "En sevdiğin renk", "Okulun adı"], "E-posta şifren"),
        ("Aşağıdakilerden hangisi gizli bilgi değildir?", ["En sevdiğin yemek", "Okulun adı", "TC kimlik numaran"], "En sevdiğin yemek"),
        ("Aşağıdakilerden hangisi gizli bilgi?", ["Adresin", "En sevdiğin spor", "Okulun adresi"], "Adresin"),
        ("Aşağıdakilerden hangisi başkalarıyla paylaşılmamalı?", ["Telefon numaran", "En sevdiğin kitap", "Okulun adı"], "Telefon numaran"),
        ("Aşağıdakilerden hangisi gizli bilgi değildir?", ["En sevdiğin film", "Doğum tarihin", "Adresin"], "En sevdiğin film"),
        ("Aşağıdakilerden hangisi gizli bilgi?", ["Okulun adı", "E-posta şifren", "En sevdiğin yemek"], "E-posta şifren"),
        ("Aşağıdakilerden hangisi başkalarıyla paylaşılabilir?", ["En sevdiğin spor", "Adresin", "Telefon numaran"], "En sevdiğin spor"),
        ("Aşağıdakilerden hangisi gizli bilgi?", ["Doğum tarihin", "En sevdiğin oyun", "Okulun adı"], "Doğum tarihin"),
        ("Aşağıdakilerden hangisi gizli bilgi değildir?", ["En sevdiğin kitap", "Telefon numaran", "Adresin"], "En sevdiğin kitap"),
        ("Aşağıdakilerden hangisi gizli bilgi?", ["TC kimlik numaran", "En sevdiğin renk", "Okulun adı"], "TC kimlik numaran"),
        ("Aşağıdakilerden hangisi başkalarıyla paylaşılmamalı?", ["E-posta şifren", "En sevdiğin film", "Okulun adresi"], "E-posta şifren"),
        ("Aşağıdakilerden hangisi gizli bilgi değildir?", ["En sevdiğin ders", "Adresin", "Telefon numaran"], "En sevdiğin ders"),
        ("Aşağıdakilerden hangisi gizli bilgi?", ["Telefon numaran", "En sevdiğin kitap", "Okulun adı"], "Telefon numaran"),
        ("Aşağıdakilerden hangisi başkalarıyla paylaşılabilir?", ["En sevdiğin yemek", "Adresin", "Doğum tarihin"], "En sevdiğin yemek"),
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
        win.title('Bilgi Avcısı')
        win.state('zoomed')
        if kullanici_adi is not None and puan is not None:
            profil = tk.Frame(win, bg="#1e355e", bd=0, highlightthickness=0)
            profil.place(relx=0.5, rely=0.08, anchor="center", width=320, height=40)
            tk.Label(profil, text=f"👤 {kullanici_adi}   ⭐ Puan: {puan}", font=("Segoe UI", 13, "bold"), bg="#1e355e", fg="white").pack()
        card = tk.Frame(win, bg="white", bd=0, highlightthickness=0)
        card.place(relx=0.5, rely=0.5, anchor="center", width=900, height=700)
        icon = tk.Label(card, text="🕵️", font=("Segoe UI", 38), bg="white")
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
    bilgi_avcisi_oyna() 