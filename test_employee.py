import unittest
from unittest import TestCase

from Employee import Employee


class TestEmployee(unittest.TestCase):

    def setUp(self):
        self.employee = Employee(456, "Michael Lafata", 11 / 15 / 2023)

    # This is a true test case for setName() method when you set a specific name, and you expect the same name was set
    def test_setNameTrue(self):
        self.employee.setName("Michael Lafata")
        self.assertEqual(self.employee.getName(), "Michael Lafata")

    # This is a false test case for setName() method when you set a specific name but your expectation is different name
    def test_setNameFalse(self):
        self.employee.setName("Ben David")
        self.assertEqual(self.employee.getName(), "Ben David")

    # This is a true test case for setID() method when you set a specific id, and you expect the same id was set
    def test_setIDTrue(self):
        self.employee.setID(456)
        self.assertEqual(self.employee.getID(), 456)

    # This is a false test case for setID() method when you set a specific id but your expectation is different id
    def test_setIDFalse(self):
        self.employee.setID(789)
        self.assertEqual(self.employee.getID(), 456)


if __name__ == "__main__":
    var = unittest.main


