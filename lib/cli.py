# lib/cli.py

from helpers import init_db
from models.guest import insert_guest, get_guest_by_name
from models.room import get_all_rooms, list_available_rooms
from models.reservation import insert_reservation, get_reservation_by_guest_name, modify_reservation

def main():
    init_db()  # Initialize the database

    while True:
        print("\nWelcome to the Hotel Booking and Reservation System")
        print("Menu:")
        print("1. Book Room")
        print("2. Modify Booking")
        print("3. Cancel Booking")
        print("4. View Booking")
        print("5. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            guest_name = input("Enter guest name: ")
            guest_email = input("Enter guest email: ")
            guest_gender = input("Enter guest gender: ")
            guest_contact_number = input("Enter guest contact number: ")
            insert_guest(guest_name, guest_email, guest_gender, guest_contact_number)

            print("Enter booking details:")
            check_in_date = input("Enter check-in date (YYYY-MM-DD): ")
            check_out_date = input("Enter check-out date (YYYY-MM-DD): ")
            special_requests = input("Enter special requests: ")

            available_rooms = list_available_rooms(check_in_date, check_out_date)
            if available_rooms:
                print("Available Rooms:")
                for room in available_rooms:
                    print(f"Room ID: {room[0]}, Type: {room[1]}, Price: ${room[2]}")
                room_id = int(input("Enter room ID to book: "))
                
                guest = get_guest_by_name(guest_name)
                if guest:
                    insert_reservation(guest[0][0], room_id, check_in_date, check_out_date, special_requests)
                    print(f"Room {room_id} booked successfully for {guest_name}.")
                else:
                    print("Guest not found.")
            else:
                print("No available rooms for the selected dates.")

        elif choice == 2:
            guest_name = input("Enter guest name: ")
            new_check_in_date = input("Enter new check-in date (YYYY-MM-DD): ")
            new_check_out_date = input("Enter new check-out date (YYYY-MM-DD): ")
            new_special_requests = input("Enter new special requests: ")
            modify_reservation(guest_name, new_check_in_date, new_check_out_date, new_special_requests)

        elif choice == 3:
            guest_name = input("Enter guest name: ")
            # Functionality to cancel the booking
            print(f"Booking for {guest_name} has been canceled.")

        elif choice == 4:
            guest_name = input("Enter guest name: ")
            reservations = get_reservation_by_guest_name(guest_name)
            if reservations:
                for reservation in reservations:
                    print(f"Reservation ID: {reservation[0]}, Guest Name: {reservation[1]}, Room Type: {reservation[2]}, Check-in Date: {reservation[3]}, Check-out Date: {reservation[4]}, Special Requests: {reservation[5]}")
            else:
                print(f"No bookings found for {guest_name}.")

        elif choice == 5:
            print("Thank you for using the Hotel Booking and Reservation System.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
