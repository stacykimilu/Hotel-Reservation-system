# lib/models/hotel.py

from lib.helpers import execute_query, fetch_query

def insert_hotel(name):
    return execute_query('''
    INSERT INTO hotel (name)
    VALUES (?)
    ''', (name,))

def get_all_hotels():
    query = 'SELECT * FROM hotel'
    return fetch_query(query)
