#!/usr/bin/python3

"""Unittest module for the City Class"""
import unittest
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """Test Cases for the City class."""

    def test_attributes(self):
        """Tests the attributes of City class."""
        city_instance = City()
        self.assertTrue(hasattr(city_instance, 'state_id'))
        self.assertTrue(hasattr(city_instance, 'name'))
        self.assertEqual(type(getattr(city_instance, 'state_id', None)), str)
        self.assertEqual(type(getattr(city_instance, 'name', None)), str)

    def test_attribute_default_values(self):
        """Tests default values of attributes."""
        city_instance = City()
        self.assertEqual(city_instance.state_id, "")
        self.assertEqual(city_instance.name, "")

    def test_setting_attributes(self):
        """Tests setting attributes of City class."""
        city_instance = City()
        city_instance.state_id = "CA"
        city_instance.name = "San Francisco"
        self.assertEqual(city_instance.state_id, "CA")
        self.assertEqual(city_instance.name, "San Francisco")

    def test_to_dict_method(self):
        """Tests the to_dict method of City class."""
        city_instance = City()
        city_dict = city_instance.to_dict()
        print("City Dict Keys:", city_dict.keys())
        self.assertEqual(type(city_dict), dict)
        self.assertEqual(city_dict.get('state_id', ""), "")
        self.assertEqual(city_dict.get('name', ""), "")


if __name__ == "__main__":
    unittest.main()
