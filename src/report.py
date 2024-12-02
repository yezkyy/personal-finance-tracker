import matplotlib.pyplot as plt
import sqlite3

def plot_expenses():
    conn = sqlite3.connect('database/finance.db')
    c = conn.cursor()
    c.execute("SELECT category, SUM(amount) FROM transactions WHERE type='expense' GROUP BY category")
    categories = c.fetchall()
    
    labels = [category[0] for category in categories]
    amounts = [category[1] for category in categories]
    
    plt.pie(amounts, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.title("Expense Breakdown")
    plt.show()
