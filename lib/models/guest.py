# lib/models/guest.py

from helpers import execute_query, fetch_query

def insert_guest(name, email, gender, contact_number):
    return execute_query('''
    INSERT INTO guest (name, email, gender, contact_number)
    VALUES (?, ?, ?, ?)
    ''', (name, email, gender, contact_number))

def get_guest_by_name(name):
    query = 'SELECT * FROM guest WHERE name = ?'
    return fetch_query(query, (name,))
