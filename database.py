import sqlite3
from datetime import datetime

def init_db():
    conn = sqlite3.connect('registrations.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS registrations
        (id INTEGER PRIMARY KEY AUTOINCREMENT,
         name TEXT NOT NULL,
         email TEXT NOT NULL,
         registration_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP)
    ''')
    conn.commit()
    conn.close()

def add_registration(name, email):
    conn = sqlite3.connect('registrations.db')
    c = conn.cursor()
    try:
        c.execute('''
            INSERT INTO registrations (name, email)
            VALUES (?, ?)
        ''', (name, email))
        conn.commit()
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False
    finally:
        conn.close()

def get_all_registrations():
    conn = sqlite3.connect('registrations.db')
    c = conn.cursor()
    c.execute('SELECT * FROM registrations')
    registrations = c.fetchall()
    conn.close()
    return registrations