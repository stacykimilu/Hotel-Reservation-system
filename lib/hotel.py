from helpers import execute_query

class Hotel:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def add_hotel(self):
        query = 'INSERT INTO hotels (name, address) VALUES (?, ?)'
        execute_query(query, (self.name, self.address))
