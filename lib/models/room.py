# lib/models/room.py

from helpers import execute_query, fetch_query

def insert_room(room_type, price, hotel_id):
    return execute_query('''
    INSERT INTO room (room_type, price, hotel_id, is_booked)
    VALUES (?, ?, ?, ?)
    ''', (room_type, price, hotel_id, False))

def get_all_rooms():
    query = 'SELECT * FROM room'
    return fetch_query(query)

def list_available_rooms(check_in_date, check_out_date):
    query = '''
    SELECT * FROM room
    WHERE is_booked = 0 OR (check_out_date <= ? OR check_in_date >= ?)
    '''
    return fetch_query(query, (check_in_date, check_out_date))
