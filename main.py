import tkinter as tk
from tkinter import messagebox, simpledialog, Toplevel, Canvas, Label, PhotoImage
from parola_dedektifi import parola_dedektifi_oyna
from kamera_canavari import kamera_canavari_oyna
from bilgi_avcisi import bilgi_avcisi_oyna
from uygulama_dedektifi import uygulama_dedektifi_oyna
from wifi_tehlikesi import wifi_tehlikesi_oyna
import os
import datetime
import webbrowser

STAND_ISMI = "Siber Güvenlik Standı 2025"
LOGO_PATH = "logo.jpg"
SKOR_DOSYASI = "skorlar.txt"
ROZETLER = {
    5: ("Altın Rozet", "#FFD700"),
    4: ("Gümüş Rozet", "#C0C0C0"),
    3: ("Gümüş Rozet", "#C0C0C0"),
    2: ("Bronz Rozet", "#CD7F32"),
    1: ("Bronz Rozet", "#CD7F32"),
    0: ("Teşekkürler", "#B0B0B0")
}

def rozet_animasyon(mesaj, renk, parent=None):
    win = Toplevel(parent)
    win.title("Rozet Kazandın!")
    win.state('zoomed')
    win.configure(bg="white")
    win.update_idletasks()
    width = win.winfo_screenwidth()
    height = win.winfo_screenheight()
    c = Canvas(win, width=width, height=height, bg="white", highlightthickness=0)
    c.place(relx=0.5, rely=0.5, anchor="center")
    center_x = width // 2
    center_y = height // 2 - 60
    for r in range(40, 200, 12):
        c.delete("all")
        c.create_oval(center_x - r, center_y - r, center_x + r, center_y + r, fill=renk, outline=renk)
        win.update()
        win.after(12)
    c.create_oval(center_x - 120, center_y - 120, center_x + 120, center_y + 120, fill=renk, outline=renk)
    c.create_text(center_x, center_y, text=mesaj, font=("Arial", 48, "bold"), fill="black")
    c.create_text(center_x, center_y + 80, text=f"{mesaj} kazandın!", font=("Arial", 32), fill="#1e355e")
    win.after(1600, win.destroy)
    parent.wait_window(win)

def skor_kaydet(isim, puan):
    try:
        with open(SKOR_DOSYASI, 'a', encoding='utf-8') as f:
            f.write(f"{isim},{puan}\n")
    except Exception as e:
        print(f"Skor kaydedilemedi: {e}")

def skor_tablosu_goster():
    skorlar = []
    if os.path.exists(SKOR_DOSYASI):
        with open(SKOR_DOSYASI, 'r', encoding='utf-8') as f:
            for satir in f:
                parca = satir.strip().split(',')
                if len(parca) == 2:
                    isim, puan = parca
                    try:
                        puan = int(puan)
                        skorlar.append((isim, puan))
                    except:
                        continue
    skorlar.sort(key=lambda x: x[1], reverse=True)
    ilk10 = skorlar[:10]
    tablo = "En İyi 10 Siber Kahraman:\n\n"
    for i, (isim, puan) in enumerate(ilk10, 1):
        tablo += f"{i}. {isim} - {puan} puan\n"
    root = tk.Tk()
    root.state('zoomed')
    root.withdraw()
    messagebox.showinfo('Skor Tablosu', tablo)
    root.destroy()

def sertifika_olustur(isim, puan, rozet_adi):
    try:
        from reportlab.lib.pagesizes import A4
        from reportlab.pdfgen import canvas
        from reportlab.lib.utils import ImageReader
        from reportlab.lib import colors
        from reportlab.pdfbase import pdfmetrics
        from reportlab.pdfbase.ttfonts import TTFont
    except ImportError as e:
        messagebox.showerror('Eksik Paket', f'Sertifika için reportlab kütüphanesi gerekli!\nTerminalde: pip install reportlab\n\nHata: {e}')
        return
    import traceback
    try:
        font_path = 'DejaVuSans.ttf'
        if not os.path.exists(font_path):
            messagebox.showerror('Font Eksik', 'DejaVuSans.ttf dosyasını proje klasörüne ekleyin!')
            return
        pdfmetrics.registerFont(TTFont('DejaVu', font_path))
        tarih = datetime.datetime.now().strftime('%d.%m.%Y')
        dosya_adi = f"SiberKahramanSertifika_{isim}.pdf"
        c = canvas.Canvas(dosya_adi, pagesize=A4)
        width, height = A4
        c.setStrokeColor(colors.HexColor('#1e90ff'))
        c.setLineWidth(8)
        c.rect(30, 30, width-60, height-60)
        if os.path.exists(LOGO_PATH):
            try:
                logo = ImageReader(LOGO_PATH)
                logo_width = 120
                logo_height = 120
                c.drawImage(logo, (width-logo_width)/2, height-150, width=logo_width, height=logo_height, mask='auto')
            except Exception as e:
                print(f"Logo eklenemedi: {e}")
        c.setFont("DejaVu", 18)
        c.drawCentredString(width/2, height-180, STAND_ISMI)
        c.setFont("DejaVu", 24)
        c.drawCentredString(width/2, height-230, "Siber Kahraman Sertifikası")
        c.setFont("DejaVu", 16)
        c.drawCentredString(width/2, height-280, f"Tebrikler {isim}!")
        c.drawCentredString(width/2, height-310, f"Toplam Puan: {puan}/15")
        c.setFont("DejaVu", 16)
        c.drawCentredString(width/2, height-340, f"{rozet_adi}")
        c.setFont("DejaVu", 12)
        c.drawCentredString(width/2, height-370, f"Tarih: {tarih}")
        c.drawCentredString(width/2, height-390, "Tüm görevleri başarıyla tamamladın.")
        c.drawCentredString(width/2, height-410, "Siber dünyada artık daha güvendesin!")
        c.setFont("DejaVu", 12)
        c.drawString(60, 60, "Stand Görevlisi: _______________")
        c.drawRightString(width-60, 60, "Tebrikler! :)")
        c.save()
        messagebox.showinfo('Sertifika Oluşturuldu', f'Sertifikan hazır!\n{dosya_adi} dosyasını bulabilirsin.')
        try:
            webbrowser.open_new(dosya_adi)
        except Exception as e:
            messagebox.showerror('Sertifika Açma Hatası', f'Sertifika açılırken hata oluştu:\n{e}')
    except Exception as e:
        hata_detayi = traceback.format_exc()
        messagebox.showerror('Sertifika Oluşturma Hatası', f'Sertifika oluşturulurken bir hata oluştu:\n{e}\n\nDetay:\n{hata_detayi}')

