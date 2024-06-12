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
        self.guest_details = None

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

    def book_room(self, guest_details, check_in_date, check_out_date, room_id, special_requests):
        for room in self.rooms:
            if room.room_id == room_id and not room.is_booked:
                room.is_booked = True
                room.guest_name = guest_details['name']
                room.check_in_date = check_in_date
                room.check_out_date = check_out_date
                room.special_requests = special_requests
                room.guest_details = guest_details
                self.reservations[guest_details['name']] = room
                print(f"Room {room_id} booked successfully for {guest_details['name']}.")
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
            room.guest_details = None
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
            print(f"Guest Details: {room.guest_details}")
        else:
            print(f"No booking found for {guest_name}.")

def main():
    hotel = Hotel("Seamless Hospitality")

    # Available rooms to the hotel
    hotel.add_room(Room(100, "Single Room", 100))
    hotel.add_room(Room(101, "Single Room", 101))
    hotel.add_room(Room(201, "Single Room  with a View", 102))
    hotel.add_room(Room(202, "Single Room", 103))
    hotel.add_room(Room(301, "Double room/twin room", 150))
    hotel.add_room(Room(303, "Double room/twin room", 151))
    hotel.add_room(Room(304, "Double room/twin room with a View", 152))
    hotel.add_room(Room(305, "Double room/twin room", 153))
    hotel.add_room(Room(401, "Queen Room", 201))
    hotel.add_room(Room(402, "Queen Room with a View", 202))
    hotel.add_room(Room(403, "Queen Room", 203))
    hotel.add_room(Room(404, "Triple Room", 204))
    hotel.add_room(Room(501, "Triple Room with a View", 205))
    hotel.add_room(Room(502, "Triple Room", 205))
    hotel.add_room(Room(503, "Studio Rooms", 305))
    hotel.add_room(Room(600, "Deluxe Rooms", 306))
    hotel.add_room(Room(601, "Deluxe Rooms", 307))
    hotel.add_room(Room(602, "Suites", 408))
    hotel.add_room(Room(603, "Suites", 409))
    hotel.add_room(Room(701, "Presidential Suites", 408))
    hotel.add_room(Room(702, "Presidential Suites", 409))
  
#  menu options
    while True:
        print("\nWelcome to the Meko Hotel Booking and Reservation System")
        print ("\nMenu:")
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
            print ("\n Enter the booking info:")
            guest_children = int(input("Enter number of children: "))
            guest_adults = int(input("Enter number of adults: "))
            check_in_date = input("Enter check-in date (YYYY-MM-DD): ")
            check_out_date = input("Enter check-out date (YYYY-MM-DD): ")
            special_requests = input("Enter special requests: ")
            guest_details = {
                'name': guest_name,
                'email': guest_email,
                'gender': guest_gender,
                'children': guest_children,
                'adults': guest_adults,
                'contact_number': guest_contact_number
            }
            available_rooms = hotel.list_available_rooms(check_in_date, check_out_date)
            if available_rooms:
                print("Available Rooms:")
                for room in available_rooms:
                    print(f"Room ID: {room.room_id}, Type: {room.room_type}, Price: ${room.price}")
                room_id = int(input("Enter room ID to book: "))
                hotel.book_room(guest_details, check_in_date, check_out_date, room_id, special_requests)
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
