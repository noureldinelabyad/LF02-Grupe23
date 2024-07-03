import unittest

import calculation


class TestCalculation(unittest.TestCase):
    def test_discount_tec5(self):
        self.assertEqual(calculation.apply_discount(10, "Tec5"), 9.50)

    def test_discount_tec15(self):
        self.assertEqual(calculation.apply_discount(10, "Tec15"), 8.50)

    def test_discount_tecfirsttry(self):
        self.assertEqual(calculation.apply_discount(10, "TecFirstTry"), 5)

    def test_discount_error(self):
        self.assertEqual(calculation.apply_discount(10, "Test"), 10)

    def test_meter_rate(self):
        self.assertEqual(calculation.calculate_amount_by_distance(500, "meter"), 0.33)

    def test_kilometer_rate(self):
        self.assertEqual(calculation.calculate_amount_by_distance(1, "kilometer"), 0.66)

    def test_disctance_rate_error(self):
        self.assertEqual(calculation.calculate_amount_by_distance(1, "kilometter"), None)

    def test_minute_rate(self):
        self.assertEqual(calculation.calculate_amount_by_time(30, "minuten"), 6.60)

    def test_hour_rate(self):
        self.assertEqual(calculation.calculate_amount_by_time(1, "stunden"), 13.20)

    def test_time_rate_error(self):
        self.assertEqual(calculation.calculate_amount_by_time(1, "mineuten"), None)