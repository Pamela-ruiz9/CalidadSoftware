"""
Hotel Reservation System.

This module implements a hotel reservation system with three main classes:
Hotel, Customer, and Reservation. It provides persistent storage using JSON
files and handles CRUD operations for all entities.

Author: Student
Date: February 22, 2026
"""

import json
import os
from datetime import datetime
from typing import Dict, List, Optional


class Customer:
    """Represents a customer in the reservation system."""

    def __init__(self, customer_id: str, name: str, email: str,
                 phone: str) -> None:
        """
        Initialize a Customer instance.

        Args:
            customer_id: Unique identifier for the customer
            name: Customer's full name
            email: Customer's email address
            phone: Customer's phone number
        """
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.phone = phone

    def to_dict(self) -> Dict:
        """
        Convert customer to dictionary for JSON serialization.

        Returns:
            Dictionary representation of the customer
        """
        return {
            'customer_id': self.customer_id,
            'name': self.name,
            'email': self.email,
            'phone': self.phone
        }

    @staticmethod
    def from_dict(data: Dict) -> 'Customer':
        """
        Create a Customer instance from dictionary.

        Args:
            data: Dictionary containing customer data

        Returns:
            Customer instance
        """
        return Customer(
            data['customer_id'],
            data['name'],
            data['email'],
            data['phone']
        )

    def __str__(self) -> str:
        """Return string representation of customer."""
        return (f"Customer(ID: {self.customer_id}, Name: {self.name}, "
                f"Email: {self.email}, Phone: {self.phone})")


class Hotel:
    """Represents a hotel in the reservation system."""

    def __init__(self, hotel_id: str, name: str, location: str,
                 total_rooms: int) -> None:
        """
        Initialize a Hotel instance.

        Args:
            hotel_id: Unique identifier for the hotel
            name: Hotel's name
            location: Hotel's location/address
            total_rooms: Total number of rooms in the hotel
        """
        self.hotel_id = hotel_id
        self.name = name
        self.location = location
        self.total_rooms = total_rooms
        self.available_rooms = total_rooms

    def to_dict(self) -> Dict:
        """
        Convert hotel to dictionary for JSON serialization.

        Returns:
            Dictionary representation of the hotel
        """
        return {
            'hotel_id': self.hotel_id,
            'name': self.name,
            'location': self.location,
            'total_rooms': self.total_rooms,
            'available_rooms': self.available_rooms
        }

    @staticmethod
    def from_dict(data: Dict) -> 'Hotel':
        """
        Create a Hotel instance from dictionary.

        Args:
            data: Dictionary containing hotel data

        Returns:
            Hotel instance
        """
        hotel = Hotel(
            data['hotel_id'],
            data['name'],
            data['location'],
            data['total_rooms']
        )
        hotel.available_rooms = data.get('available_rooms',
                                         data['total_rooms'])
        return hotel

    def __str__(self) -> str:
        """Return string representation of hotel."""
        return (f"Hotel(ID: {self.hotel_id}, Name: {self.name}, "
                f"Location: {self.location}, "
                f"Available Rooms: {self.available_rooms}/{self.total_rooms})")


class Reservation:
    """Represents a reservation in the system."""

    def __init__(self, reservation_id: str, customer_id: str,
                 hotel_id: str, check_in: str, check_out: str) -> None:
        """
        Initialize a Reservation instance.

        Args:
            reservation_id: Unique identifier for the reservation
            customer_id: ID of the customer making the reservation
            hotel_id: ID of the hotel being reserved
            check_in: Check-in date (YYYY-MM-DD format)
            check_out: Check-out date (YYYY-MM-DD format)
        """
        self.reservation_id = reservation_id
        self.customer_id = customer_id
        self.hotel_id = hotel_id
        self.check_in = check_in
        self.check_out = check_out
        self.status = "active"

    def to_dict(self) -> Dict:
        """
        Convert reservation to dictionary for JSON serialization.

        Returns:
            Dictionary representation of the reservation
        """
        return {
            'reservation_id': self.reservation_id,
            'customer_id': self.customer_id,
            'hotel_id': self.hotel_id,
            'check_in': self.check_in,
            'check_out': self.check_out,
            'status': self.status
        }

    @staticmethod
    def from_dict(data: Dict) -> 'Reservation':
        """
        Create a Reservation instance from dictionary.

        Args:
            data: Dictionary containing reservation data

        Returns:
            Reservation instance
        """
        reservation = Reservation(
            data['reservation_id'],
            data['customer_id'],
            data['hotel_id'],
            data['check_in'],
            data['check_out']
        )
        reservation.status = data.get('status', 'active')
        return reservation

    def __str__(self) -> str:
        """Return string representation of reservation."""
        return (f"Reservation(ID: {self.reservation_id}, "
                f"Customer: {self.customer_id}, Hotel: {self.hotel_id}, "
                f"Check-in: {self.check_in}, Check-out: {self.check_out}, "
                f"Status: {self.status})")


