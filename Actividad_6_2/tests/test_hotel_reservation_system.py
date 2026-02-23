"""
Unit tests for Hotel Reservation System.

This module contains comprehensive unit tests including negative test cases
for the hotel reservation system.

Author: Student
Date: February 22, 2026
"""

import os
import shutil
import sys
import unittest

# Add source directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'source'))

from hotel_reservation_system import (  # noqa: E402
    Hotel, Customer, Reservation, ReservationSystem
)


class TestCustomer(unittest.TestCase):
    """Test cases for Customer class."""

    def test_customer_creation(self):
        """Test customer creation with valid data."""
        customer = Customer("C001", "John Doe", "john@example.com",
                            "+1234567890")
        self.assertEqual(customer.customer_id, "C001")
        self.assertEqual(customer.name, "John Doe")
        self.assertEqual(customer.email, "john@example.com")
        self.assertEqual(customer.phone, "+1234567890")

    def test_customer_to_dict(self):
        """Test customer serialization to dictionary."""
        customer = Customer("C001", "John Doe", "john@example.com",
                            "+1234567890")
        data = customer.to_dict()
        self.assertEqual(data['customer_id'], "C001")
        self.assertEqual(data['name'], "John Doe")

    def test_customer_from_dict(self):
        """Test customer deserialization from dictionary."""
        data = {
            'customer_id': 'C001',
            'name': 'John Doe',
            'email': 'john@example.com',
            'phone': '+1234567890'
        }
        customer = Customer.from_dict(data)
        self.assertEqual(customer.customer_id, "C001")
        self.assertEqual(customer.name, "John Doe")

    def test_customer_str(self):
        """Test customer string representation."""
        customer = Customer("C001", "John Doe", "john@example.com",
                            "+1234567890")
        str_repr = str(customer)
        self.assertIn("C001", str_repr)
        self.assertIn("John Doe", str_repr)


class TestHotel(unittest.TestCase):
    """Test cases for Hotel class."""

    def test_hotel_creation(self):
        """Test hotel creation with valid data."""
        hotel = Hotel("H001", "Grand Hotel", "New York", 100)
        self.assertEqual(hotel.hotel_id, "H001")
        self.assertEqual(hotel.name, "Grand Hotel")
        self.assertEqual(hotel.location, "New York")
        self.assertEqual(hotel.total_rooms, 100)
        self.assertEqual(hotel.available_rooms, 100)

    def test_hotel_to_dict(self):
        """Test hotel serialization to dictionary."""
        hotel = Hotel("H001", "Grand Hotel", "New York", 100)
        data = hotel.to_dict()
        self.assertEqual(data['hotel_id'], "H001")
        self.assertEqual(data['total_rooms'], 100)
        self.assertEqual(data['available_rooms'], 100)

    def test_hotel_from_dict(self):
        """Test hotel deserialization from dictionary."""
        data = {
            'hotel_id': 'H001',
            'name': 'Grand Hotel',
            'location': 'New York',
            'total_rooms': 100,
            'available_rooms': 95
        }
        hotel = Hotel.from_dict(data)
        self.assertEqual(hotel.hotel_id, "H001")
        self.assertEqual(hotel.available_rooms, 95)

    def test_hotel_str(self):
        """Test hotel string representation."""
        hotel = Hotel("H001", "Grand Hotel", "New York", 100)
        str_repr = str(hotel)
        self.assertIn("H001", str_repr)
        self.assertIn("Grand Hotel", str_repr)


class TestReservation(unittest.TestCase):
    """Test cases for Reservation class."""

    def test_reservation_creation(self):
        """Test reservation creation with valid data."""
        reservation = Reservation("R001", "C001", "H001",
                                  "2026-03-01", "2026-03-05")
        self.assertEqual(reservation.reservation_id, "R001")
        self.assertEqual(reservation.customer_id, "C001")
        self.assertEqual(reservation.hotel_id, "H001")
        self.assertEqual(reservation.status, "active")

    def test_reservation_to_dict(self):
        """Test reservation serialization to dictionary."""
        reservation = Reservation("R001", "C001", "H001",
                                  "2026-03-01", "2026-03-05")
        data = reservation.to_dict()
        self.assertEqual(data['reservation_id'], "R001")
        self.assertEqual(data['status'], "active")

    def test_reservation_from_dict(self):
        """Test reservation deserialization from dictionary."""
        data = {
            'reservation_id': 'R001',
            'customer_id': 'C001',
            'hotel_id': 'H001',
            'check_in': '2026-03-01',
            'check_out': '2026-03-05',
            'status': 'cancelled'
        }
        reservation = Reservation.from_dict(data)
        self.assertEqual(reservation.status, "cancelled")


