import sqlite3

conn = sqlite3.connect('staff_database.db')
c = conn.cursor()

# Create Staff Table
c.execute('''CREATE TABLE IF NOT EXISTS Staff (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                designation TEXT NOT NULL,
                gender TEXT NOT NULL,
                dob TEXT NOT NULL)''')

# Create Contact Table
c.execute('''CREATE TABLE IF NOT EXISTS Contact (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                staff_id INTEGER NOT NULL,
                phone TEXT,
                email TEXT,
                address TEXT,
                FOREIGN KEY (staff_id) REFERENCES Staff(id))''')

# Create Employment Table
c.execute('''CREATE TABLE IF NOT EXISTS Employment (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                cnic INTEGER, 
                staff_id INTEGER NOT NULL,
                shift TEXT,
                hire_date TEXT,
                contract TEXT,
                salary TEXT,
                qualification TEXT,
                FOREIGN KEY (staff_id) REFERENCES Staff(id))''')

# Create Users Table
c.execute('''CREATE TABLE IF NOT EXISTS Users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL)
                ''')

conn.commit()
conn.close()
