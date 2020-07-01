#!/usr/bin/python3
"""
Place class Test Module.
"""
import unittest
import datetime
from models.place import Place
from models import storage


class TestPlace(unittest.TestCase):
    """
    Place class test GO
    """

    def setUp(self):
        """
        SET
        """
        self.tplac_a = Place()
        self.tplac_b = Place()

    def test_testobjs(self):
        """
        Make sure objects exist
        Make sure they are right type
        """
        self.assertTrue(self.tplac_a)
        self.assertTrue(type(self.tplac_a.__class__) is type)
        self.assertTrue(self.tplac_b)
        self.assertTrue(type(self.tplac_b.__class__) is type)

    def test_attributes(self):
        """
        Make sure attribute exists
        Make sure right type
        """
        self.assertTrue(hasattr(self.tplac_a, "city_id"))
        self.assertIsInstance(self.tplac_a.city_id, str)
        self.assertTrue(hasattr(self.tplac_a, "user_id"))
        self.assertIsInstance(self.tplac_a.user_id, str)
        self.assertTrue(hasattr(self.tplac_a, "name"))
        self.assertIsInstance(self.tplac_a.name, str)
        self.assertTrue(hasattr(self.tplac_a, "description"))
        self.assertIsInstance(self.tplac_a.description, str)
        self.assertTrue(hasattr(self.tplac_a, "number_rooms"))
        self.assertIsInstance(self.tplac_a.number_rooms, int)
        self.assertTrue(hasattr(self.tplac_a, "number_bathrooms"))
        self.assertIsInstance(self.tplac_a.number_bathrooms, int)
        self.assertTrue(hasattr(self.tplac_a, "max_guest"))
        self.assertIsInstance(self.tplac_a.max_guest, int)
        self.assertTrue(hasattr(self.tplac_a, "price_by_night"))
        self.assertIsInstance(self.tplac_a.price_by_night, int)
        self.assertTrue(hasattr(self.tplac_a, "latitude"))
        self.assertIsInstance(self.tplac_a.latitude, float)
        self.assertTrue(hasattr(self.tplac_a, "longitude"))
        self.assertIsInstance(self.tplac_a.longitude, float)
        self.assertTrue(hasattr(self.tplac_a, "amenity_ids"))
        self.assertIsInstance(self.tplac_a.amenity_ids, list)
        self.assertTrue(hasattr(self.tplac_a, "id"))
        self.assertIsInstance(self.tplac_a.id, str)

    def test_save_method(self):
        """
        Save testing
        """
        self.oldupdate = self.tplac_a.updated_at
        self.tplac_a.save()
        self.assertTrue(self.oldupdate != self.tplac_a.created_at)


if __name__ == '__main__':
    unittest.main()
