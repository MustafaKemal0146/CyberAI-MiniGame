import tkinter as tk
from tkinter import messagebox
import random

def kamera_canavari_oyna(parent=None, kullanici_adi=None, puan=None):
    sorular = [
        ("Kameranı açmadan önce ne yapmalısın?", ["Direkt açarım, sonra bakarım", "Önce etrafa bakarım ve gerekliyse açarım", "Kameramı açmadan önce bilgisayarı yeniden başlatırım"], "Önce etrafa bakarım ve gerekliyse açarım"),
        ("Kameranı kimlerle paylaşabilirsin?", ["Kimseyle", "Ailemle ve öğretmenimle", "Güvendiğim arkadaşlarımla"], "Kimseyle"),
        ("Kameranı kullanmadığında ne yapmalısın?", ["Kapatırım veya örterim", "Kamerayı aşağıya çeviririm", "Kamerayı açık bırakırım"], "Kapatırım veya örterim"),
        ("Kameranı açarken nelere dikkat etmelisin?", ["Etrafımda kimse var mı", "Kıyafetim uygun mu", "Hepsi"], "Hepsi"),
        ("Kameranı açmadan önce odanı nasıl bırakmalısın?", ["Düzenli ve sade", "Kameranın açısını değiştiririm", "Dağınık bırakırım"], "Düzenli ve sade"),
        ("Kameranı açarken hangi uygulamalara izin vermelisin?", ["Güvendiğim uygulamalara", "Tüm uygulamalara", "Sadece oyunlara"], "Güvendiğim uygulamalara"),
        ("Kameranı açarken hangi ortamda olmalısın?", ["Güvenli ve özel bir ortamda", "Kalabalık bir ortamda", "Her yerde açabilirim"], "Güvenli ve özel bir ortamda"),
        ("Kameranı açmadan önce ne yapmalısın?", ["Etrafı kontrol etmeliyim", "Kamerayı açıp sonra bakarım", "Kamerayı açmam"], "Etrafı kontrol etmeliyim"),
        ("Kameranı açarken hangi davranış yanlıştır?", ["Kamerayı açık bırakmak", "Kullanmadığımda kapatmak", "Kamerayı sadece derste açmak"], "Kamerayı açık bırakmak"),
        ("Kameranı açarken hangi uygulamaya izin vermemelisin?", ["Bilinmeyen uygulama", "Güvendiğim uygulama", "Okul uygulaması"], "Bilinmeyen uygulama"),
        ("Kameranı açarken hangi bilgi paylaşılmamalı?", ["Ev adresi", "Okulun adı", "Sadece adım"], "Ev adresi"),
        ("Kameranı açarken hangi davranış doğrudur?", ["Kullanmadığımda kapatmak", "Kamerayı açık bırakmak", "Kamerayı bantlamak"], "Kullanmadığımda kapatmak"),
        ("Kameranı açarken hangi davranış yanlıştır?", ["Kamerayı örterim", "Kamerayı açık bırakırım", "Kamerayı kapatırım"], "Kamerayı açık bırakırım"),
        ("Kameranı açarken hangi uygulamaya izin vermelisin?", ["Güvendiğim uygulama", "Bilinmeyen uygulama", "Sosyal medya uygulaması"], "Güvendiğim uygulama"),
        ("Kameranı açarken hangi bilgi paylaşılmamalı?", ["Telefon numarası", "Sadece adım", "Okulun adı"], "Telefon numarası"),
        ("Kameranı açarken hangi davranış doğrudur?", ["Kullanmadığımda kapatmak", "Kamerayı açık bırakmak", "Kamerayı bantlamak"], "Kullanmadığımda kapatmak"),
        ("Kameranı açarken hangi davranış yanlıştır?", ["Kamerayı örterim", "Kamerayı açık bırakırım", "Kamerayı kapatırım"], "Kamerayı açık bırakırım"),
        ("Kameranı açarken hangi uygulamaya izin vermelisin?", ["Güvendiğim uygulama", "Bilinmeyen uygulama", "Sadece oyunlar"], "Güvendiğim uygulama"),
        ("Kameranı açarken hangi bilgi paylaşılmamalı?", ["Ev adresi", "Okulun adı", "Sadece adım"], "Ev adresi"),
        ("Kameranı açarken hangi davranış doğrudur?", ["Kullanmadığımda kapatmak", "Kamerayı açık bırakmak", "Kamerayı bantlamak"], "Kullanmadığımda kapatmak"),
        ("Kameranı açarken hangi davranış yanlıştır?", ["Kamerayı örterim", "Kamerayı açık bırakırım", "Kamerayı kapatırım"], "Kamerayı açık bırakırım"),
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
        win.title('Kamera Canavarı')
        win.state('zoomed')
        if kullanici_adi is not None and puan is not None:
            profil = tk.Frame(win, bg="#1e355e", bd=0, highlightthickness=0)
            profil.place(relx=0.5, rely=0.08, anchor="center", width=320, height=40)
            tk.Label(profil, text=f"👤 {kullanici_adi}   ⭐ Puan: {puan}", font=("Segoe UI", 13, "bold"), bg="#1e355e", fg="white").pack()
        card = tk.Frame(win, bg="white", bd=0, highlightthickness=0)
        card.place(relx=0.5, rely=0.5, anchor="center", width=900, height=700)
        icon = tk.Label(card, text="📷", font=("Segoe UI", 38), bg="white")
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
    kamera_canavari_oyna() 