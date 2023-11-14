#!/usr/bin/python3
"""
Test collection for the Place class in models.place.
"""
import unittest

from models.base_model import BaseModel
from models.place import Place


class TestPlace(unittest.TestCase):
    """Test cases for the Place class"""

    def setUp(self):
        """Set up a common Place instance
        and attribute list for testing."""
        self.place = Place()
        self.attr_list = ["name", "user_id", "city_id", "description",
                          "number_bathrooms", "max_guest", "number_rooms",
                          "price_by_night", "latitude", "longitude",
                          "amenity_ids"]

    def test_attributes_are_class_attributes(self):
        """Verify that attributes in attr_list
        are class attributes of Place."""
        for attr in self.attr_list:
            self.assertTrue(hasattr(Place, attr))

    def test_attribute_types_and_defaults(self):
        """Verify that attributes in attr_list
        have correct types and default values."""
        self.assertIs(type(self.place.name), str)
        self.assertIs(type(self.place.city_id), str)
        self.assertIs(type(self.place.user_id), str)
        self.assertIs(type(self.place.description), str)
        self.assertIs(type(self.place.number_bathrooms), int)
        self.assertIs(type(self.place.max_guest), int)
        self.assertIs(type(self.place.number_rooms), int)
        self.assertIs(type(self.place.price_by_night), int)
        self.assertIs(type(self.place.latitude), float)
        self.assertIs(type(self.place.longitude), float)
        self.assertIs(type(self.place.amenity_ids), list)

        for attr in self.attr_list:
            self.assertFalse(bool(getattr(self.place, attr)))

    def test_place_object_is_subclass_of_base_model(self):
        """Verify that Place is a subclass of BaseModel."""
        self.assertTrue(issubclass(type(self.place), BaseModel))

    def test_set_attribute_values(self):
        """Verify that setting attribute values
        results in the expected values."""
        expected_name = "Cozy House"
        expected_city_id = "SF"
        expected_user_id = "user123"
        expected_description = "A lovely place with a view"
        expected_bathrooms = 2
        expected_max_guest = 4
        expected_rooms = 2
        expected_price = 100
        expected_latitude = 37.7749
        expected_longitude = -122.4194
        expected_amenity_ids = ["wifi", "parking"]

        self.place.name = expected_name
        self.place.city_id = expected_city_id
        self.place.user_id = expected_user_id
        self.place.description = expected_description
        self.place.number_bathrooms = expected_bathrooms
        self.place.max_guest = expected_max_guest
        self.place.number_rooms = expected_rooms
        self.place.price_by_night = expected_price
        self.place.latitude = expected_latitude
        self.place.longitude = expected_longitude
        self.place.amenity_ids = expected_amenity_ids

        self.assertEqual(self.place.name, expected_name)
        self.assertEqual(self.place.city_id, expected_city_id)
        self.assertEqual(self.place.user_id, expected_user_id)
        self.assertEqual(self.place.description, expected_description)
        self.assertEqual(self.place.number_bathrooms, expected_bathrooms)
        self.assertEqual(self.place.max_guest, expected_max_guest)
        self.assertEqual(self.place.number_rooms, expected_rooms)
        self.assertEqual(self.place.price_by_night, expected_price)
        self.assertEqual(self.place.latitude, expected_latitude)
        self.assertEqual(self.place.longitude, expected_longitude)
        self.assertEqual(self.place.amenity_ids, expected_amenity_ids)


if __name__ == "__main__":
    unittest.main()
