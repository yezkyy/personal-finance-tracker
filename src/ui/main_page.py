import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import Calendar
from src.finance import add_transaction
from src.ui.report_page import ReportPage  # Import ReportPage
from src.ui.reminder_page import ReminderPage

class MainPage:
    def __init__(self, root):
        self.root = root
        self.root.title("Personal Finance Tracker")
        self.root.geometry("900x650")  # Menentukan ukuran window agar lebih konsisten
        self.root.config(bg="#F1F0E8")  # Background utama
        self.root.attributes("-fullscreen", True)  # Fullscreen saat program berjalan
        self.root.bind("<Escape>", self.exit_fullscreen)  # Exit fullscreen with 'Escape'

        # Frame navigasi atas
        self.nav_frame = tk.Frame(self.root, bg="#89A8B2", height=60)
        self.nav_frame.pack(fill=tk.X, side=tk.TOP)

        # Judul aplikasi
        self.title_label = tk.Label(
            self.nav_frame, text="Personal Finance Tracker",
            fg="white", bg="#89A8B2", font=("Arial", 18, "bold")
        )
        self.title_label.grid(row=0, column=0, padx=20, pady=10)

        # Frame untuk tombol navigasi
        self.nav_buttons_frame = tk.Frame(self.nav_frame, bg="#89A8B2")
        self.nav_buttons_frame.grid(row=0, column=1, padx=20)

        self.add_page_button = tk.Button(self.nav_buttons_frame, text="Add Transaction", command=self.show_add_page, font=("Arial", 12), bg="#B3C8CF", fg="white", relief="flat", width=18)
        self.add_page_button.grid(row=0, column=0, padx=10, pady=5)

        self.report_page_button = tk.Button(self.nav_buttons_frame, text="Report", command=self.show_report_page, font=("Arial", 12), bg="#B3C8CF", fg="white", relief="flat", width=18)
        self.report_page_button.grid(row=0, column=1, padx=10, pady=5)

        self.reminder_page_button = tk.Button(self.nav_buttons_frame, text="Reminder", command=self.show_reminder_page, font=("Arial", 12), bg="#B3C8CF", fg="white", relief="flat", width=18)
        self.reminder_page_button.grid(row=0, column=2, padx=10, pady=5)

        # Konten halaman utama
        self.main_frame = tk.Frame(self.root, bg="#F1F0E8")
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        self.show_add_page()

    def show_add_page(self):
        self.clear_main_frame()
        self.current_page = AddPage(self.main_frame)

    def show_report_page(self):
        self.clear_main_frame()
        self.current_page = ReportPage(self.main_frame)  # Menampilkan halaman ReportPage

    def show_reminder_page(self):
        self.clear_main_frame()
        self.current_page = ReminderPage(self.main_frame)  # Menampilkan halaman ReminderPage

    def clear_main_frame(self):
        # Menghapus semua widget di main_frame
        for widget in self.main_frame.winfo_children():
            widget.destroy()

    def exit_fullscreen(self, event=None):
        self.root.attributes("-fullscreen", False)


class AddPage:
    def __init__(self, root):
        self.root = root
        self.frame = tk.Frame(self.root, bg="#E5E1DA", bd=2, relief="solid")
        self.frame.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)
        self.create_form()

    def create_form(self):
        tk.Label(self.frame, text="Amount:", font=("Helvetica", 12), bg="#E5E1DA").grid(row=0, column=0, padx=15, pady=10, sticky=tk.W)
        self.amount_entry = tk.Entry(self.frame, width=30, font=("Helvetica", 12))
        self.amount_entry.grid(row=0, column=1, padx=15, pady=10)

        tk.Label(self.frame, text="Category:", font=("Helvetica", 12), bg="#E5E1DA").grid(row=1, column=0, padx=15, pady=10, sticky=tk.W)
        self.category_entry = tk.Entry(self.frame, width=30, font=("Helvetica", 12))
        self.category_entry.grid(row=1, column=1, padx=15, pady=10)

        tk.Label(self.frame, text="Date:", font=("Helvetica", 12), bg="#E5E1DA").grid(row=2, column=0, padx=15, pady=10, sticky=tk.W)
        self.date_button = tk.Button(self.frame, text="Select Date", command=self.show_calendar, width=20, font=("Helvetica", 12), bg="#3498DB", fg="white")
        self.date_button.grid(row=2, column=1, padx=15, pady=10)

        self.selected_date_label = tk.Label(self.frame, text="No date selected", font=("Helvetica", 12), bg="#E5E1DA")
        self.selected_date_label.grid(row=3, column=0, columnspan=2, pady=10)

        tk.Label(self.frame, text="Type:", font=("Helvetica", 12), bg="#E5E1DA").grid(row=4, column=0, padx=15, pady=10, sticky=tk.W)
        self.type_var = tk.StringVar()
        self.type_combobox = ttk.Combobox(self.frame, textvariable=self.type_var, values=["income", "expense"], state="readonly", width=28, font=("Helvetica", 12))
        self.type_combobox.grid(row=4, column=1, padx=15, pady=10)
        self.type_combobox.set("income")

        self.add_button = tk.Button(self.frame, text="Add Transaction", command=self.add_transaction, bg="#27AE60", fg="white", font=("Helvetica", 12, "bold"), relief="flat")
        self.add_button.grid(row=5, column=0, columnspan=2, pady=20)

    def show_calendar(self):
        self.calendar_window = tk.Toplevel(self.root)
        self.calendar_window.title("Select Date")
        self.calendar_window.geometry("250x250")

        self.calendar = Calendar(self.calendar_window, selectmode="day", date_pattern="yyyy-mm-dd")
        self.calendar.pack(pady=20)

        self.select_date_button = tk.Button(self.calendar_window, text="Select", command=self.select_date, bg="#2980B9", fg="white")
        self.select_date_button.pack()

    def select_date(self):
        selected_date = self.calendar.get_date()
        self.selected_date_label.config(text=f"Selected Date: {selected_date}")
        self.calendar_window.destroy()

    def add_transaction(self):
        try:
            amount = self.amount_entry.get()
            category = self.category_entry.get()
            date = self.selected_date_label.cget("text").replace("Selected Date: ", "")
            transaction_type = self.type_var.get()

            if not amount or not category or not date or not transaction_type:
                raise ValueError("All fields are required.")

            amount = float(amount)
            if amount <= 0:
                raise ValueError("Amount must be greater than 0.")

            if transaction_type not in ["income", "expense"]:
                raise ValueError("Transaction type must be 'income' or 'expense'.")

            add_transaction(amount, category, date, transaction_type)
            messagebox.showinfo("Success", "Transaction added successfully.")
            self.clear_form()
        except ValueError as e:
            messagebox.showerror("Input Error", str(e))

    def clear_form(self):
        self.amount_entry.delete(0, tk.END)
        self.category_entry.delete(0, tk.END)
        self.selected_date_label.config(text="No date selected")
        self.type_combobox.set("income")