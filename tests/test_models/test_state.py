#!/usr/bin/python3
"""
State class Test Module.
"""
import unittest
import datetime
from models.state import State
from models import storage


class TestState(unittest.TestCase):
    """
    State class test GO
    """

    def setUp(self):
        """
        SET
        """
        self.tstate_a = State()
        self.tstate_b = State()

    def tearDown(self):
        """
        deletes test cases
        """
        del self.tstate_a
        del self.tstate_b

    def test_testobjs(self):
        """
        Make sure objects exist
        Make sure they are right type
        """
        self.assertTrue(self.tstate_a)
        self.assertTrue(type(self.tstate_a.__class__) is type)
        self.assertTrue(self.tstate_b)
        self.assertTrue(type(self.tstate_b.__class__) is type)

    def test_attributes(self):
        """
        Make sure attribute exists
        Make sure right type
        """
        self.assertTrue(hasattr(self.tstate_a, "name"))
        self.assertIsInstance(self.tstate_a.name, str)
        self.assertTrue(hasattr(self.tstate_a, "id"))
        self.assertIsInstance(self.tstate_a.id, str)

    def test_save_method(self):
        """
        Save testing
        """
        self.oldupdate = self.tstate_a.updated_at
        self.tstate_a.save()
        self.assertTrue(self.oldupdate != self.tstate_a.created_at)


if __name__ == '__main__':
    unittest.main()
