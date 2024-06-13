# lib/helpers.py

import sqlite3

DB_FILE = 'hotel.db'

def create_connection():
    return sqlite3.connect(DB_FILE)

def execute_query(query, params=()):
    conn = create_connection()
    try:
        cursor = conn.cursor()
        cursor.execute(query, params)
        conn.commit()
        return cursor.lastrowid
    finally:
        conn.close()

def fetch_query(query, params=()):
    conn = create_connection()
    try:
        cursor = conn.cursor()
        cursor.execute(query, params)
        return cursor.fetchall()
    finally:
        conn.close()

def init_db():
    execute_query('''
    CREATE TABLE IF NOT EXISTS guest (
        id INTEGER PRIMARY KEY,
        name TEXT,
        email TEXT,
        gender TEXT,
        contact_number TEXT
    )
    ''')

    execute_query('''
    CREATE TABLE IF NOT EXISTS hotel (
        id INTEGER PRIMARY KEY,
        name TEXT
    )
    ''')

    execute_query('''
    CREATE TABLE IF NOT EXISTS room (
        id INTEGER PRIMARY KEY,
        room_type TEXT,
        price REAL,
        hotel_id INTEGER,
        is_booked BOOLEAN,
        check_in_date TEXT,
        check_out_date TEXT,
        special_requests TEXT,
        guest_id INTEGER,
        FOREIGN KEY (hotel_id) REFERENCES hotel (id),
        FOREIGN KEY (guest_id) REFERENCES guest (id)
    )
    ''')

    execute_query('''
    CREATE TABLE IF NOT EXISTS reservation (
        id INTEGER PRIMARY KEY,
        guest_id INTEGER,
        room_id INTEGER,
        check_in_date TEXT,
        check_out_date TEXT,
        special_requests TEXT,
        FOREIGN KEY (guest_id) REFERENCES guest (id),
        FOREIGN KEY (room_id) REFERENCES room (id)
    )
    ''')

    # Add hardcoded rooms
    rooms = [
        (100, "Single Room", 100, 1, False),
        (101, "Double Room", 150, 1, False),
        (102, "Suite", 300, 1, False)
    ]

    for room in rooms:
        execute_query('''
        INSERT OR IGNORE INTO room (id, room_type, price, hotel_id, is_booked)
        VALUES (?, ?, ?, ?, ?)
        ''', room)
