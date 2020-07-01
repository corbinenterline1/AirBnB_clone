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

    def test_testobjs(self):
        """
        Make sure objects exist
        Make sure they are right type
        """
        self.tstate_a = State()
        self.assertTrue(self.tstate_a)
        self.assertTrue(type(self.tstate_a.__class__) is type)

    def test_b(self):
        """
        B test
        """
        self.tstate_b = State()
        self.assertTrue(self.tstate_b)
        self.assertTrue(type(self.tstate_b.__class__) is type)
