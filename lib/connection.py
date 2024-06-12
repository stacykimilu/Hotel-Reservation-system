import sqlite3

DATABASE_NAME = './database/hotel_db'

def get_db_connection():
    conn = sqlite3.connect(
     database ="hotel_db.db"
    )
    
    return conn
