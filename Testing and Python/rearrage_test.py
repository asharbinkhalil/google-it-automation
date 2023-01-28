from rearrange import rearrange_name
import unittest

class Rearragename(unittest.TestCase):
    def test_basic(self):
        testcase="Khalil, Ashar"
        expected="Ashar Khalil"
        self.assertEqual(rearrange_name(testcase),expected)

    def test_empty(self):
        testcase=""
        expected=""
        self.assertEqual(rearrange_name(testcase),expected)

    def test_single_name(self):
        testcase="Ashar"
        expected="Ashar"
        self.assertEqual(rearrange_name(testcase),expected)


unittest.main()