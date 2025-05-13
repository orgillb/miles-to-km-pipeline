import unittest
from converter import miles_to_km

class TestConverter(unittest.TestCase):
    def test_standard_value(self):
        self.assertEqual(miles_to_km(1), 1.61)

    def test_zero(self):
        self.assertEqual(miles_to_km(0), 0.0)

    def test_string_number(self):
        self.assertEqual(miles_to_km("5"), 8.05)

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            miles_to_km("abc")

if __name__ == '__main__':
    unittest.main()
