import tkinter as tk
from tkinter import messagebox
from src.finance import add_transaction

class FinanceApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Personal Finance Tracker")

        self.amount_label = tk.Label(root, text="Amount:")
        self.amount_label.grid(row=0, column=0)
        self.amount_entry = tk.Entry(root)
        self.amount_entry.grid(row=0, column=1)

        self.category_label = tk.Label(root, text="Category:")
        self.category_label.grid(row=1, column=0)
        self.category_entry = tk.Entry(root)
        self.category_entry.grid(row=1, column=1)

        self.date_label = tk.Label(root, text="Date:")
        self.date_label.grid(row=2, column=0)
        self.date_entry = tk.Entry(root)
        self.date_entry.grid(row=2, column=1)

        self.type_label = tk.Label(root, text="Type (income/expense):")
        self.type_label.grid(row=3, column=0)
        self.type_entry = tk.Entry(root)
        self.type_entry.grid(row=3, column=1)

        self.add_button = tk.Button(root, text="Add Transaction", command=self.add_transaction)
        self.add_button.grid(row=4, column=0, columnspan=2)

    def add_transaction(self):
        amount = float(self.amount_entry.get())
        category = self.category_entry.get()
        date = self.date_entry.get()
        transaction_type = self.type_entry.get()
        
        if transaction_type not in ['income', 'expense']:
            messagebox.showerror("Error", "Transaction type must be 'income' or 'expense'")
        else:
            add_transaction(amount, category, date, transaction_type)
            messagebox.showinfo("Success", "Transaction added successfully")
