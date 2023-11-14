#!/usr/bin/python3
"""
Test collection for the User class in models.user.
"""
import unittest
from models.base_model import BaseModel
from models.user import User


class TestUser(unittest.TestCase):
    """Test cases against the User class"""

    def test_attribute_types_and_defaults(self):
        """Verify that 'first_name' and
        'last_name' have correct types and default values."""
        user = User()
        self.assertIs(type(user.first_name), str)
        self.assertIs(type(user.last_name), str)
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")

    def test_user_is_subclass_of_base_model(self):
        """Verify that User is a subclass of BaseModel."""
        user = User()
        self.assertTrue(issubclass(type(user), BaseModel))

    def test_set_attribute_values(self):
        """Verify that setting attribute values
        results in the expected values."""
        user = User()
        expected_first_name = "John"
        expected_last_name = "Doe"

        user.first_name = expected_first_name
        user.last_name = expected_last_name

        self.assertEqual(user.first_name, expected_first_name)
        self.assertEqual(user.last_name, expected_last_name)


if __name__ == "__main__":
    unittest.main()