def isim_giris_ekrani(parent):
    win = Toplevel(parent)
    win.title('Oyuncu Adı')
    win.state('zoomed')
    win.configure(bg='#e3f0ff')
    win.grab_set()
    width = win.winfo_screenwidth()
    height = win.winfo_screenheight()
    frame = tk.Frame(win, bg='white', bd=0, highlightthickness=0)
    frame.place(relx=0.5, rely=0.5, anchor='center', width=600, height=340)
    baslik = tk.Label(frame, text='Adını Gir', font=('Segoe UI', 36, 'bold'), bg='white', fg='#1e355e')
    baslik.pack(pady=(40, 20))
    entry = tk.Entry(frame, font=('Segoe UI', 28), justify='center', bd=2, relief='solid', width=18)
    entry.pack(pady=(0, 30), ipady=12)
    entry.focus_set()
    sonuc = {'isim': None}
    def onayla():
        isim = entry.get().strip()
        if isim:
            sonuc['isim'] = isim
            win.destroy()
        else:
            messagebox.showwarning('Uyarı', 'Lütfen adını gir!', parent=win)
    onay_btn = tk.Button(frame, text='Başla', font=('Segoe UI', 24, 'bold'), bg='#1e90ff', fg='white', activebackground='#63b3ed', activeforeground='white', relief='flat', bd=0, highlightthickness=0, padx=24, pady=10, command=onayla, cursor='hand2')
    onay_btn.pack(pady=(0, 10))
    win.bind('<Return>', lambda e: onayla())
    parent.wait_window(win)
    return sonuc['isim']

def istasyonlari_baslat():
    root = tk.Tk()
    root.state('zoomed')
    root.withdraw()
    isim = None
    while not isim:
        isim = isim_giris_ekrani(root)
        if isim is None or isim.strip() == "":
            if messagebox.askyesno('Çıkış', 'Ad girmeden oyun başlatılamaz. Çıkmak istiyor musun?', parent=root):
                return
            else:
                isim = None
    puan = 0
    istasyonlar = [
        (lambda: parola_dedektifi_oyna(root), 'Parola Dedektifi'),
        (lambda: kamera_canavari_oyna(root), 'Kamera Canavarı'),
        (lambda: bilgi_avcisi_oyna(root), 'Bilgi Avcısı'),
        (lambda: uygulama_dedektifi_oyna(root), 'Uygulama Dedektifi'),
        (lambda: wifi_tehlikesi_oyna(root), 'Wi-Fi Tehlikesi'),
    ]
    for fonk, ad in istasyonlar:
        sonuc = fonk()
        root.update()
        if sonuc == -1:
            # Tam ekran büyük sonuç ekranı
            son_win = tk.Toplevel(root)
            son_win.title('Kaybettin')
            son_win.state('zoomed')
            son_win.configure(bg='#f8eaea')
            frame = tk.Frame(son_win, bg='white', bd=0, highlightthickness=0)
            frame.place(relx=0.5, rely=0.5, anchor='center', width=900, height=480)
            baslik = tk.Label(frame, text='KAYBETTİN', font=('Segoe UI', 54, 'bold'), bg='white', fg='#d32f2f')
            baslik.pack(pady=(40, 20))
            aciklama = tk.Label(frame, text='Bir soruda yanlış yaptın ve oyunu kaybettin.', font=('Segoe UI', 28), bg='white', fg='#1e355e', wraplength=800)
            aciklama.pack(pady=(0, 24))
            kapat_btn = tk.Button(frame, text='Kapat', font=('Segoe UI', 22, 'bold'), bg='#d32f2f', fg='white', activebackground='#e57373', activeforeground='white', relief='flat', bd=0, highlightthickness=0, padx=32, pady=12, command=root.quit, cursor='hand2')
            kapat_btn.pack(pady=(30, 0))
            root.wait_window(son_win)
            root.quit()
            return
        if sonuc == 3:
            puan += 3
            rozet_animasyon("Rozet!", "#1e90ff", parent=root)
        else:
            puan += sonuc
    rozet_adi, rozet_renk = ROZETLER.get(puan//3, ("Teşekkürler", "#B0B0B0"))
    rozet_animasyon(rozet_adi, rozet_renk, parent=root)
    messagebox.showinfo('Sonuç', f'Tebrikler {isim}!\nToplam Puan: {puan}/15\nKazandığın Rozet: {rozet_adi}', parent=root)
    skor_kaydet(isim, puan)
    sertifika_olustur(isim, puan, rozet_adi)
    skor_tablosu_goster()
    root.destroy()

if __name__ == '__main__':
    istasyonlari_baslat() 