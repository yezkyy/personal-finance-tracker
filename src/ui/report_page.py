import tkinter as tk
from tkinter import Toplevel
from src.finance import generate_report
from src.report import plot_expenses

class ReportPage:
    def __init__(self, root):
        self.root = root
        self.create_report_page()

    def create_report_page(self):
        tk.Label(self.root, text="Generate Financial Report", font=("Helvetica", 14, "bold"), bg="#F1F0E8").grid(row=0, column=0, pady=20)

        # Button for showing report
        self.report_button = tk.Button(
            self.root, text="Show Report", command=self.open_report_window,
            bg="#89A8B2", fg="white", font=("Helvetica", 12, "bold"), relief="flat", bd=2
        )
        self.report_button.grid(row=1, column=0, pady=10, padx=20, sticky="ew")

        # Button for viewing chart
        self.chart_button = tk.Button(
            self.root, text="View Expense Chart", command=plot_expenses,
            bg="#B3C8CF", fg="white", font=("Helvetica", 12, "bold"), relief="flat", bd=2
        )
        self.chart_button.grid(row=2, column=0, pady=10, padx=20, sticky="ew")

        # Back button
        self.back_button = tk.Button(
            self.root, text="Back", command=self.back,
            bg="#E5E1DA", fg="black", font=("Helvetica", 12, "bold"), relief="flat", bd=2
        )
        self.back_button.grid(row=3, column=0, pady=20, padx=20, sticky="ew")

    def open_report_window(self):
        report_window = Toplevel()
        report_window.title("Financial Report")
        report_window.geometry("600x400")

        report = generate_report()
        tk.Label(report_window, text="Financial Report", font=("Helvetica", 16, "bold")).grid(row=0, column=0, pady=10)

        tk.Label(report_window, text=f"Total Income: {report['total_income']}", font=("Helvetica", 12)).grid(row=1, column=0, pady=5)
        tk.Label(report_window, text=f"Total Expense: {report['total_expense']}", font=("Helvetica", 12)).grid(row=2, column=0, pady=5)
        tk.Label(report_window, text=f"Balance: {report['balance']}", font=("Helvetica", 12)).grid(row=3, column=0, pady=5)

        tk.Button(report_window, text="Close", command=report_window.destroy, bg="#E74C3C", fg="white", font=("Helvetica", 12, "bold"), relief="flat", bd=2).grid(row=4, column=0, pady=20)

    def back(self):
        self.root.show_add_page()