import datetime

class Room:
    def __init__(self, room_id, room_type, price):
        self.room_id = room_id
        self.room_type = room_type
        self.price = price
        self.is_booked = False
        self.guest_name = None
        self.check_in_date = None
        self.check_out_date = None
        self.special_requests = None

class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = []
        self.reservations = {}

    def add_room(self, room):
        self.rooms.append(room)

    def list_available_rooms(self, check_in_date, check_out_date):
        available_rooms = []
        for room in self.rooms:
            if not room.is_booked or (room.check_out_date <= check_in_date or room.check_in_date >= check_out_date):
                available_rooms.append(room)
        return available_rooms

    def book_room(self, guest_name, check_in_date, check_out_date, room_id, special_requests):
        for room in self.rooms:
            if room.room_id == room_id and not room.is_booked:
                room.is_booked = True
                room.guest_name = guest_name
                room.check_in_date = check_in_date
                room.check_out_date = check_out_date
                room.special_requests = special_requests
                self.reservations[guest_name] = room
                print(f"Room {room_id} booked successfully for {guest_name}.")
                return
        print(f"Room {room_id} is not available for booking.")

    def modify_booking(self, guest_name, new_check_in_date, new_check_out_date, new_special_requests):
        if guest_name in self.reservations:
            room = self.reservations[guest_name]
            room.check_in_date = new_check_in_date
            room.check_out_date = new_check_out_date
            room.special_requests = new_special_requests
            print(f"Booking for {guest_name} modified successfully.")
        else:
            print(f"No booking found for {guest_name}.")

    def cancel_booking(self, guest_name):
        if guest_name in self.reservations:
            room = self.reservations[guest_name]
            room.is_booked = False
            room.guest_name = None
            room.check_in_date = None
            room.check_out_date = None
            room.special_requests = None
            del self.reservations[guest_name]
            print(f"Booking for {guest_name} canceled successfully.")
        else:
            print(f"No booking found for {guest_name}.")

    def view_booking(self, guest_name):
        if guest_name in self.reservations:
            room = self.reservations[guest_name]
            print(f"Booking Details for {guest_name}:")
            print(f"Room ID: {room.room_id}")
            print(f"Room Type: {room.room_type}")
            print(f"Check-in Date: {room.check_in_date}")
            print(f"Check-out Date: {room.check_out_date}")
            print(f"Special Requests: {room.special_requests}")
        else:
            print(f"No booking found for {guest_name}.")

def main():
    hotel = Hotel("Seamless Hospitality")

    # Add rooms to the hotel
    hotel.add_room(Room(101, "Single", 100))
    hotel.add_room(Room(102, "Double", 150))
    hotel.add_room(Room(103, "Suite", 200))

    while True:
        print("\nWelcome to the Hotel Booking and Reservation System")
        print("1. Book Room")
        print("2. Modify Booking")
        print("3. Cancel Booking")
        print("4. View Booking")
        print("5. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            guest_name = input("Enter guest name: ")
            check_in_date = input("Enter check-in date (YYYY-MM-DD): ")
            check_out_date = input("Enter check-out date (YYYY-MM-DD): ")
            special_requests = input("Enter special requests: ")
            available_rooms = hotel.list_available_rooms(check_in_date, check_out_date)
            if available_rooms:
                print("Available Rooms:")
                for room in available_rooms:
                    print(f"Room ID: {room.room_id}, Type: {room.room_type}, Price: ${room.price}")
                room_id = int(input("Enter room ID to book: "))
                hotel.book_room(guest_name, check_in_date, check_out_date, room_id, special_requests)
            else:
                print("No available rooms for the selected dates.")
        
        elif choice == 2:
            guest_name = input("Enter guest name: ")
            new_check_in_date = input("Enter new check-in date (YYYY-MM-DD): ")
            new_check_out_date = input("Enter new check-out date (YYYY-MM-DD): ")
            new_special_requests = input("Enter new special requests: ")
            hotel.modify_booking(guest_name, new_check_in_date, new_check_out_date, new_special_requests)

        elif choice == 3:
            guest_name = input("Enter guest name: ")
            hotel.cancel_booking(guest_name)

        elif choice == 4:
            guest_name = input("Enter guest name: ")
            hotel.view_booking(guest_name)

        elif choice == 5:
            print("Thank you for using the Hotel Booking and Reservation System.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
