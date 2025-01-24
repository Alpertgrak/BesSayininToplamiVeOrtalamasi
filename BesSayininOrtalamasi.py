import tkinter as tk
from tkinter import messagebox
class BesSayiApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Beş Sayının Toplamı ve Ortalaması Hesabı")

        # Pencere boyutlarını sabitliyoruz (örneğin 300x200)
        self.root.geometry("300x400")
        self.root.resizable(False, False)  # Pencereyi yeniden boyutlandırmayı kapatıyoruz

        # Sayı Girişi
        self.s1_label = tk.Label(root, text="1. Sayıyı Girin:")
        self.s1_label.grid(row=0, column=0, padx=10, pady=10)

        self.s1_entry = tk.Entry(root)
        self.s1_entry.grid(row=0, column=1, padx=10, pady=5)

        self.s2_label = tk.Label(root, text="2. Sayıyı Girin:")
        self.s2_label.grid(row=1, column=0, padx=10, pady=10)

        self.s2_entry = tk.Entry(root)
        self.s2_entry.grid(row=1, column=1, padx=10, pady=5)

        self.s3_label = tk.Label(root, text="3. Sayıyı Girin:")
        self.s3_label.grid(row=2, column=0, padx=10, pady=10)

        self.s3_entry = tk.Entry(root)
        self.s3_entry.grid(row=2, column=1, padx=10, pady=5)

        self.s4_label = tk.Label(root, text="4. Sayıyı Girin:")
        self.s4_label.grid(row=3, column=0, padx=10, pady=10)

        self.s4_entry = tk.Entry(root)
        self.s4_entry.grid(row=3, column=1, padx=10, pady=5)

        self.s5_label = tk.Label(root, text="5. Sayıyı Girin:")
        self.s5_label.grid(row=4, column=0, padx=10, pady=10)

        self.s5_entry = tk.Entry(root)
        self.s5_entry.grid(row=4, column=1, padx=10, pady=5)

        # Buton
        self.hesapla_button = tk.Button(root, text="Hesapla", command=self.TopOrtHesapla)
        self.hesapla_button.grid(row=5, column=0, padx=10, pady=10)

        # Sonuç Etiketi
        self.Toplam_label = tk.Label(root, text="")
        self.Toplam_label.grid(row=6, column=0, padx=10, pady=10)

        self.Ortalama_label = tk.Label(root, text="")
        self.Ortalama_label.grid(row=7, column=0, padx=10, pady=10)

    def TopOrtHesapla(self):
        try:
             a1= int(self.s1_entry.get())  # s1 değerini alıyoruz.
             a2 = int(self.s2_entry.get())  # s2 değerini alıyoruz.
             a3= int(self.s3_entry.get())  # s3 değerini alıyoruz.
             a4 = int(self.s4_entry.get())  # s4 değerini alıyoruz.
             a5= int(self.s5_entry.get())  # s5 değerini alıyoruz.

             Toplam=a1+a2+a3+a4+a5
             Ortalama=Toplam/5

             # Sonucu gösterme
             self.Toplam_label.config(text=f"Toplam: {Toplam}")
             self.Ortalama_label.config(text=f"Ortalama:: {Ortalama}")


        except ValueError:
            # Eğer değer sayısal değilse uyarı mesajı
            messagebox.showerror("Hatalı Giriş", "Lütfen geçerli bir değer girin.")


# Tkinter arayüzünü başlatma
if __name__ == "__main__":
    root = tk.Tk()
    app = BesSayiApp(root)
    root.mainloop()
