#!/usr/bin/python3
"""
Amenity class Test Module.
"""
import unittest
import datetime
from models.amenity import Amenity
from models import storage


class TestAmenity(unittest.TestCase):
    """
    Amenity class test GO
    """

    def setUp(self):
        """
        SET
        """
        self.tamen_a = Amenity()
        self.tamen_b = Amenity()

    def test_testobjs(self):
        """
        Make sure objects exist
        Make sure they are right type
        """
        self.assertTrue(self.tamen_a)
        self.assertTrue(type(self.tamen_a.__class__) is type)
        self.assertTrue(self.tamen_b)
        self.assertTrue(type(self.tamen_b.__class__) is type)

    def test_attributes(self):
        """
        Make sure attribute exists
        Make sure right type
        """
        self.assertTrue(hasattr(self.tamen_a, "name"))
        self.assertIsInstance(self.tamen_a.name, str)
        self.assertTrue(hasattr(self.tamen_a, "id"))
        self.assertIsInstance(self.tamen_a.id, str)

    def test_save_method(self):
        """
        Save testing
        """
        self.oldupdate = self.tamen_a.updated_at
        self.tamen_a.save()
        self.assertTrue(self.oldupdate != self.tamen_a.created_at)


if __name__ == '__main__':
    unittest.main()
