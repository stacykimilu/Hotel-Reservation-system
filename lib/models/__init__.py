import sqlite3

def get_db_connection():
    connection = sqlite3.connect('hotel_booking.db')
    return connection

def init_db():
    connection = get_db_connection()
    cursor = connection.cursor()
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS hotel (
        id INTEGER PRIMARY KEY,
        name TEXT,
        location TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    ''')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS guest (
        id INTEGER PRIMARY KEY,
        username TEXT,
        role TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    ''')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS room (
        id INTEGER PRIMARY KEY,
        room_type TEXT,
        capacity INTEGER,
        hotel_id INTEGER,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (hotel_id) REFERENCES hotel (id)
    )
    ''')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS reservation (
        id INTEGER PRIMARY KEY,
        guest_id INTEGER,
        room_id INTEGER,
        check_in_date TIMESTAMP,
        check_out_date TIMESTAMP,
        status TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (guest_id) REFERENCES guest (id),
        FOREIGN KEY (room_id) REFERENCES room (id)
    )
    ''')
    
    connection.commit()
    connection.close()
    print("Database and tables created successfully.")
