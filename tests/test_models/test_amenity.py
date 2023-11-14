#!/usr/bin/python3
"""
Test collection for the Amenity class in the models.amenity module.
"""
import unittest

from models.base_model import BaseModel
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Test cases for the Amenity class"""

    def setUp(self):
        """Set up a common Amenity instance for testing."""
        self.amenity = Amenity()

    def test_amenity_is_subclass_of_base_model(self):
        """Verify that Amenity is a subclass of BaseModel."""
        self.assertTrue(issubclass(type(self.amenity), BaseModel))

    def test_name_is_class_attribute(self):
        """Verify that 'name' is a class attribute of Amenity."""
        self.assertTrue(hasattr(self.amenity, "name"))

    def test_name_attribute_type(self):
        """Verify that the 'name' attribute is of type str."""
        self.assertIs(type(self.amenity.name), str)

    def test_name_attribute_has_default_value(self):
        """Verify that the 'name' attribute has a default value."""
        self.assertFalse(bool(self.amenity.name))

    def test_set_name_attribute(self):
        """Verify that setting the 'name' attribute
        results in the expected value."""
        expected_name = "NewAmenity"
        self.amenity.name = expected_name
        self.assertEqual(self.amenity.name, expected_name)


if __name__ == "__main__":
    unittest.main()
