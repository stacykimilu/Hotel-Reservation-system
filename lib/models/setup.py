import sqlite3

DATABASE_NAME = 'hotel_management.db'

def init_db():
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    # Create tables
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS guests (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            contact_info TEXT NOT NULL
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS rooms (
            id INTEGER PRIMARY KEY,
            hotel_id INTEGER,
            room_number TEXT NOT NULL,
            status TEXT NOT NULL,
            FOREIGN KEY (hotel_id) REFERENCES hotels(id)
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS reservations (
            id INTEGER PRIMARY KEY,
            guest_id INTEGER,
            room_id INTEGER,
            check_in_date TEXT NOT NULL,
            check_out_date TEXT NOT NULL,
            FOREIGN KEY (guest_id) REFERENCES guests(id),
            FOREIGN KEY (room_id) REFERENCES rooms(id)
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS hotels (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            address TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def execute_query(query, params=None):
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    if params:
        cursor.execute(query, params)
    else:
        cursor.execute(query)
    conn.commit()
    conn.close()

def fetch_all(query, params=None):
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    if params:
        cursor.execute(query, params)
    else:
        cursor.execute(query)
    records = cursor.fetchall()
    conn.close()
    return records