import unittest
from src.converter import celsius_to_fahrenheit, fahrenheit_to_celsius


class TestConverter(unittest.TestCase):
    """Test suite cho module converter (Issue: Add temperature conversion)."""

    def test_celsius_to_fahrenheit_zero(self):
        self.assertAlmostEqual(celsius_to_fahrenheit(0), 32)

    def test_celsius_to_fahrenheit_hundred(self):
        self.assertAlmostEqual(celsius_to_fahrenheit(100), 212)

    def test_fahrenheit_to_celsius_freezing(self):
        self.assertAlmostEqual(fahrenheit_to_celsius(32), 0)

    def test_fahrenheit_to_celsius_boiling(self):
        self.assertAlmostEqual(fahrenheit_to_celsius(212), 100)

    def test_fahrenheit_to_celsius_negative(self):
        # -40°F bằng -40°C
        self.assertAlmostEqual(fahrenheit_to_celsius(-40), -40)

    def test_fahrenheit_to_celsius_decimal(self):
        # 98.6°F (nhiệt độ cơ thể) tương đương 37°C
        self.assertAlmostEqual(fahrenheit_to_celsius(98.6), 37, places=2)

    def test_negative_values(self):
        # -40 độ C bằng -40 độ F
        self.assertAlmostEqual(celsius_to_fahrenheit(-40), -40)
        self.assertAlmostEqual(fahrenheit_to_celsius(-40), -40)


if __name__ == "__main__":
    unittest.main()