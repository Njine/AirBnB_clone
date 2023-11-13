#!/usr/bin/python3

"""Unittest module for the Amenity Class."""

import unittest
import os
import sys
from models import storage
from models.amenity import Amenity
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """Test Cases for the Amenity class."""

    def setUp(self):
        """Sets up test methods."""
        pass

    def tearDown(self):
        """Tears down test methods."""
        self.resetStorage()

    def resetStorage(self):
        """Resets FileStorage data."""
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_instantiation(self):
        """Tests instantiation of Amenity class."""
        amenity_instance = Amenity()
        self.assertIsInstance(amenity_instance, Amenity)
        self.assertTrue(issubclass(type(amenity_instance), BaseModel))

    def test_attributes(self):
        """Tests the attributes of Amenity class."""
        amenity_instance = Amenity()
        self.assertTrue(hasattr(amenity_instance, 'name'))


if __name__ == "__main__":
    unittest.main()
