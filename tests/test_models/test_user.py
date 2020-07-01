#!/usr/bin/python3
"""
User class Test Module.
"""
import unittest
import datetime
from models.user import User
from models import storage


class TestUser(unittest.TestCase):
    """
    User class test GO
    """

    def setUp(self):
        """
        SET
        """
        self.tuser_a = User()
        self.tuser_b = User()

    def test_testobjs(self):
        """
        Make sure objects exist
        Make sure they are right type
        """
        self.assertTrue(self.tuser_a)
        self.assertTrue(type(self.tuser_a.__class__) is type)
        self.assertTrue(self.tuser_b)
        self.assertTrue(type(self.tuser_b.__class__) is type)

    def test_attributes(self):
        """
        Make sure attribute exists
        Make sure right type
        """
        self.assertTrue(hasattr(self.tuser_a, "email"))
        self.assertIsInstance(self.tuser_a.email, str)
        self.assertTrue(hasattr(self.tuser_a, "password"))
        self.assertIsInstance(self.tuser_a.password, str)
        self.assertTrue(hasattr(self.tuser_a, "first_name"))
        self.assertIsInstance(self.tuser_a.first_name, str)
        self.assertTrue(hasattr(self.tuser_a, "last_name"))
        self.assertIsInstance(self.tuser_a.last_name, str)
        self.assertTrue(hasattr(self.tuser_a, "id"))
        self.assertIsInstance(self.tuser_a.id, str)

    def test_save_method(self):
        """
        Save testing
        """
        self.oldupdate = self.tuser_a.updated_at
        self.tuser_a.save()
        self.assertTrue(self.oldupdate != self.tuser_a.created_at)


if __name__ == '__main__':
    unittest.main()
