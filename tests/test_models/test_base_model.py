"""BaseModel Test"""
import unittest
from models.base_model import BaseModel

class TestInit(unittest.TestCase):
    """Test init method"""
    def test_uuid_type(self):
        """Test uuid type"""
        b1 = BaseModel()
        self.assertEqual(type(b1.id), str)

    def test_uuid_uniqe(self):
        """Test uuid unique"""
        b1 = BaseModel()
        b2 = BaseModel()
        self.assertNotEqual(b1.id, b2.id)

    def test_created_at_class(self):
        """Test date time class"""
        b1 = BaseModel()
        self.assertEqual(type(b1.created_at).__name__, "datetime")

    def test_initial_created_at_and_update_at(self):
        """Test initial created_at and update_at"""
        b1 = BaseModel()
        self.assertEqual(b1.created_at, b1.updated_at)


class TestStr(unittest.TestCase):
    def test_str_string(self):
        """Test __str__ method"""
        b1 = BaseModel()
        self.assertAlmostEqual(type(str(b1)), str)

class TestSave(unittest.TestCase):
    def test_save(self):
        """Test save method"""
        b1 = BaseModel()
        b1.save()
        self.assertNotEqual(b1.created_at, b1.updated_at)

class TestToDict(unittest.TestCase):
    def test_to_dict(self):
        """Test to dict method"""
        b1 = BaseModel()
        dic = b1.to_dict()
        for key in dic.keys():
            self.assertAlmostEqual(type(dic[key]), str)


