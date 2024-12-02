import tkinter as tk
from tkinter import messagebox
from src.reminder import check_due_bills

class ReminderPage:
    def __init__(self, root):
        tk.Label(root, text="Upcoming Bills and Reminders", font=("Helvetica", 14, "bold")).pack(pady=20)

        self.reminder_button = tk.Button(
            root, text="Check Due Bills", command=self.show_reminders,
            bg="#F1C40F", fg="black", font=("Helvetica", 12, "bold"), relief="flat", bd=2
        )
        self.reminder_button.pack(pady=10)

        self.reminder_listbox = tk.Listbox(root, width=50, height=10, font=("Helvetica", 12), selectmode=tk.SINGLE, relief="flat")
        self.reminder_listbox.pack(pady=10)

    def show_reminders(self):
        due_bills = check_due_bills()
        self.reminder_listbox.delete(0, tk.END)

        if due_bills:
            for bill in due_bills:
                self.reminder_listbox.insert(tk.END, f"{bill[0]} (Due: {bill[1]})")
        else:
            messagebox.showinfo("No Bills", "No bills are currently due!")