class TestReservationSystemNegativeCases(unittest.TestCase):
    """Test negative cases for Reservation System."""

    def setUp(self):
        """Set up test environment."""
        self.test_dir = "test_data_negative"
        if os.path.exists(self.test_dir):
            shutil.rmtree(self.test_dir)
        self.system = ReservationSystem(self.test_dir)

    def tearDown(self):
        """Clean up test environment."""
        if os.path.exists(self.test_dir):
            shutil.rmtree(self.test_dir)

    def test_negative_create_duplicate_hotel(self):
        """NEGATIVE: Test creating hotel with duplicate ID."""
        self.system.create_hotel("H001", "Hotel 1", "Location 1", 50)
        result = self.system.create_hotel("H001", "Hotel 2", "Location 2", 60)
        self.assertIsNone(result)

    def test_negative_create_hotel_invalid_rooms(self):
        """NEGATIVE: Test creating hotel with zero rooms."""
        result = self.system.create_hotel("H001", "Hotel 1", "Location 1", 0)
        self.assertIsNone(result)

    def test_negative_create_hotel_negative_rooms(self):
        """NEGATIVE: Test creating hotel with negative rooms."""
        result = self.system.create_hotel("H001", "Hotel 1", "Location 1", -10)
        self.assertIsNone(result)

    def test_negative_delete_nonexistent_hotel(self):
        """NEGATIVE: Test deleting non-existent hotel."""
        result = self.system.delete_hotel("NONEXISTENT")
        self.assertFalse(result)

    def test_negative_delete_hotel_with_active_reservation(self):
        """NEGATIVE: Test deleting hotel with active reservations."""
        self.system.create_hotel("H001", "Hotel 1", "Location 1", 50)
        self.system.create_customer("C001", "Customer 1", "c1@test.com",
                                    "123456")
        self.system.create_reservation("R001", "C001", "H001",
                                       "2026-03-01", "2026-03-05")
        result = self.system.delete_hotel("H001")
        self.assertFalse(result)

    def test_negative_display_nonexistent_hotel(self):
        """NEGATIVE: Test displaying non-existent hotel."""
        result = self.system.display_hotel("NONEXISTENT")
        self.assertIsNone(result)

    def test_negative_modify_nonexistent_hotel(self):
        """NEGATIVE: Test modifying non-existent hotel."""
        result = self.system.modify_hotel("NONEXISTENT", name="New Name")
        self.assertIsNone(result)

    def test_negative_modify_hotel_reduce_rooms_below_reserved(self):
        """NEGATIVE: Test reducing hotel rooms below reserved count."""
        self.system.create_hotel("H001", "Hotel 1", "Location 1", 50)
        self.system.create_customer("C001", "Customer 1", "c1@test.com",
                                    "123456")
        self.system.create_reservation("R001", "C001", "H001",
                                       "2026-03-01", "2026-03-05")
        result = self.system.modify_hotel("H001", total_rooms=0)
        self.assertIsNone(result)

    def test_negative_create_duplicate_customer(self):
        """NEGATIVE: Test creating customer with duplicate ID."""
        self.system.create_customer("C001", "Customer 1", "c1@test.com",
                                    "123456")
        result = self.system.create_customer("C001", "Customer 2",
                                             "c2@test.com", "789012")
        self.assertIsNone(result)

    def test_negative_delete_nonexistent_customer(self):
        """NEGATIVE: Test deleting non-existent customer."""
        result = self.system.delete_customer("NONEXISTENT")
        self.assertFalse(result)

    def test_negative_delete_customer_with_active_reservation(self):
        """NEGATIVE: Test deleting customer with active reservations."""
        self.system.create_hotel("H001", "Hotel 1", "Location 1", 50)
        self.system.create_customer("C001", "Customer 1", "c1@test.com",
                                    "123456")
        self.system.create_reservation("R001", "C001", "H001",
                                       "2026-03-01", "2026-03-05")
        result = self.system.delete_customer("C001")
        self.assertFalse(result)

    def test_negative_display_nonexistent_customer(self):
        """NEGATIVE: Test displaying non-existent customer."""
        result = self.system.display_customer("NONEXISTENT")
        self.assertIsNone(result)

    def test_negative_modify_nonexistent_customer(self):
        """NEGATIVE: Test modifying non-existent customer."""
        result = self.system.modify_customer("NONEXISTENT", name="New Name")
        self.assertIsNone(result)

    def test_negative_create_duplicate_reservation(self):
        """NEGATIVE: Test creating reservation with duplicate ID."""
        self.system.create_hotel("H001", "Hotel 1", "Location 1", 50)
        self.system.create_customer("C001", "Customer 1", "c1@test.com",
                                    "123456")
        self.system.create_reservation("R001", "C001", "H001",
                                       "2026-03-01", "2026-03-05")
        result = self.system.create_reservation("R001", "C001", "H001",
                                                "2026-03-10", "2026-03-15")
        self.assertIsNone(result)

    def test_negative_create_reservation_nonexistent_customer(self):
        """NEGATIVE: Test creating reservation with non-existent customer."""
        self.system.create_hotel("H001", "Hotel 1", "Location 1", 50)
        result = self.system.create_reservation("R001", "NONEXISTENT", "H001",
                                                "2026-03-01", "2026-03-05")
        self.assertIsNone(result)

    def test_negative_create_reservation_nonexistent_hotel(self):
        """NEGATIVE: Test creating reservation with non-existent hotel."""
        self.system.create_customer("C001", "Customer 1", "c1@test.com",
                                    "123456")
        result = self.system.create_reservation("R001", "C001", "NONEXISTENT",
                                                "2026-03-01", "2026-03-05")
        self.assertIsNone(result)

    def test_negative_create_reservation_no_available_rooms(self):
        """NEGATIVE: Test creating reservation when no rooms available."""
        self.system.create_hotel("H001", "Hotel 1", "Location 1", 1)
        self.system.create_customer("C001", "Customer 1", "c1@test.com",
                                    "123456")
        self.system.create_customer("C002", "Customer 2", "c2@test.com",
                                    "789012")
        self.system.create_reservation("R001", "C001", "H001",
                                       "2026-03-01", "2026-03-05")
        result = self.system.create_reservation("R002", "C002", "H001",
                                                "2026-03-01", "2026-03-05")
        self.assertIsNone(result)

    def test_negative_create_reservation_invalid_date_format(self):
        """NEGATIVE: Test creating reservation with invalid date format."""
        self.system.create_hotel("H001", "Hotel 1", "Location 1", 50)
        self.system.create_customer("C001", "Customer 1", "c1@test.com",
                                    "123456")
        result = self.system.create_reservation("R001", "C001", "H001",
                                                "01-03-2026", "05-03-2026")
        self.assertIsNone(result)

    def test_negative_create_reservation_checkout_before_checkin(self):
        """NEGATIVE: Test reservation with check-out before check-in."""
        self.system.create_hotel("H001", "Hotel 1", "Location 1", 50)
        self.system.create_customer("C001", "Customer 1", "c1@test.com",
                                    "123456")
        result = self.system.create_reservation("R001", "C001", "H001",
                                                "2026-03-05", "2026-03-01")
        self.assertIsNone(result)

    def test_negative_create_reservation_same_checkin_checkout(self):
        """NEGATIVE: Test reservation with same check-in/check-out date."""
        self.system.create_hotel("H001", "Hotel 1", "Location 1", 50)
        self.system.create_customer("C001", "Customer 1", "c1@test.com",
                                    "123456")
        result = self.system.create_reservation("R001", "C001", "H001",
                                                "2026-03-01", "2026-03-01")
        self.assertIsNone(result)

    def test_negative_cancel_nonexistent_reservation(self):
        """NEGATIVE: Test cancelling non-existent reservation."""
        result = self.system.cancel_reservation("NONEXISTENT")
        self.assertFalse(result)

    def test_negative_cancel_already_cancelled_reservation(self):
        """NEGATIVE: Test cancelling already cancelled reservation."""
        self.system.create_hotel("H001", "Hotel 1", "Location 1", 50)
        self.system.create_customer("C001", "Customer 1", "c1@test.com",
                                    "123456")
        self.system.create_reservation("R001", "C001", "H001",
                                       "2026-03-01", "2026-03-05")
        self.system.cancel_reservation("R001")
        result = self.system.cancel_reservation("R001")
        self.assertFalse(result)


