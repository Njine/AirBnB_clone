#!/usr/bin/python3
"""
Test collection for the City class in the models.city module.
"""
import unittest

from models.base_model import BaseModel
from models.city import City


class TestCity(unittest.TestCase):
    """Test cases for the City class"""

    def setUp(self):
        """Set up a common City instance and attribute list for testing."""
        self.city = City()
        self.attr_list = ["state_id", "name"]

    def test_city_is_subclass_of_base_model(self):
        """Verify that City is a subclass of BaseModel."""
        self.assertTrue(issubclass(type(self.city), BaseModel))

    def test_attributes_are_class_attributes(self):
        """Verify that attributes in attr_list are class attributes of City."""
        for attr in self.attr_list:
            self.assertTrue(hasattr(self.city, attr))

    def test_attribute_types(self):
        """Verify that attributes in attr_list are of type str."""
        for attr in self.attr_list:
            self.assertIs(type(getattr(self.city, attr)), str)

    def test_attributes_have_default_values(self):
        """Verify that attributes in attr_list have default values."""
        for attr in self.attr_list:
            self.assertFalse(bool(getattr(self.city, attr)))

    def test_set_attribute_values(self):
        """Verify that setting attribute values results in the expected values."""
        expected_state_id = "CA"
        expected_name = "San Francisco"

        self.city.state_id = expected_state_id
        self.city.name = expected_name

        self.assertEqual(self.city.state_id, expected_state_id)
        self.assertEqual(self.city.name, expected_name)


if __name__ == "__main__":
    unittest.main()
