from src.ui.main_page import MainPage
from src.finance import create_db
import tkinter as tk

if __name__ == "__main__":
    create_db()

    # Membuat jendela Tkinter
    root = tk.Tk()
    
    # Membuat objek aplikasi
    app = MainPage(root)
    
    # Menjalankan aplikasi
    root.mainloop()