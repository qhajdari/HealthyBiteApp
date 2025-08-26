import unittest
from app.services.stats_service import threaded_stats

class TestStatsService(unittest.TestCase):
    def test_threaded_stats(self):
        s = threaded_stats([10, 20, 30])
        self.assertEqual(s["min"], 10)
        self.assertEqual(s["max"], 30)
        self.assertAlmostEqual(s["avg"], 20.0, places=5)

    def test_threaded_stats_empty(self):
        s = threaded_stats([])
        self.assertIsNone(s["min"])
        self.assertIsNone(s["max"])
        self.assertIsNone(s["avg"])

