import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import Calendar
from src.finance import add_transaction

class MainPage:
    def __init__(self, root):
        self.root = root
        self.root.title("Personal Finance Tracker")
        self.root.geometry("800x600")  # Menentukan ukuran window agar lebih konsisten
        self.root.config(bg="#F1F0E8")  # Background utama
        self.root.bind("<Escape>", self.exit_fullscreen)  # Exit fullscreen with 'Escape'

        # Frame navigasi di atas
        self.nav_frame = tk.Frame(self.root, bg="#89A8B2", height=50)
        self.nav_frame.pack(fill=tk.X, side=tk.TOP)

        self.title_label = tk.Label(
            self.nav_frame, text="Personal Finance Tracker",
            fg="white", bg="#89A8B2", font=("Arial", 16, "bold")
        )
        self.title_label.pack(pady=10)

        # Konten halaman
        self.main_frame = tk.Frame(self.root, bg="#F1F0E8")
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        self.show_add_page()

    def show_add_page(self):
        self.clear_main_frame()
        self.current_page = AddPage(self.main_frame)

    def clear_main_frame(self):
        # Menghapus semua widget di main_frame
        for widget in self.main_frame.winfo_children():
            widget.destroy()

    def exit_fullscreen(self, event=None):
        self.root.attributes("-fullscreen", False)

class AddPage:
    def __init__(self, root):
        self.root = root
        
        # Menggunakan Frame untuk penataan yang lebih rapi
        self.frame = tk.Frame(self.root, bg="#E5E1DA", bd=2, relief="solid")
        self.frame.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)

        self.create_form()

    def create_form(self):
        # Label dan input untuk jumlah uang
        tk.Label(self.frame, text="Amount:", font=("Helvetica", 12), bg="#E5E1DA").grid(row=0, column=0, padx=15, pady=10, sticky=tk.W)
        self.amount_entry = tk.Entry(self.frame, width=30, font=("Helvetica", 12))
        self.amount_entry.grid(row=0, column=1, padx=15, pady=10)

        # Label dan input untuk kategori
        tk.Label(self.frame, text="Category:", font=("Helvetica", 12), bg="#E5E1DA").grid(row=1, column=0, padx=15, pady=10, sticky=tk.W)
        self.category_entry = tk.Entry(self.frame, width=30, font=("Helvetica", 12))
        self.category_entry.grid(row=1, column=1, padx=15, pady=10)

        # Label dan tombol untuk memilih tanggal
        tk.Label(self.frame, text="Date:", font=("Helvetica", 12), bg="#E5E1DA").grid(row=2, column=0, padx=15, pady=10, sticky=tk.W)
        self.date_button = tk.Button(self.frame, text="Select Date", command=self.show_calendar, width=20, font=("Helvetica", 12), bg="#3498DB", fg="white")
        self.date_button.grid(row=2, column=1, padx=15, pady=10)

        self.selected_date_label = tk.Label(self.frame, text="No date selected", font=("Helvetica", 12), bg="#E5E1DA")
        self.selected_date_label.grid(row=3, column=0, columnspan=2, pady=10)

        # Label dan combobox untuk memilih tipe transaksi
        tk.Label(self.frame, text="Type:", font=("Helvetica", 12), bg="#E5E1DA").grid(row=4, column=0, padx=15, pady=10, sticky=tk.W)
        self.type_var = tk.StringVar()
        self.type_combobox = ttk.Combobox(self.frame, textvariable=self.type_var, values=["Income", "Expense"], state="readonly", width=28, font=("Helvetica", 12))
        self.type_combobox.grid(row=4, column=1, padx=15, pady=10)
        self.type_combobox.set("Income")

        # Tombol untuk menambahkan transaksi
        self.add_button = tk.Button(self.frame, text="Add Transaction", command=self.add_transaction, bg="#27AE60", fg="white", font=("Helvetica", 12, "bold"), relief="flat")
        self.add_button.grid(row=5, column=0, columnspan=2, pady=20)

    def show_calendar(self):
        # Membuka kalender di popup (Toplevel)
        self.calendar_window = tk.Toplevel(self.root)
        self.calendar_window.title("Select Date")
        self.calendar_window.geometry("250x250")

        self.calendar = Calendar(self.calendar_window, selectmode="day", date_pattern="yyyy-mm-dd")
        self.calendar.pack(pady=20)

        # Tombol untuk memilih tanggal
        self.select_date_button = tk.Button(self.calendar_window, text="Select", command=self.select_date, bg="#2980B9", fg="white")
        self.select_date_button.pack()

    def select_date(self):
        selected_date = self.calendar.get_date()
        self.selected_date_label.config(text=f"Selected Date: {selected_date}")
        self.calendar_window.destroy()

    def add_transaction(self):
        try:
            # Ambil data dari input
            amount = self.amount_entry.get()
            category = self.category_entry.get()
            date = self.selected_date_label.cget("text").replace("Selected Date: ", "")
            transaction_type = self.type_var.get()

            # Validasi input kosong
            if not amount or not category or not date or not transaction_type:
                raise ValueError("All fields are required.")

            # Validasi jumlah (harus berupa angka positif)
            amount = float(amount)
            if amount <= 0:
                raise ValueError("Amount must be greater than 0.")

            # Validasi tipe transaksi
            if transaction_type not in ["income", "expense"]:
                raise ValueError("Transaction type must be 'income' or 'expense'.")

            # Panggil fungsi add_transaction dari src/finance.py
            add_transaction(amount, category, date, transaction_type)

            # Tampilkan pesan sukses
            messagebox.showinfo("Success", "Transaction added successfully!")
            self.clear_entries()

        except ValueError as e:
            # Tampilkan pesan error
            messagebox.showerror("Error", str(e))

    def clear_entries(self):
        self.amount_entry.delete(0, tk.END)
        self.category_entry.delete(0, tk.END)
        self.selected_date_label.config(text="No date selected")
        self.type_combobox.set("income")