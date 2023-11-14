#!/usr/bin/python3
import os.path
import unittest
import models
from models import base_model
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.amenity import Amenity
from models.city import City
from models.review import Review
from models.place import Place
"""
Test collection for FileStorage Module
"""


class TestFileStorage(unittest.TestCase):
    """Unit tests for FileStorage class and methods."""

    def setUp(self):
        """Prepare for tests:
        - If 'file.json' exists, rename it to 'tempfile'
        - Initialize FileStorage and BaseModel objects
        """
        if os.path.isfile('file.json'):
            os.rename('file.json', 'tempfile')
        self.storage = FileStorage()
        self.base = BaseModel()

    def tearDown(self):
        """Clean up after tests:
        - Rename 'tempfile' back to 'file.json'
        - Delete created objects
        """
        if os.path.isfile('tempfile'):
            os.rename('tempfile', 'file.json')
        del self.storage
        del self.base

    def test_attributes(self):
        """Check attributes of initialized objects."""
        self.assertTrue(hasattr(self.base, "created_at"))
        self.assertTrue(hasattr(self.base, "updated_at"))
        self.assertTrue(hasattr(self.base, "id"))
        self.assertTrue(hasattr(self.base, "__class__"))
        self.assertEqual(self.base.__class__.__name__, "BaseModel")
        self.assertEqual(self.storage._FileStorage__file_path, "file.json")
        self.assertIsInstance(self.storage._FileStorage__objects, dict)

    def test_all_method(self):
        """Test the all() method of FileStorage."""
        all_objs_dict = self.storage.all()
        base_id = "BaseModel." + self.base.id
        self.assertIsInstance(all_objs_dict, dict)
        self.assertIn(base_id, all_objs_dict)


class TestFileStorageInit(unittest.TestCase):
    """Contains test cases against the FileStorage initialization"""

    def test_file_path_is_a_private_class_attr(self):
        """Checks that file_path is a private class attribute"""
        self.assertFalse(hasattr(FileStorage(), "__file_path"))

    def test_objects_is_a_private_class_attr(self):
        """Checks that objects is a private class attribute"""
        self.assertFalse(hasattr(FileStorage(), "__objects"))

    def test_init_without_arg(self):
        """Tests initialization without args"""
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_init_with_arg(self):
        """Tests initialization with args"""
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_storage_initialization(self):
        """Tests storage created in __init__.py"""
        self.assertEqual(type(models.storage), FileStorage)


if __name__ == "__main__":
    unittest.main()
