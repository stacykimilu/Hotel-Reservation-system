# lib/main.py

from models import guest, room, reservation

def main():
    print("Welcome to the Hotel Reservation System!")
    username = input("Enter your username: ")
    
    guest_id = guest.get_guest_by_username(username)
    if not guest_id:
        print(f"User '{username}' not found. Let's create your profile.")
        email = input("Enter your email address: ")
        phone_number = input("Enter your phone number: ")
        guest.insert_guest(username, email, phone_number)
        print(f"User '{username}' created successfully!")

    while True:
        print("\nMenu:")
        print("1. Book a Room")
        print("2. View Booked Rooms")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            book_room(username)
        elif choice == '2':
            view_booked_rooms(username)
        elif choice == '3':
            print("Thank you for using the Hotel Reservation System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

def book_room(username):
    rooms = room.get_all_rooms()
    for room_data in rooms:
        print(f"Room ID: {room_data[0]}, Type: {room_data[1]}, Capacity: {room_data[2]}")

    room_id = int(input("Enter Room ID to book: "))
    
    if not any(room_data[0] == room_id for room_data in rooms):
        print("Room not found")
        return

    check_in_date = input("Enter check-in date (YYYY-MM-DD): ")
    check_out_date = input("Enter check-out date (YYYY-MM-DD): ")

    guest_id = guest.get_guest_by_username(username)

    reservation.insert_reservation(guest_id, room_id, check_in_date, check_out_date, "Booked")

    print("Room booked successfully!")

def view_booked_rooms(username):
    guest_id = guest.get_guest_by_username(username)
    reservations = reservation.get_reservations_by_guest_id(guest_id)

    if not reservations:
        print("No rooms booked.")
    else:
        print("Your Booked Rooms:")
        for res in reservations:
            room_details = room.get_room_by_id(res[2])
            print(f"Room ID: {res[2]}, Type: {room_details[1]}, Check-in: {res[3]}, Check-out: {res[4]}, Status: {res[5]}")

def main():
    guest.create_guest_table()
    room.create_room_table()
    reservation.create_reservation_table()

    main()

if __name__ == "__main__":
    main()
