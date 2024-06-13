# lib/models/reservation.py

from helpers import execute_query, fetch_query

def insert_reservation(guest_id, room_id, check_in_date, check_out_date, special_requests):
    return execute_query('''
    INSERT INTO reservation (guest_id, room_id, check_in_date, check_out_date, special_requests)
    VALUES (?, ?, ?, ?, ?)
    ''', (guest_id, room_id, check_in_date, check_out_date, special_requests))

def get_reservation_by_guest_name(guest_name):
    query = '''
    SELECT reservation.id, guest.name, room.room_type, reservation.check_in_date, reservation.check_out_date, reservation.special_requests
    FROM reservation
    JOIN guest ON reservation.guest_id = guest.id
    JOIN room ON reservation.room_id = room.id
    WHERE guest.name = ?
    '''
    return fetch_query(query, (guest_name,))

def modify_reservation(guest_name, new_check_in_date, new_check_out_date, new_special_requests):
    guest_query = 'SELECT id FROM guest WHERE name = ?'
    guest_id = fetch_query(guest_query, (guest_name,))
    if not guest_id:
        print("No guest found with that name.")
        return

    reservation_query = '''
    UPDATE reservation
    SET check_in_date = ?, check_out_date = ?, special_requests = ?
    WHERE guest_id = ?
    '''
    execute_query(reservation_query, (new_check_in_date, new_check_out_date, new_special_requests, guest_id[0][0]))
    print(f"Reservation for {guest_name} updated successfully.")
