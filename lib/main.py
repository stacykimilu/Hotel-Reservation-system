from guest import Guest
from hotel import Hotel
from room import Room
from reservation import create_reservation, update_reservation, cancel_reservation
from helpers import create_tables, fetch_all

def main():
    create_tables()
    print("Welcome to the Hotel Booking and Reservation System")

    while True:
        print("\nOptions:")
        print("1. Add Guest")
        print("2. Add Hotel")
        print("3. Add Room")
        print("4. Create Reservation")
        print("5. Update Reservation")
        print("6. Cancel Reservation")
        print("7. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            name = input("Enter guest name: ")
            contact_info = input("Enter guest contact info: ")
            guest = Guest(name, contact_info)
            guest.add_guest()
            print(f"Guest {name} added successfully.")
        
        elif choice == 2:
            name = input("Enter hotel name: ")
            address = input("Enter hotel address: ")
            hotel = Hotel(name, address)
            hotel.add_hotel()
            print(f"Hotel {name} added successfully.")
        
        elif choice == 3:
            hotel_id = int(input("Enter hotel ID: "))
            room_number = input("Enter room number: ")
            status = input("Enter room status (available/booked): ")
            room = Room(hotel_id, room_number, status)
            room.add_room()
            print(f"Room {room_number} added successfully.")
        
        elif choice == 4:
            guest_id = int(input("Enter guest ID: "))
            room_id = int(input("Enter room ID: "))
            check_in_date = input("Enter check-in date (YYYY-MM-DD): ")
            check_out_date = input("Enter check-out date (YYYY-MM-DD): ")
            special_requests = input("Enter special requests: ")
            create_reservation(guest_id, room_id, check_in_date, check_out_date, special_requests)
            print("Reservation created successfully.")
        
        elif choice == 5:
            reservation_id = int(input("Enter reservation ID: "))
            check_in_date = input("Enter new check-in date (YYYY-MM-DD): ")
            check_out_date = input("Enter new check-out date (YYYY-MM-DD): ")
            special_requests = input("Enter new special requests: ")
            update_reservation(reservation_id, check_in_date, check_out_date, special_requests)
            print("Reservation updated successfully.")
        
        elif choice == 6:
            reservation_id = int(input("Enter reservation ID: "))
            cancel_reservation(reservation_id)
            print("Reservation canceled successfully.")
        
        elif choice == 7:
            print("Thank you for using the Hotel Booking and Reservation System.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
