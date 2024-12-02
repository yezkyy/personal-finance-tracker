import sqlite3

def create_db():
    conn = sqlite3.connect('database/finance.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS transactions (
                    id INTEGER PRIMARY KEY,
                    amount REAL,
                    category TEXT,
                    date TEXT,
                    type TEXT)''')
    c.execute('''CREATE TABLE IF NOT EXISTS bills (
                    id INTEGER PRIMARY KEY,
                    amount REAL,
                    description TEXT,
                    due_date TEXT,
                    paid BOOLEAN)''')
    conn.commit()
    conn.close()

def add_transaction(amount, category, date, transaction_type):
    conn = sqlite3.connect('database/finance.db')
    c = conn.cursor()
    c.execute('''INSERT INTO transactions (amount, category, date, type) 
                 VALUES (?, ?, ?, ?)''', (amount, category, date, transaction_type))
    conn.commit()
    conn.close()

def generate_report():
    conn = sqlite3.connect('database/finance.db')
    c = conn.cursor()
    
    c.execute("SELECT SUM(amount) FROM transactions WHERE type='income'")
    total_income = c.fetchone()[0] or 0
    
    c.execute("SELECT SUM(amount) FROM transactions WHERE type='expense'")
    total_expense = c.fetchone()[0] or 0
    
    balance = total_income - total_expense
    conn.close()
    
    return {
        "total_income": total_income,
        "total_expense": total_expense,
        "balance": balance
    }
