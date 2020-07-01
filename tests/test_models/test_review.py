#!/usr/bin/python3
"""
Review class Test Module.
"""
import unittest
import datetime
from models.review import Review
from models import storage


class TestReview(unittest.TestCase):
    """
    Review class test GO
    """

    def setUp(self):
        """
        SET
        """
        self.trev_a = Review()
        self.trev_b = Review()

    def test_testobjs(self):
        """
        Make sure objects exist
        Make sure they are right type
        """
        self.assertTrue(self.trev_a)
        self.assertTrue(type(self.trev_a.__class__) is type)
        self.assertTrue(self.trev_b)
        self.assertTrue(type(self.trev_b.__class__) is type)

    def test_attributes(self):
        """
        Make sure attribute exists
        Make sure right type
        """
        self.assertTrue(hasattr(self.trev_a, "place_id"))
        self.assertIsInstance(self.trev_a.place_id, str)
        self.assertTrue(hasattr(self.trev_a, "user_id"))
        self.assertIsInstance(self.trev_a.user_id, str)
        self.assertTrue(hasattr(self.trev_a, "text"))
        self.assertIsInstance(self.trev_a.text, str)
        self.assertTrue(hasattr(self.trev_a, "id"))
        self.assertIsInstance(self.trev_a.id, str)

    def test_save_method(self):
        """
        Save testing
        """
        self.oldupdate = self.trev_a.updated_at
        self.trev_a.save()
        self.assertTrue(self.oldupdate != self.trev_a.created_at)


if __name__ == '__main__':
    unittest.main()
