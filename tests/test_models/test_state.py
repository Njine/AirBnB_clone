#!/usr/bin/python3
"""
Test collection for the State class in models.state.
"""
import unittest

from models.base_model import BaseModel
from models.state import State


class TestState(unittest.TestCase):
    """Test cases for the State class"""

    def setUp(self):
        """Set up a common State instance for testing."""
        self.state = State()

    def test_state_is_subclass_of_base_model(self):
        """Verify that State is a subclass of BaseModel."""
        self.assertTrue(issubclass(type(self.state), BaseModel))

    def test_name_is_class_attribute(self):
        """Verify that 'name' is a class attribute of State."""
        self.assertTrue(hasattr(self.state, "name"))

    def test_name_attribute_type(self):
        """Verify that the 'name' attribute is of type str."""
        self.assertIs(type(self.state.name), str)

    def test_name_attribute_has_default_value(self):
        """Verify that the 'name' attribute has a default value."""
        self.assertFalse(bool(self.state.name))

    def test_set_name_attribute(self):
        """Verify that setting the 'name'
        attribute results in the expected value."""
        expected_name = "California"
        self.state.name = expected_name
        self.assertEqual(self.state.name, expected_name)


if __name__ == "__main__":
    unittest.main()
