#!/usr/bin/python3
"""
Unittest for class FileStorage
"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import os
import pep8
import unittest


class TestFileStorage(unittest.TestCase):
    """
    defines TestFileStorage, test class for unittests
    """
    def setUp(self):
        self.file_sto1 = FileStorage()

    def tearDown(self):
        del file_sto1

    def test_style_pep8(self):
        """ test files for pep8 style """
        check_style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/base.py'])
        self.assertEqual(result.total_errors, 0, "Review for pep8 style")

    def test_priv_attr(self):
        """ test for class attributes """
        self.assertTrue(hasattr(self.file_sto1, "__file_path"))
        self.assertTrue(hasattr(self.file_sto1, "__objects"))

    def test_all_exists(self):
        """ test for available class method all() """
        self.assertTrue(hasattr(self.file_sto1, "all"))

    def test_all(self):
        """ test for functionality class method all() """
        result = FileStorage.__objects
        self.assertEqual(result, 

    def test_new_exists(self):
        """ test for available class method new() """
        self.assertTrue(hasattr(self.file_sto1, "new"))

    def test_new(self):
        """ test for functionality class method new() """
        self.assertTrue(hasattr(self.file_sto1, "new"))

    def test_save_exists(self):
        """ test for available class method save() """
        self.assertTrue(hasattr(self.file_sto1, "save"))

    def test_save(self):
        """ test for functionality class method save() """
        self.assertTrue(hasattr(self.file_sto1, "save"))

    def test_reload_exists(self):
        """ test for available class method reload() """
        self.assertTrue(hasattr(self.file_sto1, "reload"))

    def test_reload(self):
        """ test for class method reload() """
        self.assertTrue(hasattr(self.file_sto1, "reload"))

if __name__ == '__main__':
        unittest.main()
