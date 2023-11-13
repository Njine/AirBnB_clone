#!/usr/bin/python3
"""Defines unittests for console.py.
Unittest classes:
    TestHBNBCommand_prompting
    TestHBNBCommand_help
    TestHBNBCommand_exit
    TestHBNBCommand_create
    TestHBNBCommand_show
    TestHBNBCommand_all
    TestHBNBCommand_destroy
    TestHBNBCommand_update
"""
import os
import sys
import unittest
from models import storage
from models.engine.file_storage import FileStorage
from console import HBNBCommand
from io import StringIO
from unittest.mock import patch


class TestHBNBCommand_prompting(unittest.TestCase):
    def test_some_prompting_function(self):
        #  test code here
        pass


class TestHBNBCommand_help(unittest.TestCase):
    def test_help_function(self):
        # test code here
        pass


class TestHBNBCommand_exit(unittest.TestCase):
    def test_exit_function(self):
        # test code here
        pass


class TestHBNBCommand_create(unittest.TestCase):
    def test_create_function(self):
        # test code here
        pass


class TestHBNBCommand_show(unittest.TestCase):
    def test_show_function(self):
        # test code here
        pass


class TestHBNBCommand_all(unittest.TestCase):
    def test_all_function(self):
        # test code here
        pass


class TestHBNBCommand_destroy(unittest.TestCase):
    def test_destroy_function(self):
        #  test code here
        pass


class TestHBNBCommand_update(unittest.TestCase):
    def test_update_function(self):
        # test code here
        pass


if __name__ == '__main__':
    unittest.main()
