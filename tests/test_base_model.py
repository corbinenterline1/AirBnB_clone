#!/usr/bin/python3
"""
base_model unittest module.
"""
import unittest
import datetime
import json
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """
    BaseModel class Test GO
    """

    def setUp(self):
        """
        Creating test BaseModel objects & dict for kwargs.
        """

        self.tbm_a = BaseModel()
        self.tbm_b = BaseModel()

    def test_testobjs(self):
        """
        For each test object:
        1) Confirm it exists
        2) Confirm proper type
        """

        self.assertTrue(self.tbm_a)
        self.assertTrue(type(self.tbm_a.__class__) is type)
        self.assertTrue(self.tbm_b)
        self.assertTrue(type(self.tbm_b.__class__) is type)

    def test_attributes(self):
        """
        For each attribute:
        1) Confirm it exists
        2) Confirm proper type
        """

        self.assertTrue(hasattr(self.tbm_a, "id"))
        self.assertIsInstance(self.tbm_a.id, str)
        self.assertTrue(hasattr(self.tbm_b, "id"))
        self.assertIsInstance(self.tbm_b.id, str)
        a_created_at = self.tbm_a.created_at
        a_updated_at = self.tbm_a.updated_at
        b_created_at = self.tbm_b.created_at

    def test_time(self):
        """
        Tests that times are equal, minus microseconds
        """
        self.assertTrue(self.tbm_a.created_at != self.tbm_b.created_at)

    def test_save_method(self):
        """
        Save testing. Expected output
        """
        self.tbm_a.save()
        self.a_updated_at_new = self.tbm_a.updated_at
        self.assertTrue(self.a_updated_at_new != self.tbm_a.created_at)

    def test_to_dict_method(self):
        """
        Make sure to_dict result is dict type
        Try empty
        """
        self.testdic = self.tbm_a.to_dict()
        self.assertIsInstance(self.testdic, dict)

if __name__ == '__main__':
        unittest.main()
