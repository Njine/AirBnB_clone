#!/usr/bin/python3
"""
Test collection for Review class in models.review.
"""
import unittest

from models.base_model import BaseModel
from models.review import Review


class TestReview(unittest.TestCase):
    """Test cases for the Review class"""

    def setUp(self):
        """Set up a common Review instance
        and attribute list for testing."""
        self.review = Review()
        self.attr_list = [
            "place_id",
            "user_id",
            "text"
        ]

    def test_review_is_subclass_of_base_model(self):
        """Verify that Review is a subclass of BaseModel."""
        self.assertTrue(issubclass(type(self.review), BaseModel))

    def test_attributes_are_class_attributes(self):
        """Verify that attributes in attr_list
        are class attributes of Review."""
        for attr in self.attr_list:
            self.assertTrue(hasattr(self.review, attr))

    def test_attribute_types_and_defaults(self):
        """Verify that attributes in attr_list
        have correct types and default values."""
        for attr in self.attr_list:
            self.assertIs(type(getattr(self.review, attr)), str)
            self.assertFalse(bool(getattr(self.review, attr)))

    def test_set_attribute_values(self):
        """Verify that setting attribute values
        results in the expected values."""
        expected_place_id = "123"
        expected_user_id = "user456"
        expected_text = "Great place, highly recommended!"

        self.review.place_id = expected_place_id
        self.review.user_id = expected_user_id
        self.review.text = expected_text

        self.assertEqual(self.review.place_id, expected_place_id)
        self.assertEqual(self.review.user_id, expected_user_id)
        self.assertEqual(self.review.text, expected_text)


if __name__ == "__main__":
    unittest.main()