class TestReservationSystemPositiveCases(unittest.TestCase):
    """Test positive cases for Reservation System."""

    def setUp(self):
        """Set up test environment."""
        self.test_dir = "test_data_positive"
        if os.path.exists(self.test_dir):
            shutil.rmtree(self.test_dir)
        self.system = ReservationSystem(self.test_dir)

    def tearDown(self):
        """Clean up test environment."""
        if os.path.exists(self.test_dir):
            shutil.rmtree(self.test_dir)

    def test_create_hotel_success(self):
        """Test successful hotel creation."""
        hotel = self.system.create_hotel("H001", "Grand Hotel", "NYC", 100)
        self.assertIsNotNone(hotel)
        self.assertEqual(hotel.hotel_id, "H001")

    def test_modify_hotel_success(self):
        """Test successful hotel modification."""
        self.system.create_hotel("H001", "Grand Hotel", "NYC", 100)
        hotel = self.system.modify_hotel("H001", name="Luxury Hotel")
        self.assertIsNotNone(hotel)
        self.assertEqual(hotel.name, "Luxury Hotel")

    def test_delete_hotel_success(self):
        """Test successful hotel deletion."""
        self.system.create_hotel("H001", "Grand Hotel", "NYC", 100)
        result = self.system.delete_hotel("H001")
        self.assertTrue(result)

    def test_create_customer_success(self):
        """Test successful customer creation."""
        customer = self.system.create_customer("C001", "John Doe",
                                               "john@test.com", "123456")
        self.assertIsNotNone(customer)
        self.assertEqual(customer.customer_id, "C001")

    def test_modify_customer_success(self):
        """Test successful customer modification."""
        self.system.create_customer("C001", "John Doe", "john@test.com",
                                    "123456")
        customer = self.system.modify_customer("C001", email="new@test.com")
        self.assertIsNotNone(customer)
        self.assertEqual(customer.email, "new@test.com")

    def test_delete_customer_success(self):
        """Test successful customer deletion."""
        self.system.create_customer("C001", "John Doe", "john@test.com",
                                    "123456")
        result = self.system.delete_customer("C001")
        self.assertTrue(result)

    def test_create_reservation_success(self):
        """Test successful reservation creation."""
        self.system.create_hotel("H001", "Hotel 1", "Location 1", 50)
        self.system.create_customer("C001", "Customer 1", "c1@test.com",
                                    "123456")
        reservation = self.system.create_reservation("R001", "C001", "H001",
                                                     "2026-03-01",
                                                     "2026-03-05")
        self.assertIsNotNone(reservation)
        self.assertEqual(reservation.status, "active")

    def test_cancel_reservation_success(self):
        """Test successful reservation cancellation."""
        self.system.create_hotel("H001", "Hotel 1", "Location 1", 50)
        self.system.create_customer("C001", "Customer 1", "c1@test.com",
                                    "123456")
        self.system.create_reservation("R001", "C001", "H001",
                                       "2026-03-01", "2026-03-05")
        result = self.system.cancel_reservation("R001")
        self.assertTrue(result)

    def test_get_all_hotels(self):
        """Test getting all hotels."""
        self.system.create_hotel("H001", "Hotel 1", "Location 1", 50)
        self.system.create_hotel("H002", "Hotel 2", "Location 2", 75)
        hotels = self.system.get_all_hotels()
        self.assertEqual(len(hotels), 2)

    def test_get_all_customers(self):
        """Test getting all customers."""
        self.system.create_customer("C001", "Customer 1", "c1@test.com",
                                    "123456")
        self.system.create_customer("C002", "Customer 2", "c2@test.com",
                                    "789012")
        customers = self.system.get_all_customers()
        self.assertEqual(len(customers), 2)

    def test_get_all_reservations(self):
        """Test getting all reservations."""
        self.system.create_hotel("H001", "Hotel 1", "Location 1", 50)
        self.system.create_customer("C001", "Customer 1", "c1@test.com",
                                    "123456")
        self.system.create_reservation("R001", "C001", "H001",
                                       "2026-03-01", "2026-03-05")
        reservations = self.system.get_all_reservations()
        self.assertEqual(len(reservations), 1)

    def test_persistence_hotels(self):
        """Test hotel data persistence."""
        self.system.create_hotel("H001", "Hotel 1", "Location 1", 50)
        new_system = ReservationSystem(self.test_dir)
        hotel = new_system.display_hotel("H001")
        self.assertIsNotNone(hotel)
        self.assertEqual(hotel.name, "Hotel 1")

    def test_persistence_customers(self):
        """Test customer data persistence."""
        self.system.create_customer("C001", "Customer 1", "c1@test.com",
                                    "123456")
        new_system = ReservationSystem(self.test_dir)
        customer = new_system.display_customer("C001")
        self.assertIsNotNone(customer)
        self.assertEqual(customer.name, "Customer 1")

    def test_available_rooms_decrease(self):
        """Test that available rooms decrease on reservation."""
        self.system.create_hotel("H001", "Hotel 1", "Location 1", 50)
        self.system.create_customer("C001", "Customer 1", "c1@test.com",
                                    "123456")
        self.system.create_reservation("R001", "C001", "H001",
                                       "2026-03-01", "2026-03-05")
        hotel = self.system.display_hotel("H001")
        self.assertEqual(hotel.available_rooms, 49)

    def test_available_rooms_increase_on_cancel(self):
        """Test that available rooms increase on cancellation."""
        self.system.create_hotel("H001", "Hotel 1", "Location 1", 50)
        self.system.create_customer("C001", "Customer 1", "c1@test.com",
                                    "123456")
        self.system.create_reservation("R001", "C001", "H001",
                                       "2026-03-01", "2026-03-05")
        self.system.cancel_reservation("R001")
        hotel = self.system.display_hotel("H001")
        self.assertEqual(hotel.available_rooms, 50)


if __name__ == '__main__':
    unittest.main()
