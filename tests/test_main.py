import main
import unittest


class TestMain(unittest.TestCase):
    def test_attendance_case1(self):
        data = main.attendance(consecutive_absent=0, nth_class=0, total_days=5)
        self.assertEqual(data.valid_classes, 29)
        self.assertEqual(data.days_missed_ceremony, 14)

    def test_attendance_case2(self):
        data = main.attendance(consecutive_absent=0, nth_class=0, total_days=10)
        self.assertEqual(data.valid_classes, 773)
        self.assertEqual(data.days_missed_ceremony, 372)
