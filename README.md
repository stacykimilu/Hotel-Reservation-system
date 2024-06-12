# Hotel Booking and Reservation System
Date: 2024/6/11

By Stacy Mwende Kimilu

## Description
Welcome to the Hotel Booking and Reservation System! This Python Command-Line Interface (CLI) application is designed to simplify the process of booking accommodations and managing reservations for hotels. Whether you're a hotel manager seeking to optimize occupancy or a traveler looking for a seamless booking experience, this application provides a user-friendly platform to reserve rooms and manage reservations effortlessly.

## Project Setup Instructions
To run the Hotel Booking and Reservation System locally, follow these steps:

1. Ensure you have Python installed on your device.
2. Fork and clone the repository to your local machine.
3. Navigate to the project directory using the terminal: `cd python-p3-v2-final-project-template`.
4. Open a terminal and run the following command to start the application: `python main.py`.

## Folder Structure
The folder structure of the project is organized as follows:

- **main.py**: Main Python file for running the application. This script initializes the application, processes user inputs, and calls the appropriate functions to handle various tasks such as booking rooms, viewing reservations, and managing hotel data.

- **reservation.py**: This file contains the logic and functionalities for handling reservations. It includes functions to create, update, and cancel reservations. Key functions:
  - `create_reservation()`: Books a room for a guest.
  - `update_reservation()`: Modifies an existing reservation.
  - `cancel_reservation()`: Cancels a reservation.

- **hotel.py**: This file manages hotel data and operations. It includes classes and functions to manage room availability, rates, and other hotel-related data. Key components:
  - `Hotel` class: Represents a hotel with attributes like name, address, and room inventory.
  - `add_room()`: Adds a room to the hotel's inventory.
  - `remove_room()`: Removes a room from the hotel's inventory.

- **guest.py**: Manages guest information and interactions. It includes functions to handle guest details and their interactions with the hotel system. Key components:
  - `Guest` class: Represents a guest with attributes like name, contact information, and reservation history.
  - `add_guest()`: Adds a guest to the system.
  - `remove_guest()`: Removes a guest from the system.

- **database.py**: This file handles database operations and data storage using SQLite. It includes functions to initialize the database, perform CRUD operations, and ensure data integrity. Key functions:
  - `init_db()`: Initializes the database with the necessary tables.
  - `execute_query()`: Executes a given SQL query.
  - `fetch_all()`: Retrieves all records from a specified table.

- **README.md**: Markdown file containing information about the project.

## Live Site on GitHub Pages
[Live Site](https://github.com/stacykimilu/python-p3-v2-final-project-template)

## Technologies Used

- **Python**: A high-level, interpreted programming language known for its simplicity and readability. In this project, Python is used for implementing the application's core logic, managing hotel data, handling reservations, and providing a command-line interface for user interaction.
- **SQLite**: A lightweight, disk-based database that doesn't require a separate server process. SQLite is used in this project to store hotel and reservation data efficiently, allowing for easy data management and retrieval.
- **GitHub**: A web-based platform used for version control and collaborative development. GitHub hosts the project's code repository, enabling multiple developers to contribute to the project, track changes, and manage different versions of the codebase.

## Object-Relational Mapping (ORM)
This project uses SQLite as the underlying database and does not utilize a separate ORM. SQLite provides a lightweight and efficient solution for data storage and retrieval, without the need for complex ORM frameworks.

## Object-Oriented Programming (OOP)
The application follows Object-Oriented Programming (OOP) principles, utilizing Python classes such as `Hotel`, `Reservation`, and `Guest` to model the system's entities. These classes encapsulate data and behavior related to hotels, reservations, and guests, allowing for modular and organized code structure.

## Support and Contact Details
If you have any inquiries or suggestions, feel free to reach out:

GitHub: [Stacy Kimilu](https://github.com/stacykimilu)

## License
The content of this site is licensed under the MIT license.

© 2024 Stacy Mwende Kimilu
