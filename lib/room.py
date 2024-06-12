from helpers import execute_query

class Room:
    def __init__(self, hotel_id, room_number, status):
        self.hotel_id = hotel_id
        self.room_number = room_number
        self.status = status

    def add_room(self):
        query = 'INSERT INTO rooms (hotel_id, room_number, status) VALUES (?, ?, ?)'
        execute_query(query, (self.hotel_id, self.room_number, self.status))

    def update_status(self, status):
        query = 'UPDATE rooms SET status = ? WHERE hotel_id = ? AND room_number = ?'
        execute_query(query, (status, self.hotel_id, self.room_number))
