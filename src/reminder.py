import sqlite3

def add_bill(amount, description, due_date):
    conn = sqlite3.connect('database/finance.db')
    c = conn.cursor()
    c.execute('''INSERT INTO bills (amount, description, due_date, paid) 
                VALUES (?, ?, ?, ?)''', (amount, description, due_date, False))
    conn.commit()
    conn.close()

def check_due_bills():
    conn = sqlite3.connect('database/finance.db')
    c = conn.cursor()
    c.execute("SELECT description, due_date FROM bills WHERE paid=0 AND due_date <= DATE('now')")
    due_bills = c.fetchall()
    conn.close()
    
    return due_bills
