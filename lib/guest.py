from helpers import execute_query

class Guest:
    def __init__(self, name, contact_info):
        self.name = name
        self.contact_info = contact_info

    def add_guest(self):
        query = 'INSERT INTO guests (name, contact_info) VALUES (?, ?)'
        execute_query(query, (self.name, self.contact_info))

    def remove_guest(self):
        query = 'DELETE FROM guests WHERE name = ? AND contact_info = ?'
        execute_query(query, (self.name, self.contact_info))
