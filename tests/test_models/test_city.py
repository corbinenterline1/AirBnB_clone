#!/usr/bin/python3
"""
City class Test Module.
"""
import unittest
import datetime
from models.city import City
from models import storage


class TestCity(unittest.TestCase):
    """
    City class test GO
    """

    def setUp(self):
        """
        SET
        """
        self.tcit_a = City()
        self.tcit_b = City()

    def test_testobjs(self):
        """
        Make sure objects exist
        Make sure they are right type
        """
        self.assertTrue(self.tcit_a)
        self.assertTrue(type(self.tcit_a.__class__) is type)
        self.assertTrue(self.tcit_b)
        self.assertTrue(type(self.tcit_b.__class__) is type)

    def test_attributes(self):
        """
        Make sure attribute exists
        Make sure right type
        """
        self.assertTrue(hasattr(self.tcit_a, "name"))
        self.assertIsInstance(self.tcit_a.name, str)
        self.assertTrue(hasattr(self.tcit_a, "state_id"))
        self.assertIsInstance(self.tcit_a.state_id, str)
        self.assertTrue(hasattr(self.tcit_a, "id"))
        self.assertIsInstance(self.tcit_a.id, str)

    def test_save_method(self):
        """
        Save testing
        """
        self.oldupdate = self.tcit_a.updated_at
        self.tcit_a.save()
        self.assertTrue(self.oldupdate != self.tcit_a.created_at)


if __name__ == '__main__':
    unittest.main()
