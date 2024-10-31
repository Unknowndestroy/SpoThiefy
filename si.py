import customtkinter as ctk
import itertools
from tkinter import messagebox
import os

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

class SpotifyMateApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.title("SpoThiefy")
        self.geometry("500x300")

        # Arka plan renkleri ve geçiş hızı
        self.colors = itertools.cycle(["#FF5733", "#33FF57", "#3357FF", "#F333FF"])
        self.current_color = next(self.colors)
        self.configure(bg=self.current_color)
        self.animate_background()

        # Sağ üstte dil seçme menüsü
        self.language_var = ctk.StringVar(value="🌐 Türkçe")
        self.language_menu = ctk.CTkOptionMenu(
            self, values=["🌐 Türkçe", "🌐 İngilizce", "🌐 Rusça", "🌐 Ukraynaca"],
            variable=self.language_var, width=150, anchor="e", command=self.change_language
        )
        self.language_menu.place(relx=0.98, rely=0.05, anchor="ne")

        # URL giriş alanı
        self.url_label = ctk.CTkLabel(self, text="Spotify URL:", font=("Arial", 14))
        self.url_label.place(relx=0.1, rely=0.25)
        self.url_entry = ctk.CTkEntry(self, width=300)
        self.url_entry.place(relx=0.5, rely=0.35, anchor="center")

        # İndir butonu
        self.download_button = ctk.CTkButton(self, text="İndir", command=self.download_song)
        self.download_button.place(relx=0.5, rely=0.5, anchor="center")
        
        # Buton animasyonu
        self.blink_download_button()

    def animate_background(self):
        """Smooth geçişle arka plan rengini değiştirme."""
        self.current_color = next(self.colors)
        self.configure(bg=self.current_color)
        self.after(1000, self.animate_background)  # 1 saniyede bir arka plan rengi değişir

    def blink_download_button(self):
        """Butonun arka plan rengini 2 saniyede bir değiştiren animasyon."""
        current_color = "green" if self.download_button.cget("fg_color") == "blue" else "blue"
        self.download_button.configure(fg_color=current_color)
        self.after(2000, self.blink_download_button)  # 2 saniyede bir buton rengi değişir

    def change_language(self, choice):
        """Dil değiştirme fonksiyonu."""
        if choice == "🌐 Türkçe":
            self.download_button.configure(text="İndir")
            self.url_label.configure(text="Spotify URL:")
        elif choice == "🌐 İngilizce":
            self.download_button.configure(text="Download")
            self.url_label.configure(text="Spotify URL:")
        elif choice == "🌐 Rusça":
            self.download_button.configure(text="Скачать")
            self.url_label.configure(text="Ссылка Spotify:")
        elif choice == "🌐 Ukraynaca":
            self.download_button.configure(text="Завантажити")
            self.url_label.configure(text="Посилання Spotify:")

    def download_song(self):
        """Spotify şarkısını indirme fonksiyonu."""
        url = self.url_entry.get()
    
        if "/track/" in url or "/playlist/" in url:
            os.system(f"spotdl {url}")
            messagebox.showinfo("İndirme", "İndirme tamamlandı!")
        else:
            messagebox.showerror("Hata", "Geçerli bir Spotify bağlantısı girin.")

if __name__ == "__main__":
    app = SpotifyMateApp()
    app.mainloop()
