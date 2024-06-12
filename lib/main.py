from reservation import create_reservation, update_reservation, cancel_reservation
from hotel import Hotel
from guest import Guest
from database import init_db

def main():
    init_db()  
if __name__ == "__main__":
    main()
