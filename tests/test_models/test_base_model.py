#!/usr/bin/python3
"""
Module containing the test suite for the BaseModel class.
"""
import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """
    Test suite for the BaseModel class in models.base_model module.
    """
    def test_created_at_is_datetime(self):
        """
        Verifies that the attribute 'created_at' is a datetime object.
        """
        b = BaseModel()
        self.assertTrue(type(b.created_at) is datetime)

    def test_updated_at_is_datetime(self):
        """
        Verifies that the attribute 'updated_at' is a datetime object.
        """
        b = BaseModel()
        self.assertTrue(type(b.updated_at) is datetime)

    def test_str_representation(self):
        """
        Checks if the string representation is appropriate.
        """
        b = BaseModel()
        self.assertEqual(str(b),
                         "[BaseModel] ({}) {}".format(b.id, b.__dict__))

    def test_ids_is_unique(self):
        """
        Verifies that id is generated randomly and uniquely.
        """
        b1 = BaseModel()
        b2 = BaseModel()
        self.assertNotEqual(b1.id, b2.id)

    def test_type_of_id_is_str(self):
        """
        Verifies that the generated id is a str object.
        """
        b = BaseModel()
        self.assertTrue(type(b.id) is str)

    def test_if_BaseModel_instance_has_id(self):
        """
        Verifies that an instance has an id assigned on initialization.
        """
        b = BaseModel()
        self.assertTrue(hasattr(b, "id"))
