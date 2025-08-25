import unittest
from app.services.logger_service import LoggerService

class TestLoggerSingleton(unittest.TestCase):
    def test_single_instance(self):
        a = LoggerService()
        b = LoggerService()
        self.assertIs(a, b)      # i njëjti objekt
        a.log("first")
        self.assertEqual(b.logs[-1], "first")

if __name__ == "__main__":
    unittest.main()
