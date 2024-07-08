import unittest

from calculations import calculate_discount, calculate_amount_by_time, calculate_amount_by_distance
from exceptions import DiscountException, UnitException


class TestCalculation(unittest.TestCase):
    def test_discount_tec5(self):
        self.assertEqual(calculate_discount(10, "Tec5"), 9.50)

    def test_discount_tec15(self):
        self.assertEqual(calculate_discount(10, "Tec15"), 8.50)

    def test_discount_tecfirsttry(self):
        self.assertEqual(calculate_discount(10, "TecFirstTry"), 5)

    def test_discount_none(self):
        self.assertEqual(calculate_discount(10, None), 10)

    def test_discount_error(self):
        with self.assertRaises(DiscountException):
            calculate_discount(10, "Ligeia")

    def test_meter_rate(self):
        self.assertEqual(calculate_amount_by_distance(500, "meter"), 0.33)

    def test_kilometer_rate(self):
        self.assertEqual(calculate_amount_by_distance(1, "kilometer"), 0.66)

    def test_distance_rate_error(self):
        with self.assertRaises(UnitException):
            calculate_amount_by_distance(1, "haku")

    def test_minute_rate(self):
        self.assertEqual(calculate_amount_by_time(30, "minuten"), 6.60)

    def test_hour_rate(self):
        self.assertEqual(calculate_amount_by_time(1, "stunden"), 13.20)

    def test_time_rate_error(self):
        with self.assertRaises(UnitException):
            calculate_amount_by_time(1, "fleur5")
