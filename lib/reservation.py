from helper import execute_query

def create_reservation(guest_id, room_id, check_in_date, check_out_date, special_requests):
    query = '''
        INSERT INTO reservations (guest_id, room_id, check_in_date, check_out_date, special_requests)
        VALUES (?, ?, ?, ?, ?)
    '''
    execute_query(query, (guest_id, room_id, check_in_date, check_out_date, special_requests))

def update_reservation(reservation_id, check_in_date, check_out_date, special_requests):
    query = '''
        UPDATE reservations
        SET check_in_date = ?, check_out_date = ?, special_requests = ?
        WHERE id = ?
    '''
    execute_query(query, (check_in_date, check_out_date, special_requests, reservation_id))

def cancel_reservation(reservation_id):
    query = 'DELETE FROM reservations WHERE id = ?'
    execute_query(query, (reservation_id,))