class ReservationSystem:
    """Manages the hotel reservation system operations."""

    def __init__(self, data_dir: str = "data") -> None:
        """
        Initialize the Reservation System.

        Args:
            data_dir: Directory to store data files
        """
        self.data_dir = data_dir
        self.hotels_file = os.path.join(data_dir, "hotels.json")
        self.customers_file = os.path.join(data_dir, "customers.json")
        self.reservations_file = os.path.join(data_dir, "reservations.json")

        # Create data directory if it doesn't exist
        os.makedirs(data_dir, exist_ok=True)

        self.hotels: Dict[str, Hotel] = {}
        self.customers: Dict[str, Customer] = {}
        self.reservations: Dict[str, Reservation] = {}

        self._load_data()

    def _load_data(self) -> None:
        """Load all data from JSON files."""
        try:
            self._load_hotels()
        except Exception as e:
            print(f"Error loading hotels: {e}")
            self.hotels = {}

        try:
            self._load_customers()
        except Exception as e:
            print(f"Error loading customers: {e}")
            self.customers = {}

        try:
            self._load_reservations()
        except Exception as e:
            print(f"Error loading reservations: {e}")
            self.reservations = {}

    def _load_hotels(self) -> None:
        """Load hotels from JSON file."""
        if os.path.exists(self.hotels_file):
            try:
                with open(self.hotels_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    self.hotels = {
                        h_id: Hotel.from_dict(h_data)
                        for h_id, h_data in data.items()
                    }
            except json.JSONDecodeError as e:
                print(f"Invalid JSON in hotels file: {e}")
                raise
            except KeyError as e:
                print(f"Missing required field in hotel data: {e}")
                raise

    def _load_customers(self) -> None:
        """Load customers from JSON file."""
        if os.path.exists(self.customers_file):
            try:
                with open(self.customers_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    self.customers = {
                        c_id: Customer.from_dict(c_data)
                        for c_id, c_data in data.items()
                    }
            except json.JSONDecodeError as e:
                print(f"Invalid JSON in customers file: {e}")
                raise
            except KeyError as e:
                print(f"Missing required field in customer data: {e}")
                raise

    def _load_reservations(self) -> None:
        """Load reservations from JSON file."""
        if os.path.exists(self.reservations_file):
            try:
                with open(self.reservations_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    self.reservations = {
                        r_id: Reservation.from_dict(r_data)
                        for r_id, r_data in data.items()
                    }
            except json.JSONDecodeError as e:
                print(f"Invalid JSON in reservations file: {e}")
                raise
            except KeyError as e:
                print(f"Missing required field in reservation data: {e}")
                raise

    def _save_hotels(self) -> None:
        """Save hotels to JSON file."""
        try:
            with open(self.hotels_file, 'w', encoding='utf-8') as f:
                data = {h_id: hotel.to_dict()
                        for h_id, hotel in self.hotels.items()}
                json.dump(data, f, indent=2, ensure_ascii=False)
        except Exception as e:
            print(f"Error saving hotels: {e}")
            raise

    def _save_customers(self) -> None:
        """Save customers to JSON file."""
        try:
            with open(self.customers_file, 'w', encoding='utf-8') as f:
                data = {c_id: customer.to_dict()
                        for c_id, customer in self.customers.items()}
                json.dump(data, f, indent=2, ensure_ascii=False)
        except Exception as e:
            print(f"Error saving customers: {e}")
            raise

    def _save_reservations(self) -> None:
        """Save reservations to JSON file."""
        try:
            with open(self.reservations_file, 'w', encoding='utf-8') as f:
                data = {r_id: reservation.to_dict()
                        for r_id, reservation in self.reservations.items()}
                json.dump(data, f, indent=2, ensure_ascii=False)
        except Exception as e:
            print(f"Error saving reservations: {e}")
            raise

    # Hotel operations
    def create_hotel(self, hotel_id: str, name: str, location: str,
                     total_rooms: int) -> Optional[Hotel]:
        """
        Create a new hotel.

        Args:
            hotel_id: Unique identifier for the hotel
            name: Hotel's name
            location: Hotel's location
            total_rooms: Total number of rooms

        Returns:
            Created Hotel instance or None if hotel already exists
        """
        if hotel_id in self.hotels:
            print(f"Error: Hotel with ID {hotel_id} already exists")
            return None

        if total_rooms <= 0:
            print("Error: Total rooms must be positive")
            return None

        hotel = Hotel(hotel_id, name, location, total_rooms)
        self.hotels[hotel_id] = hotel
        self._save_hotels()
        return hotel

    def delete_hotel(self, hotel_id: str) -> bool:
        """
        Delete a hotel.

        Args:
            hotel_id: ID of the hotel to delete

        Returns:
            True if deleted, False otherwise
        """
        if hotel_id not in self.hotels:
            print(f"Error: Hotel with ID {hotel_id} not found")
            return False

        # Check for active reservations
        active_reservations = [
            r for r in self.reservations.values()
            if r.hotel_id == hotel_id and r.status == "active"
        ]
        if active_reservations:
            print("Error: Cannot delete hotel with active reservations")
            return False

        del self.hotels[hotel_id]
        self._save_hotels()
        return True

    def display_hotel(self, hotel_id: str) -> Optional[Hotel]:
        """
        Display hotel information.

        Args:
            hotel_id: ID of the hotel to display

        Returns:
            Hotel instance or None if not found
        """
        if hotel_id not in self.hotels:
            print(f"Error: Hotel with ID {hotel_id} not found")
            return None
        return self.hotels[hotel_id]

    def modify_hotel(self, hotel_id: str, name: Optional[str] = None,
                     location: Optional[str] = None,
                     total_rooms: Optional[int] = None) -> Optional[Hotel]:
        """
        Modify hotel information.

        Args:
            hotel_id: ID of the hotel to modify
            name: New name (optional)
            location: New location (optional)
            total_rooms: New total rooms (optional)

        Returns:
            Modified Hotel instance or None if not found
        """
        if hotel_id not in self.hotels:
            print(f"Error: Hotel with ID {hotel_id} not found")
            return None

        hotel = self.hotels[hotel_id]

        if name is not None:
            hotel.name = name
        if location is not None:
            hotel.location = location
        if total_rooms is not None:
            if total_rooms <= 0:
                print("Error: Total rooms must be positive")
                return None
            if total_rooms < (hotel.total_rooms - hotel.available_rooms):
                print("Error: Cannot reduce rooms below reserved count")
                return None
            hotel.available_rooms += (total_rooms - hotel.total_rooms)
            hotel.total_rooms = total_rooms

        self._save_hotels()
        return hotel

    # Customer operations
    def create_customer(self, customer_id: str, name: str, email: str,
                        phone: str) -> Optional[Customer]:
        """
        Create a new customer.

        Args:
            customer_id: Unique identifier for the customer
            name: Customer's name
            email: Customer's email
            phone: Customer's phone

        Returns:
            Created Customer instance or None if already exists
        """
        if customer_id in self.customers:
            print(f"Error: Customer with ID {customer_id} already exists")
            return None

        customer = Customer(customer_id, name, email, phone)
        self.customers[customer_id] = customer
        self._save_customers()
        return customer

    def delete_customer(self, customer_id: str) -> bool:
        """
        Delete a customer.

        Args:
            customer_id: ID of the customer to delete

        Returns:
            True if deleted, False otherwise
        """
        if customer_id not in self.customers:
            print(f"Error: Customer with ID {customer_id} not found")
            return False

        # Check for active reservations
        active_reservations = [
            r for r in self.reservations.values()
            if r.customer_id == customer_id and r.status == "active"
        ]
        if active_reservations:
            print("Error: Cannot delete customer with active reservations")
            return False

        del self.customers[customer_id]
        self._save_customers()
        return True

    def display_customer(self, customer_id: str) -> Optional[Customer]:
        """
        Display customer information.

        Args:
            customer_id: ID of the customer to display

        Returns:
            Customer instance or None if not found
        """
        if customer_id not in self.customers:
            print(f"Error: Customer with ID {customer_id} not found")
            return None
        return self.customers[customer_id]

    def modify_customer(self, customer_id: str, name: Optional[str] = None,
                        email: Optional[str] = None,
                        phone: Optional[str] = None) -> Optional[Customer]:
        """
        Modify customer information.

        Args:
            customer_id: ID of the customer to modify
            name: New name (optional)
            email: New email (optional)
            phone: New phone (optional)

        Returns:
            Modified Customer instance or None if not found
        """
        if customer_id not in self.customers:
            print(f"Error: Customer with ID {customer_id} not found")
            return None

        customer = self.customers[customer_id]

        if name is not None:
            customer.name = name
        if email is not None:
            customer.email = email
        if phone is not None:
            customer.phone = phone

        self._save_customers()
        return customer

    # Reservation operations
    def create_reservation(self, reservation_id: str, customer_id: str,
                           hotel_id: str, check_in: str,
                           check_out: str) -> Optional[Reservation]:
        """
        Create a new reservation.

        Args:
            reservation_id: Unique identifier for the reservation
            customer_id: ID of the customer
            hotel_id: ID of the hotel
            check_in: Check-in date (YYYY-MM-DD)
            check_out: Check-out date (YYYY-MM-DD)

        Returns:
            Created Reservation instance or None if validation fails
        """
        if reservation_id in self.reservations:
            print(f"Error: Reservation {reservation_id} already exists")
            return None

        if customer_id not in self.customers:
            print(f"Error: Customer with ID {customer_id} not found")
            return None

        if hotel_id not in self.hotels:
            print(f"Error: Hotel with ID {hotel_id} not found")
            return None

        hotel = self.hotels[hotel_id]
        if hotel.available_rooms <= 0:
            print(f"Error: No available rooms in hotel {hotel_id}")
            return None

        # Validate dates
        try:
            check_in_date = datetime.strptime(check_in, "%Y-%m-%d")
            check_out_date = datetime.strptime(check_out, "%Y-%m-%d")
            if check_out_date <= check_in_date:
                print("Error: Check-out must be after check-in")
                return None
        except ValueError:
            print("Error: Invalid date format. Use YYYY-MM-DD")
            return None

        reservation = Reservation(reservation_id, customer_id, hotel_id,
                                  check_in, check_out)
        self.reservations[reservation_id] = reservation
        hotel.available_rooms -= 1

        self._save_reservations()
        self._save_hotels()
        return reservation

    def cancel_reservation(self, reservation_id: str) -> bool:
        """
        Cancel a reservation.

        Args:
            reservation_id: ID of the reservation to cancel

        Returns:
            True if cancelled, False otherwise
        """
        if reservation_id not in self.reservations:
            print(f"Error: Reservation {reservation_id} not found")
            return False

        reservation = self.reservations[reservation_id]
        if reservation.status == "cancelled":
            print(f"Error: Reservation {reservation_id} already cancelled")
            return False

        reservation.status = "cancelled"
        hotel = self.hotels.get(reservation.hotel_id)
        if hotel:
            hotel.available_rooms += 1
            self._save_hotels()

        self._save_reservations()
        return True

    def get_all_hotels(self) -> List[Hotel]:
        """Get all hotels."""
        return list(self.hotels.values())

    def get_all_customers(self) -> List[Customer]:
        """Get all customers."""
        return list(self.customers.values())

    def get_all_reservations(self) -> List[Reservation]:
        """Get all reservations."""
        return list(self.reservations.values())
